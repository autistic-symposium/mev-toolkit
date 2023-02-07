## liquidations

<br>

### tl, dr

* lending protocol (e.g. aave or maker) liquidations present a well-known MEV opportunity. they work by requiring users to deposit some collateral. users can then borrow different assets and tokens from others depending on what they need, up to a certain amount of their deposited collateral. 
* as the value of a borrower's collateral fluctuates, if the value of the borrowed assets exceeds the value of the collateral, the protcol allows anyone to liquidate the collateral (similar to margin calls in traditional finance). 
* searchers compete to parse blockchain data as fast as possible to determine which borrowers can be liquidated and be the first to submit a liquidation transaction and collect the liquidation fee.
* example of strategy: bot detects a liquidation opportuniy at a block and issues a liquidation tx, which is expected to be include in the next block. to compete with other liquidators, the bot sets high tx fees for their liquidation tx.
* another strategy: bot observes a tx which will create a liquidation opportunity (e.g., an oracle price update tx rendering a collaterized debit to be liquidated), then backruns this tx with a liquidation tx to avoid the fee bidding competition.


<br>

---

## resources

* [anatomy of liquidator bots](https://github.com/go-outside-labs/mev-toolkit/blob/main/anatomy_of_mev_bots/bots/liquidators.md)
* [liquidation dashboard, by eigenphi](https://eigenphi.io/mev/ethereum/liquidation)
* [understanding compound's liquidation, by zengo](https://zengo.com/understanding-compounds-liquidation/)
* [nahtan worsley's liquidation strategies, by forbes](https://www.forbes.com/sites/jeffkauflin/2022/10/11/the-secretive-world-of-mev-where-crypto-bots-scalp-investors-for-big-profits/?sh=25489eda2d8d) 
