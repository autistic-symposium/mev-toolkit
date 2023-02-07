## 🥪 sandwiching

<br>

### tl, dr

*  predict trade opportunities that will mine into a future block by pushing another user’s trade opportunity to its max slippage limit, which will result in an arbitrage opportunity at a later time (typically within the same block).

* sandwiching is a common situation that occurs when a searcher identifies a large trade in the mempool that will cause an impact on the price of an asset.

* the searcher buys or sells a calculated amount directly prior to the large trade being executed and then immediately exits their position after the large order has taken place, banking a nice profit.

* the main theme of sandwich attacks is slippage caused by available liquidity in the pool. As users, ensuring the slippage setting is within appropriate risk limit reduce the risk of large MEVs.

* to sandwich, a searcher will watch the mempool for large DEX trades.

* a searcher can calculate the approximate price effect of this large trade and execute an optimal buy order immediately before the large trade, then executing a sell order immediately after the large trade (selling it for the igher price caused by the large order).

* sandwiching is riskier as it isn't atomic an it's prone to [salmonella attack](https://github.co/Defi-Cartel/salmonella).

<br>

<img width="700" src="https://user-images.githubusercontent.com/1130416/196341536-47b22f79-404f-4c55-8091-30a7251adcb1.png">



<br>

---

### in this dir

* [interesting txs in the wild](interesting_examples.md)
* [cross-trading arb like sandwich](cross_trading.md)

<br>

---

### resources

* [sandwich attacks on uniswap v2](https://www.defi-sandwi.ch/)
* [sandwich overview, by eigenphi](https://eigenphi.io/mev/ethereum/sandwich)
* [modern mev sandwich attacks on ethereum routers, by totlsota.eth](https://mirror.xyz/totlsota.eth/9JaNkZ1XQfQD6Y79aLYHC_kb_dSBoJ2JYiag5BuGGM8)
* [demystify the dark forest: sandwich attack, by coinmonks](https://medium.com/coinmonks/demystify-the-dark-forest-on-ethereum-sandwich-attacks-5a3aec9fa33e)


