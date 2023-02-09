##  private order flows 

<br>

<img width="802" src="https://user-images.githubusercontent.com/1130416/217937850-9b7e9434-ee72-4c2a-9e5e-ae9fe795310e.png">



<br>

### rpc-based "payment for order flow protocols" (POFPs)

<br>

* this type of private order flows can be realized by modifying either the user's rpc or by modifying the protocol's frontend
* the rpc endpoint re-broadcasts (forwarding) the tx to nodes. 
* in respect to every pending tx they receive, they can: 1) censor, 2) forward to some mempool, or 3) forward it directly to some block-builders or validators.

<br>

--- 

### validator transaction reordering protocols (VTRPs)

<br>

* private tx reordering
* two goals: 1) identify valuable user txs, 2) replace the POFP's value-extracted tx with its own value-extractive tx
* when a VTRP is able to identify a valuable user tx but, due to the tactics of the POFP, is unable to inject its own transaction in place of the POFP's -> VTRP's optimal strategy is to censor the user's transaction from the final block

<br>

---



### stat arbs

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

#### resources

<br>


* [private order flow and the block builder market, by jon charbonneau](https://twitter.com/jon_charb/status/1562916372505665536)
* [ethereum's biggest issue no one's talking about](https://mariusvanderwijden.github.io/blog/2022/10/21/lightclients/)
* [private order flow is the new MEV (youtube)](https://www.youtube.com/watch?v=bapIqxhIdaY)
* [kolibrio](https://www.kolibr.io/) (and [docs](https://docs.kolibr.io/))
