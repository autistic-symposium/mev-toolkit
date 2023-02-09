## sniping

<br>


### tl; dr

<br>

* **liquidity sniping** happens when searchers compete to purchase an asset immediately after the creation of a liquidity pool. 
* tokens are then not off-loaded in the same block, but instead sold over the next minutes or hours. 
* profits for a sniper are not guaranteed.

<br>

### tricks

<br>

#### cex

* craw relays by requesting through a network of proxies to not get ratelimited (for example, by cloudflare ~5 seconds).
* maintain an in-memory list of endpoints that are predicted to be cached, so only use the ones that are predicted to be uncached.
* [proxymesh: rotating anonynous http proxy servers](https://proxymesh.com/)

<br>

---

### resources

<br>

* [anatomy of snipor bots](https://github.com/go-outside-labs/mev-toolkit/blob/main/MEV_searchers/bots/snipers.md)
* [nft sniping, by avrahan eisenberg 😬](https://deepfivalue.substack.com/p/how-our-team-makes-millions-in-crypto)
