## Notes on Sandwich trading

* To sandwich, a searcher will watch the mempool for large DEX trades.
* A searcher can calculate the approximate price effect of this large trade and execute an optimal buy order immediately before the large trade, then executing a sell order immediately after the large trade (selling it for the igher price caused by the large order).
* Sandwiching is riskier as it isn't atomic an it's prone to [salmonella attack](https://github.co/Defi-Cartel/salmonella)
