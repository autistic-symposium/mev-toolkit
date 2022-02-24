from eth_account.signers.local import LocalAccount
from web3.middleware import construct_sign_and_send_raw_middleware

from flashbots import flashbot
from flashbots.types import SignTx
from eth_account.account import Account
from web3 import Web3, HTTPProvider
from web3.types import TxParams, Wei

import os

"""
In this example we setup a transaction for 0.1 eth with a gasprice of 1
From here we will use Flashbots to pass a bundle with the needed content
"""

# ETH_ACCOUNT_SIGNATURE is an Ethereum private key that does NOT store funds and is NOT your bot's primary key.
#This is an identifying key for signing payloads to establish reputation and whitelisting
ETH_ACCOUNT_SIGNATURE: LocalAccount = Account.from_key(os.environ.get("ETH_SIGNATURE_KEY"))
ETH_ACCOUNT_FROM: LocalAccount = Account.from_key(os.environ.get("ETH_PRIVATE_FROM"))
ETH_ACCOUNT_TO: LocalAccount = Account.from_key(os.environ.get("ETH_PRIVATE_TO"))

print("Connecting to RPC")

# Create a web3 object with a standard json rpc provider, such as Infura, Alchemy, or your own node.
w3 = Web3(HTTPProvider("http://localhost:8545"))
w3.middleware_onion.add(construct_sign_and_send_raw_middleware(ETH_ACCOUNT_FROM))

# Flashbots providers require both a standard provider and ETH_ACCOUNT_SIGNATURE (to establish reputation)
flashbot(w3, ETH_ACCOUNT_SIGNATURE)

print(f"From account {ETH_ACCOUNT_FROM.address}: {w3.eth.get_balance(ETH_ACCOUNT_FROM.address)}")
print(f"To account {ETH_ACCOUNT_TO.address}: {w3.eth.get_balance(ETH_ACCOUNT_TO.address)}")

# Setting up an transaction with 1 in gasPrice where we are trying to send
print("Sending request")
params: TxParams = {
    "from": ETH_ACCOUNT_FROM.address,
    "to": ETH_ACCOUNT_TO.address,
    "value": w3.toWei("1.0", "gwei"),
    "gasPrice": w3.toWei("1.0", "gwei"),
    "nonce": w3.eth.get_transaction_count(ETH_ACCOUNT_FROM.address),
}

try:
    tx = w3.eth.send_transaction(
        params,
    )
    print("Request sent! Waiting for receipt")
except ValueError as e:
    # Skipping if TX already is added and pending
    if "replacement transaction underpriced" in e.args[0]["message"]:
        print("Have TX in pool we can use for the example")
    else:
        raise


print("Setting up flashbots request")
nonce = w3.eth.get_transaction_count(ETH_ACCOUNT_FROM.address)
bribe = w3.toWei("0.01", "ether")

signed_tx: SignTx = {
    "to": ETH_ACCOUNT_TO.address,
    "value": bribe,
    "nonce": nonce + 1,
    "gasPrice": 0,
    "gas": 25000,
}

signed_transaction = ETH_ACCOUNT_TO.sign_transaction(signed_tx)

bundle = [
    #  some transaction
    {
        "signer": ETH_ACCOUNT_FROM,
        "transaction": {
            "to": ETH_ACCOUNT_TO.address,
            "value": Wei(123),
            "nonce": nonce,
            "gasPrice": 0,
        },
    },
    # the bribe
    {
        "signed_transaction": signed_transaction.rawTransaction,
    },
]

block = w3.eth.block_number

result = w3.flashbots.send_bundle(bundle, target_block_number=w3.eth.blockNumber + 3)
result.wait()
receipts = result.receipts()
block_number = receipts[0].blockNumber

# the miner has received the amount expected
bal_before = w3.eth.get_balance(ETH_ACCOUNT_FROM.address, block_number - 1)
bal_after = w3.eth.get_balance(ETH_ACCOUNT_FROM.address, block_number)
profit = bal_after - bal_before - w3.toWei("2", "ether")  # sub block reward
print("Balance before", bal_before)
print("Balance after", bal_after)
assert profit == bribe

# the tx is successful
print(w3.eth.get_balance(ETH_ACCOUNT_TO.address))
