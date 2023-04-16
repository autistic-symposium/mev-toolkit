## flashbots

<br>

### tl;dr

<br>

* **flashbots** is a research and development organization focused on mitigating the negative externalities of current MEV extraction techniques.
* after the release of MEV-geth (and later MEV-boost), much of the computation related to MEV was taken off-chain, by a side-relay that allows MEV searchers to communicate directly with nodes and other participants. This lead to a decrease in fee congestion pricing.
* however, MEV “marketplaces” like flashbots, are quite centralized, since the vast majority of blocks flow through it.

<br>

##### bundles

* bundle/transaction profitability is determined by: fee per gas used, priority fee, and direct validator payments.


<br>

----

### in this dir

<br>


* [mev-boost](mev-boost)
* [suave](suave)
* [scripts](scripts)
* [tools](tools)




<br>

---

### resources

<br>

- [how to use flashbots](https://cryptomarketpool.com/how-to-use-flashbots/)
- [bundle pricing docs](https://docs.flashbots.net/flashbots-auction/searchers/advanced/bundle-pricing)
- [flashbots bundler explorer](https://flashbots-explorer.marto.lol/)
- [flashbots: frontrunning the mev crisis by thegostep](https://ethresear.ch/t/flashbots-frontrunning-the-mev-crisis/8251)
- [order flows kingmaker of block builders by noxx](https://noxx.substack.com/p/order-flows-kingmaker-of-the-block)
- [data analysis of Flashbots MEV](https://github.com/ivanmolto/mev-flashbots-unleashed)
- [flashbots' transparency board](https://transparency.flashbots.net/)
- [flashbots' research topics](https://github.com/flashbots/mev-research)
- [mev economics](https://www.youtube.com/playlist?list=PLXzKMXK2aHh7bW0j2dhpnLNiIJIMnPgsD)


