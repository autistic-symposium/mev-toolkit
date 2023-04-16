## balancer

<br>

### tl; dr

* liquidity infrastructure

<br>

---


### composable stable pools

* contribute more than $640M to balancer's tvl
* one of the many technical components of balancer's flexible amm framework and essential for token like stables or lsds
* these pools are designed for assets that are either expected to consistently trade at near parity, or at a known exchange rate
* pools use stable math, based on stableswap (populatized by curve finance)
* reinforced by balancer's nested pool v2 infrastructure, metastable pools have a myriad of benefits compared to a standard pool 2: correlated token liquidity utilization, reduced liquidity fragmentation of like-assets, capital efficiency.
* use cases include: bb-g-USD, wstETH, and bb-i-USD.
* protocols like gearbox, lido, and idle continue to expand on the capabilities of metastable pools.
* best assets are either pegged or correlated (e.g rETH and boosted pools like bb-g-USD).
* token swaps can occur between any and all nested pools within balancer (e.g. aave boosted pools and rocket pool lsd eth).
* each pool has a function known as a rate provider that updates tokens to the correct ratio any time a trade takes place. this function means that liquid staked yield flows to liquidity providers rather than arbers.

<br>

---

## resources
