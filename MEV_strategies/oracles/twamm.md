## twamm designs

<br>

### tl; dr


<br>


* time weighted amm designs prevent sandwich attacks by executing transactions lazily.
* orders are executed as if they were placed between blocks. this way, an attacker would need to straddle blocks in order to take advantage of the victim's slippage tolernace (which is riskier than simply including txs around the victim's).



<br>

---


### resources


<br>

* [twamm, by paradigm](https://www.paradigm.xyz/2021/07/twamm)
* [twamm ref implementation](https://github.com/para-dave/twamm)
* [some properties of twamm](https://github.com/pcaversaccio/reentrancy-attacks)

