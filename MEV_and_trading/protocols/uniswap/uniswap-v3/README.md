## uniswap v3

<br>

### tl; dr

<br> 

- uniswap v3 introduced: 

  * **concentrated liquidity** and **non-fungible liquidity**: 
    * replacing fungible ERC20 liquidity positions with non-fungible ERC-721 liquidity positions. 
    * individual LPs get granular control over what price ranges their capital is allocated to. 
    * individual positions are aggregated together into a single pool, forming one combined curve for users to trade against.
  * **multiple fee tiers**: allowing LPs to be appropriately compensated for taking on varying degrees of risk. 
  * **range orders**: lps can deposit a single token in a custom price range, above or below the current price.
  * **improvements to the TWAP oracle**: possible to calculate any recent TWAP within ~9 days in a single on-call chain.

- new strategies:
  * creating and closing LP positions can be a form of trading. range orders can be used as either buy-limit or take-profit orders. 


<br>

---

### in this dir

<br>

* [just in time liquidity mev](just-in-time.md)

<br>

---

### resources

<br>

* [uniswap v3 whitepaper](https://uniswap.org/whitepaper-v3.pdf)
* [liquidity mining on uniswap v3, by paradigm](https://www.paradigm.xyz/2021/05/liquidity-mining-on-uniswap-v3)
* [uniswap v3 book, by jeiwan](https://github.com/Jeiwan/uniswapv3-book)
* [jit liquidity by chainsight](https://twitter.com/ChainsightLabs/status/1457958811243778052)
* [conceptualizing uniswap v3 lp profit and loss](https://atise.medium.com/conceptualizing-uniswap-v3-lp-profit-and-loss-ecbae6e09644)
* [on why lp-ing on uniswap is a losing game](https://twitter.com/thiccythot_/status/1589022227437039616)
* [usage of markout to calculate LP profitability in uniswap v3, by crocswap](https://crocswap.medium.com/usage-of-markout-to-calculate-lp-profitability-in-uniswap-v3-e32773b1a88e)
* [ETH USDC retroactive data Aaalysis, by flipside](https://science.flipsidecrypto.xyz/ethusdc_results/eth_usdc_analysis.html)
* [markouts and stat analysis in uniswap v3](https://github.com/go-outside-labs/mev-toolkit/blob/main/MEV_strategies/stat_arbs/README.md)
