#!/usr/bin/env python3 
# This script sends a bundle of two transactions which transfer ETH into a random account.
# For full instructions: https://lilithsecurity.substack.com/p/-mev-wednesdays-intro-to-flashbots


import os
import secrets
from pathlib import Path
from dotenv import load_dotenv
from flashbots import flashbot
from eth_account.account import Account
from eth_account.signers.local import LocalAccount
from web3 import Web3, HTTPProvider
from web3.exceptions import TransactionNotFound
from web3.types import TxParams


def env(key: str) -> str:
    load_dotenv(Path('.') / '.env')
    return os.getenv(key)


def random_account() -> LocalAccount:
    key = "0x" + secrets.token_hex(32)
    return Account.from_key(key)


def main():

    SENDER_KEY = env("SENDER_KEY")
    SIGNER_KEY = env("SIGNER_KEY")
    PROVIDER_URL = env("PROVIDER_URL")
    CHAIN_ID =  int(env("CHAIN_ID"))

    # 1. account to send the transfer and sign transactions
    sender: LocalAccount = Account.from_key(SENDER_KEY)

    # 2. account to receive the transfer
    receiverAddress: str = random_account().address

    # 3. account to sign bundles and flashbots reputation
    signer: LocalAccount = Account.from_key(SIGNER_KEY)
    w3 = Web3(HTTPProvider(PROVIDER_URL))
    flashbot(w3, signer, "https://relay-goerli.flashbots.net")

    print(f"✅ Sender address: {sender.address}")
    print(f"✅ Receiver address: {receiverAddress}")
    print(f"✅ Sender account balance: {Web3.fromWei(w3.eth.get_balance(sender.address), 'ether')} ETH")
    print(f"✅ Receiver account balance: {Web3.fromWei(w3.eth.get_balance(receiverAddress), 'ether')} ETH")

    # 4. bundle two EIP-1559
    nonce = w3.eth.get_transaction_count(sender.address)
    tx1: TxParams = {
        "to": receiverAddress,
        "value": Web3.toWei(0.005, "ether"),
        "gas": 21000,
        "maxFeePerGas": Web3.toWei(300, "gwei"),
        "maxPriorityFeePerGas": Web3.toWei(50, "gwei"),
        "nonce": nonce,
        "chainId": CHAIN_ID,
        "type": 2,
    }
    tx1_signed = sender.sign_transaction(tx1)

    tx2: TxParams = {
        "to": receiverAddress,
        "value": Web3.toWei(0.005, "ether"),
        "gas": 21000,
        "maxFeePerGas": Web3.toWei(300, "gwei"),
        "maxPriorityFeePerGas": Web3.toWei(50, "gwei"),
        "nonce": nonce + 1,
        "chainId": CHAIN_ID,
        "type": 2,
    }

    bundle = [
        {"signed_transaction": tx1_signed.rawTransaction},
        {"signer": sender, "transaction": tx2},
    ]

    # 5. Send bundle until it gets mined
    while True:
        block = w3.eth.block_number
        print(f"✨ Simulating on block {block}...")

        try:
            w3.flashbots.simulate(bundle, block)
            print("✅ Simulation successful!")
    
        except Exception as e:
            print(f"🚨 Simulation error: {e}")
            return

        print(f"Sending bundle targeting next block: {block+1}...")
        send_result = w3.flashbots.send_bundle(bundle, target_block_number=block + 1)
        send_result.wait()

        try:
            receipts = send_result.receipts()
            print(f"\n✅ Bundle was mined in block {receipts[0].blockNumber}\a")
            break

        except Exception as e:
            print(f"Bundle not found in block {block+1}: {e}")

    print(f"✅ Sender account balance: {Web3.fromWei(w3.eth.get_balance(sender.address), 'ether')} ETH")
    print(f"✅ Receiver account balance: {Web3.fromWei(w3.eth.get_balance(receiverAddress), 'ether')} ETH")


if __name__ == "__main__":
    main()
