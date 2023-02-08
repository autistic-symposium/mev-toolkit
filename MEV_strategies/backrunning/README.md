## backrunning (tailgating)

<br>


### tl; dr

<br>

* backrunners predict trade opportunities that will be included into a future block based on the outcome of another user's trade, so that their tx is ordered immediately after some unconfirmed 'target tx'.
* a typical backrunner will send many identical txs, with gas price identical to that of the target tx, sometimes from different accounts, in order to increase the chances that one of their txs is ordered after the target but before any competitor (snipping).
* example of strategy: a buy tx immediately behind the initial liquidity. the bot swoops in and buys as many tokens as possible and waits for the price to go up and other traders buy the token from uniswap and proceeds to sell back the tokens at a higher price.

<br>

---

### resources

<br>

* [anatomy of backrunner bots](https://github.com/go-outside-labs/mev-toolkit/blob/main/anatomy_of_mev_bots/bots/backrunners.md)
* [intro to backrunning on ethereum](https://www.youtube.com/watch?v=ApAJ1afUbBI)
* [dune for Portion of Daily Gas Used by Backrunning Bot Contracts](https://dune.com/phabc/backrunning-bots-gas-consumption)
* [backrunning study for bZx IDO](https://amanusk.medium.com/the-fastest-draw-on-the-blockchain-bzrx-example-6bd19fabdbe1)
* [ef discussion on random ordering of equally-priced txs](https://github.com/ethereum/go-ethereum/issues/21350)

