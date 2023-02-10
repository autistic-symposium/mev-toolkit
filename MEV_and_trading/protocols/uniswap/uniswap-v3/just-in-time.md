## just-in-time (jit) liquidity 

<br>

### tl; dr

<br>

* **uniswap v3** comes with just-in-time (jit) liquidity, allowing LPs to provide concentrated liquidity within smaller price ranges, i.e., to specify a range of prices their liquidity is active for. this allows capital efficiency for correlated tokens.
* the **liquidity range** determines the share of fees. however, the tighter the tick range, the greater the risk of impermanence loss (the greater the likelihood that the price of the asset pair will move out of the tick range to volatility), which would generate no fees).
* a **strategy** is to scan the mempool for substantial pending trades, provide liquidity where a LP mints and burns a concentrated position immediately before and after a swap. no impermanent loss happens because everything happens within the same block.
* because provision has **high costs**, it's usually only used against very large swaps (i.e., it's a non-atomic strategy).


<br>

### example cex + dex

<br>

1. consider a JIT LP that has ETH and USDC both in a wallet and in a CEX. 
2. when the LP observes a large ETH -> USDC swap in the mempool, they deploy a LP position on Uniswap, and at the same time submit an ETH buy order on the CEX. 
3. after both trades, the LP has the same total amount of ETH and USDC as before. 
4. assuming that the following holds, the LP are also profitable:

```
    fees_DEX + price_impact_DEX > fees_CEX + price_impact_CEX
```


<br>

----

<br>

### resources

* [uniswap on jit liquidity](https://uniswap.org/blog/jit-liquidity)
* [just-in-time mev dune board](https://dune.com/ChainsightAnalytics/Uniswap-v3-Just-in-Time-(JIT)-Liquidity-MEV)
* [uniswap v3 lp by rekt](https://rekt.news/uniswap-v3-lp-rekt/)
