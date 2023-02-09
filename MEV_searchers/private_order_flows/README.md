##  private order flows 

<br>

### tl; dr

<br>

<img width="759" src="https://user-images.githubusercontent.com/1130416/217937850-9b7e9434-ee72-4c2a-9e5e-ae9fe795310e.png">

<br>

<img width="759"  src="https://user-images.githubusercontent.com/1130416/217938181-3ea5947c-b847-4f4c-a41c-a40addceed8b.png">


<br>

---

### types of private order flows

<br>

#### rpc-based "payment for order flow protocols" (POFPs)

* this type of private order flows can be realized by modifying either the user's rpc or by modifying the protocol's frontend
* the rpc endpoint re-broadcasts (forwarding) the tx to nodes. 
* in respect to every pending tx they receive, they can: 1) censor, 2) forward to some mempool, or 3) forward it directly to some block-builders or validators.

<br>

#### validator transaction reordering protocols (VTRPs)



* private tx reordering
* two goals: 1) identify valuable user txs, 2) replace the POFP's value-extracted tx with its own value-extractive tx
* when a VTRP is able to identify a valuable user tx but, due to the tactics of the POFP, is unable to inject its own transaction in place of the POFP's -> VTRP's optimal strategy is to censor the user's transaction from the final block

<br>

---

### resources

<br>


* [private order flow and the block builder market, by jon charbonneau](https://twitter.com/jon_charb/status/1562916372505665536)
* [ethereum's biggest issue no one's talking about](https://mariusvanderwijden.github.io/blog/2022/10/21/lightclients/)
* [private order flow is the new MEV (youtube)](https://www.youtube.com/watch?v=bapIqxhIdaY)
* [kolibrio](https://www.kolibr.io/) (and [docs](https://docs.kolibr.io/))
