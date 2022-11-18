## PvP bot battles

<br>

### salmonella

* exploited the generalised nature of front-running setups through an erc20 token that could detect when a non-owner is transacting it, returning just 10% of the amount.
* [source code](https://github.com/Defi-Cartel/salmonella)

<br>

### kattana

* trap for front-runnign bots during token listing.

<br>

### YOLOchain

* [bert miller thread](https://twitter.com/bertcmiller/status/1381296074086830091?s=20)
  * instead of users paying tx fees via gas prices, flashbots users pay fees via a smart contract call which transfers eth to miner.
  * miners receive bundles of txs from users and include the bundle that pays the most
  * sandwich bots watch the mempool for users buying on dexes and sandwich them
  * bots will simulate their txs on local infrastrcuture
