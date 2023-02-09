## statistical arbers

<br>

### tl; dr for a strategy

<br>

* if CEX is greater than the price on chain (DEX), stat arbs can buy on the DEX and hedge on the CEX -> confident that the DEX price will drift towards the CEX price, but not confident that will happen to the CEX price
* problem: settlement mismatch -> CEX trades are fast but blockchains aren't -> start arbs are unsure if the trade will land or competitors will beat them
* from the time between trade submission and receipt of the next block, the trade (their exposure to the assets) is uncertain 
* the greater the uncertainty, the more the profit estimate needs to be marked down
* while volatility of the token is important, the longer the time period between blocks, the longer tx remains, and the longer it can go without being fully hedged
* as block time increases, stat arb MEV profit estimates get marked down -> payments made by stat arbers to miners/validators or to users/traders decrease
* conclusion: the battle between PFOF-style MEV could lead to increase block times for stat arbers, decreasing combined realized MEV



<br>

---

### resources

<br>


* [cointegrator bots](https://github.com/go-outside-labs/blockchain-science-py)
