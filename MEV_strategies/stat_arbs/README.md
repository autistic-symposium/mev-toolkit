## statistical strategies (signal-based)

<br>

### tl; dr

<br>


* **statistical mev** (non-atomic) convey informed strategies that rely on off-chain information (signal). 

* examples can be strategies that rely on:
   - [cross-chains](https://github.com/go-outside-labs/mev-toolkit/tree/main/MEV_searchers/cross_domain_mev) arbitrage
   - [CEX + DEX arbitrage](https://github.com/go-outside-labs/searcher-coingator-rs)
   - [order flow](https://github.com/go-outside-labs/mev-toolkit/tree/main/MEV_searchers/private_order_flows) trading by aggregating orders from multiple private or public mempools
   - [whale watching](https://github.com/go-outside-labs/mev-toolkit/tree/main/MEV_and_trading/whales) 

* these strategies are more profitable and less accessible due to capital requirements and risk profile.



<br>

----

### in this dir

<br>


* [routers and aggregators](aggregators)
* [convex optimization](convex_optimization)



<br>

---

### links

<br>

* [anatomy of stat bots](https://github.com/go-outside-labs/mev-toolkit/blob/main/MEV_searchers/bots/stat-arbers.md)
* [`addLiquidity()` sandwich attack optimization problem](https://mirror.xyz/0xc19565163aFdEe3783FC970E4Bd0275B11848d34/oTdSfZEBdp9WPCNaKqDKCkuDJ9neR2UISc_5mMjZKYU)
* [dex arbitrage, mathematical optimizations & me, by noxx](https://noxx.substack.com/p/dex-arbitrage-mathematical-optimisations)
* [a new game in town, by frontier research](https://frontier.tech/a-new-game-in-town)
