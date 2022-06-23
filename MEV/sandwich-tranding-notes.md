## Sandwich trading

<br>

* Sandwiching is a common situation that occurs when a searcher identifies a large trade in the mempool that will cause an impact on the price of an asset. The searcher buys or sells a calculated amount directly prior to the large trade being executed and then immediately exits their position after the large order has taken place, banking a nice profit.
* The main theme of sandwich attacks is slippage caused by available liquidity in the pool. As users, ensuring the slippage setting is within appropriate risk limit reduce the risk of large MEVs.
* To sandwich, a searcher will watch the mempool for large DEX trades.
* A searcher can calculate the approximate price effect of this large trade and execute an optimal buy order immediately before the large trade, then executing a sell order immediately after the large trade (selling it for the igher price caused by the large order).
* Sandwiching is riskier as it isn't atomic an it's prone to [salmonella attack](https://github.co/Defi-Cartel/salmonella)


<br>

---

### How to recognize cross-trading arbitrage like sandwich

<br>

A sandwich arbitrage has characters as below:
- In the same block, the attacker's transactions contain a start transaction, an end transaction, and one or more victim transactions in between.
- the combination of attacker and victim needs to satisfy an essential condition: the from address is not the same.


The CombinedTransferTable of each transaction contains the same Address processing the Trade. Combining the Attacker's Start Transaction and End Transaction give the CombinedTransferTable of this arbitrage having the final net surplus.

Signal for Arbritage recognition: all three transactions had Trade happened on Address: Uniswap V2.

<br>

---

### Examples in the wild

<br>


* https://etherscan.io/tx/0x90f2f133fcfe8e1870b69323ea0b46193b9443a701b4cef81a14c727a1df648f
* A MEV bot sandwich attacked this user https://etherscan.io/tx/0xa79dfb5d4442a4ff04768c638bf306b75340ac325e86c34653904ab7f7429ac5
* The bot spent $18,583.13, to make $19,182.43, https://etherscan.io/tx/0x206203f5d62b8027fc8ad0c88be2b6d7b8e9c6b5b81a49c9a8d1c227d6027018
