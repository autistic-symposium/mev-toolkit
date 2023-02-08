## gmx oracle abuse


<br>

### tl; dr

<br>

* gmx has not price impact (large order trades at mark price). 
* when high volatility, there is a spread from the chainlink price to the median price of reference exchanges.


<br>

### tl; dr october'22 event

<br>

* dynamic price: gmx differs from amms by offering zero slippage on trades via an oracle price update system (via chainlink and aggregate of prices from leading volume exchanges), while amms like uniswap rely on arb bots to balance prices in the pools. 
* gmx team-run bots make calls to `SetPriceWithBit()` to update asset prices. mev operators can observe these prices updates in the mempool before land on chain.

<br>

---

### resources

<br>

* [chainsight twitter](https://twitter.com/ChainsightLabs/status/1580208615654584321?s=20&t=-FG5kQ_7kAKhLnbuk05wSg)
