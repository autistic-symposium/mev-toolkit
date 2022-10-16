## 🥪 back-running

<br>

* occurs when a transaction sender wishes to have their tx ordered immediately after some unconfirmed 'target tx'.
* a typical backrunner will send many identical txs, with gas price identical to that of the target tx, sometimes from different accounts, in order to increase the chances that one of their txs is ordered after the target but before any competitor.

<br>


### strategy

<br>

* a back-running bot that back-runs new token listings.
* it monitors the mempoll for new pairs being created on uniswap, if it finds a new pair the both places a buy transaction imediately behind the initial liquidity.
* the bot swoops in and buys as many tokens as possible (but not all them as there needs to be an opportunity for others to buy tokens)
* the bot waits for the price to go up and other traders buy the token from uniswap and proceeds to sell back the tokens at a higher price
* the key strategy is to be the first to buy tokens, but only after it has been launched.
