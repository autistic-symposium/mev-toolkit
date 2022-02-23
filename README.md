# Stateful Blockchains, MEV, and Flashbots

* This repository contains my notes, scripts, code through my journey into stateful blockchains and miner profit.


* **[Flashbots](https://github.com/flashbots/pm)** maintains a proof-of-concept communication channel for users to send their Ethereum transactions directly to miners. It was created as part of Flashbots' goal to mitigate the negative externalities and existential risks posed by MEV to smart-contract blockchains.

---

## Episodes

* [Chapter I: `geth` and running an Ethereum node](https://github.com/bt3gl-labs/Getting-Started-MEVs-and-Flashbots/blob/main/chapter_I.md)
* [Chapter II: The Mem Pool and MEV](https://github.com/bt3gl-labs/Getting-Started-MEVs-and-Flashbots/blob/main/chapter_II.md)
* [Chapter III: Flashbots](https://github.com/bt3gl-labs/Getting-Started-MEVs-and-Flashbots/blob/main/chapter_III.md)
* [Chapter IV: Flashbots bundle](https://github.com/bt3gl-labs/Stateful-Blockchains-and-Flashbots/blob/main/chapter_IV.md)


---

## Further references


- [Flashbots PM](https://github.com/flashbots/pm)
- [Etherscan data on flashbots](https://etherscan.io/blocks/label/flashbots)

---

## Terminology

* MEV: Maximal (or miner) Extractable Value
* Front-running: when a miner steals a profitable opportunity (such as arbitrage) for themselves by sending the same transaction with a higher gas price.
* Sandwiching: profiting off slippage in liquidity pools by buying and selling before and after large transactions posted in the mempool.
* DEX arbitrage: If two DEXes are offering a token at two different prices, one can buy the token on the lower-priced DEX and sell it on the higher-priced DEX.
* Liquidations: if the value of a borrowed asset exceeds the collateral, anyone can liquidate the collateral and collect the liquidation fee for themselves.
