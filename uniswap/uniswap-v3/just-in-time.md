## just-in-time (jit) liquidity mev

<br>

### tl; dr

* uniswap v3 allows LPs to provide concentrated liquidity within smaller price ranges. 
* jit liquidity is a form of liquidity provision where an LP mints and burns a concentrated position immediately before and after a swap.
* because provision has significant costs, it's usually only used against very large swaps
* jit lps face competition in mev auction market - the price improvement provided by jit liquidity should be capped by twice the fee rate of the pool that jit occurs in.
* sophisticated searchers can add and remove concentrated liquidity on sandwich trades. 

<br>

----

### impermanent loss (il)

* uniswap lps profit a fixed trading fee associated with each liquidity pool, typically 0.01%, 0.05%, or 0.3% of the value of each swap
* when the price of the two assets begins to diverge, lps experience il associated with that divergence, as lps are continuously selling the appreciating asset of the pair for more of the depreciating asset.
* lps are in profit overall if the trading fees outweigh the il they are subject (either v2 or v3)
* in uniswap v3, lps may capture more tradng fees whenever their liquidity is in range, however, if the price moves permanently out of the range of their liquidity, their il aggravates. 
* additionally, uniswap v3 comes with just-in-time (jit) liquidity, which reduces the fee accrual of normal lp.


<br>

----

### resources

* [uniswap's jit liquidity](https://uniswap.org/blog/jit-liquidity)
