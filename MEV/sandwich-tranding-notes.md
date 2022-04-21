## Notes on Sandwich trading

* Sandwiching is a common situation that occurs when a searcher identifies a large trade in the mempool that will cause an impact on the price of an asset. The searcher buys or sells a calculated amount directly prior to the large trade being executed and then immediately exits their position after the large order has taken place, banking a nice profit.
* The main theme of sandwich attacks is slippage caused by available liquidity in the pool. As users, ensuring the slippage setting is within appropriate risk limit reduce the risk of large MEVs.
* To sandwich, a searcher will watch the mempool for large DEX trades.
* A searcher can calculate the approximate price effect of this large trade and execute an optimal buy order immediately before the large trade, then executing a sell order immediately after the large trade (selling it for the igher price caused by the large order).
* Sandwiching is riskier as it isn't atomic an it's prone to [salmonella attack](https://github.co/Defi-Cartel/salmonella)
