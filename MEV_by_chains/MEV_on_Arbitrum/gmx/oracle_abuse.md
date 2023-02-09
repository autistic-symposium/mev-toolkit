## gmx oracle abuse


<br>

### tl; dr

<br>


* october'22 oracle abuse: dynamic price: gmx differs from amms by offering zero slippage on trades via an oracle price update system (via chainlink and aggregate of prices from leading volume exchanges), while amms like uniswap rely on arb bots to balance prices in the pools. gmx team-run bots make calls to `SetPriceWithBit()` to update asset prices. mev operators can observe these prices updates in the mempool before land on chain.
* a new oracle oracle has been deployed (XGET), which allows for information to be verified on-chain while providing frontrunning resistance (by having nodes sign a combination of blockhashes and values).


<br>

### tl; dr 

<br>



<br>

---

### resources

<br>

* [chainsight twitter](https://twitter.com/ChainsightLabs/status/1580208615654584321?s=20&t=-FG5kQ_7kAKhLnbuk05wSg)
* [another twitter](https://twitter.com/wilburforce_/status/1571891338097860608)
