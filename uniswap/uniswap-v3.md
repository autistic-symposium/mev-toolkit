## 🍣 uniswap v3

<br>

### tl; dr

* Uniswap v3 introduce the concept of "concentrated liquidity", replacing fungible ERC20 liquidity positions with non-fungible ERC-721 liquidity positions.
* better gas refunds due to it's flashloan style architecture.
* the profitability of a liquidity provider (LP) has been called into question: estimations that about half of LPs would have been off holding assets directly rather than providing liquidity


<br>

----

### impermanent loss (il)

* uniswap lps profit a fixed trading fee associated with each liquidity pool, typically 0.01%, 0.05%, or 0.3% of the value of each swap
* when the price of the two assets begins to diverge, lps experience il associated with that divergence, as lps are continuously selling the appreciating asset of the pair for more of the depreciating asset.
* lps are in profit overall if the trading fees outweigh the il they are subject (either v2 or v3)
* in uniswap v3, lps may capture more tradng fees whenever their liquidity is in range, however, if the price moves permanently out of the range of their liquidity, their il aggravates. 
* additionally, uniswap v3 comes with just-in-time (jit) liquidity, which reduces the fee accrual of normal lp.

<br>

---

### resources

* [uniswap v3 whitepaper](https://uniswap.org/whitepaper-v3.pdf)
* [liquidity mining on uniswap v3 by paradigm](https://www.paradigm.xyz/2021/05/liquidity-mining-on-uniswap-v3)
