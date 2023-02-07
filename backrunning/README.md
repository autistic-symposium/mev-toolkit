## 🥪 backrunning (tailgating)

<br>


### tl; dr

* backrunners predict trade opportunities that will mine into a future block based on the outcome of another user's trade.
* it occurs when a transaction sender wishes to have their tx ordered immediately after some unconfirmed 'target tx'.
* a typical backrunner will send many identical txs, with gas price identical to that of the target tx, sometimes from different accounts, in order to increase the chances that one of their txs is ordered after the target but before any competitor (snipping).

<br>

---

### strategy

<br>

* a backrunning bot that back-runs new token listings.
* it monitors the mempool for new pairs being created on uniswap, if it finds a new pair the bot places a buy transaction imediately behind the initial liquidity.
* the bot swoops in and buys as many tokens as possible (but not all them as there needs to be an opportunity for others to buy tokens)
* the bot waits for the price to go up and other traders buy the token from uniswap and proceeds to sell back the tokens at a higher price
* the key strategy is to be the first to buy tokens, but only after it has been launched.

<br>

---

### resources

<br>

* [intro to backrunning on ethereum](https://www.youtube.com/watch?v=ApAJ1afUbBI)
* [dune for Portion of Daily Gas Used by Backrunning Bot Contracts](https://dune.com/phabc/backrunning-bots-gas-consumption)
* [backrunning study for bZx IDO](https://amanusk.medium.com/the-fastest-draw-on-the-blockchain-bzrx-example-6bd19fabdbe1)
* [ef discussion on random ordering of equally-priced txs](https://github.com/ethereum/go-ethereum/issues/21350)

