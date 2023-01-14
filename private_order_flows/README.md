## MEV private order flows solutions


#### private order flow protocols (POFPs)

* rpc-based mev solutions (private order flow) 
* private orderflows are realized by modifying either the user's rpc or by modifying the protocol's frontend
* the goal of private order flow protocols (POFPs)

<br>

--- 

### validator transaction reordering protocols (VTRPs)

* private tx reordering
* two goals: 1) identify valuable user txs, 2) replace the POFP's value-extracted tx with its own value-extractive tx
* when a VTRP is able to identify a valuable user tx but, due to the tactics of the POFP, is unable to inject its own transaction in place of the POFP's -> VTRP's optimal strategy is to censor the user's transaction from the final block


---

<br>

### stat arbs

* if CEX is greater than the price on chain (on theDEX), stat arbs will buy on the DEX and hedge on the CEX -> confident that the DEX price will drift towards the CEX price, but not confident that will happen to the CEX price
* problem: settlement mismatch -> CEX trades are fast but blockchains aren't -> start arbs are unsure if the trade will land or competitors will beat them
* from the time between trade submission and receipt of the next block, the trade (their exposure to the assets) is uncertain 
* the greater the uncertainty, the more the profit estimate needs to be marked down
* while volatility of the token is important, the longer the time period between blocks, the longer tx remains, and the longer can go without being fully hedged
* as block time increases, stat arb MEV profit estimates get marked down -> payments made by stat arbers to miners/validators or to users/traders decrease
* conclusion: the battle between PFOF-style MEV could lead to increase block times for stat arbers, decreasing combined realzied MEV

<br>

---

#### resources

* [Ethereum's biggest issue no one's talking about](https://mariusvanderwijden.github.io/blog/2022/10/21/lightclients/)
* [Youtube: Private Order Flow is the new MEV](https://www.youtube.com/watch?v=bapIqxhIdaY)
