## ⚡️🤖🧱⛓ [scratch space] Stateful Blockchains, MEV, and Flashbots

<br>

### *"Maximal (formerly "miner" in the context of Proof of Work) extractable value (MEV) refers to the maximum value that can be extracted from block production in excess of the standard block reward and gas fees by censoring and/or changing the order of transactions in a block."* - MEV Wiki

<br>
<br>


---

## My notes

<br>

* [Chapter I: `geth` and running an Ethereum node](https://github.com/bt3gl-labs/Getting-Started-MEVs-and-Flashbots/blob/main/chapter_I.md)
* [Chapter II: The Mempool and MEV](https://github.com/bt3gl-labs/Getting-Started-MEVs-and-Flashbots/blob/main/chapter_II.md)
* [Chapter III: Flashbots](https://github.com/bt3gl-labs/Getting-Started-MEVs-and-Flashbots/blob/main/chapter_III.md)
* [Chapter IV: Flashbots bundle](https://github.com/bt3gl-labs/Stateful-Blockchains-and-Flashbots/blob/main/chapter_IV.md)

<br>
<br>

---

## My code

<br>

* [PoCs having `geth` in Docker and K8s](https://github.com/bt3gl-labs/Stateful-Blockchains-and-Flashbots/tree/main/geth_and_k8s)


<br>
<br>

---

## Further resources

<br>

- [Flashbots](https://github.com/flashbots/pm) maintains a proof-of-concept communication channel for users to send their Ethereum transactions directly to miners.
- [MEV wiki](https://www.mev.wiki/)
- [Etherscan data on flashbots](https://etherscan.io/blocks/label/flashbots)
- [MEV Dashboard by Flashbots](https://explore.flashbots.net/).
- [Sandwiched?](https://sandwiched.wtf/)

<br>
<br>

---

## Some terminology

<br>

* **Mempool**: the set of pending, unconfirmed transactions in the EVM.
* **MEV**: Maximal (or miner) Extractable Value
* **Frontrunning**: also known as Priority Gas Auctions (PGAs), when a miner steals a profitable opportunity (such as arbitrage) for themselves by sending the same transaction with a higher gas price. For example, a transaction A is broadcasted with a higher gas price than an already pending transaction B so that A gets mined before B (eg. to snatch a Uniswap price arbitrage trade to rebalance a pool).
* **Backrunning**: a transaction A is broadcasted with a slightly lower gas price than already pending transaction B so that A gets mined right after B in the same block. (eg. to execute a DyDx liquidation after a price oracle update that triggers a DyDx loan to go under the required collateralization ratio).
* **Sandwiching**: profiting off slippage in liquidity pools by buying and selling before and after large transactions posted in the mempool.
* **DEX arbitrage**: If two DEXes are offering a token at two different prices, one can buy the token on the lower-priced DEX and sell it on the higher-priced DEX.
* **Liquidations**: if the value of a borrowed asset exceeds the collateral, anyone can liquidate the collateral and collect the liquidation fee for themselves.

<br><br>
