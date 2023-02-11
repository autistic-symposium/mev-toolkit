## PvP bot battles

<br>

### cool stories

<br>

#### salmonella

* exploited the generalised nature of front-running setups through an erc20 token that could detect when a non-owner is transacting it, returning just 10% of the amount.
* [source code](https://github.com/Defi-Cartel/salmonella)

<br>

#### kattana

* trap for front-running bots during token listing.

<br>

#### YOLOchain

* [bert miller thread](https://twitter.com/bertcmiller/status/1381296074086830091?s=20)
  * instead of users paying tx fees via gas prices, flashbots users pay fees via a smart contract call which transfers eth to miner.
  * miners receive bundles of txs from users and include the bundle that pays the most
  * sandwich bots watch the mempool for users buying on dexes and sandwich them
  * bots will simulate their txs on local infrastrcuture

<br>

#### other stories of hacked MEV bot  


* [https://twitter.com/AnciliaInc/status/1580705036400611328](https://twitter.com/AnciliaInc/status/1580705036400611328)
* [https://twitter.com/BlockSecTeam/status/1580779311862190080](https://twitter.com/BlockSecTeam/status/1580779311862190080)
* [https://twitter.com/MevRefund/status/1537421091697836032](https://twitter.com/MevRefund/status/1537421091697836032)
* [https://twitter.com/MevRefund/status/1580652170592280576](https://twitter.com/MevRefund/status/1580652170592280576)
* [a list of malicious tokens](malicious_tokens.md)[https://github.com/kailinr/cyanide]

<br>


----


### resources

<br>

* [disassembling mev bots, by noxx](https://noxx.substack.com/p/mev-memoirs-into-the-arena-chapter-3e9)
* [toxic tokens contracts (salmonella derivatives)
