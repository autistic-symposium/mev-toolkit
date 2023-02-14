## just-in-time (jit) liquidity 

<br>

### tl; dr

<br>

* **uniswap v3** comes with just-in-time (jit) liquidity, allowing LPs to provide concentrated liquidity within smaller price ranges, i.e., to specify a range of prices their liquidity is active for. this allows capital efficiency for correlated tokens.

* the **liquidity range** determines the share of fees. however, the tighter the tick range, the greater the risk of impermanence loss (the greater the likelihood that the price of the asset pair will move out of the tick range to volatility), which would generate no fees).

* a **strategy** is to scan the mempool for substantial pending trades, provide liquidity where a LP mints and burns a concentrated position immediately before and after a swap. no impermanent loss happens because everything happens within the same block.

* because provision has **high costs**, it's usually only used against very large swaps (i.e., it's a non-atomic strategy).

* [*"their strategies mainly allocate liquidity in a narrow range and adjust the tick intervals to track market price based on quantitative indicators such as bollinger bands"*](https://mirror.xyz/0xc19565163aFdEe3783FC970E4Bd0275B11848d34/wr9JWZ_MIroWnXeze_tXG1R7nSsoTkp7IvqK5BsWYhA)


<br>

### in this dir

<br>

* [tricks](tricks)

<br>

----

<br>

### links

<br>

* [uniswap on jit liquidity](https://uniswap.org/blog/jit-liquidity)
* [just-in-time mev dune board](https://dune.com/ChainsightAnalytics/Uniswap-v3-Just-in-Time-(JIT)-Liquidity-MEV)
* [uniswap v3 lp by rekt](https://rekt.news/uniswap-v3-lp-rekt/)
