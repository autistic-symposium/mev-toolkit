## 🧀 liquidations

<br>

### tl, dr

* Lending protocol (e.g. Aave or Maker) liquidations present a well-known MEV opportunity.

* They work by requiring users to deposit some collateral. Users can then borrow different assets and toekns from others depending on what they need, up to a certain amount of their deposited collateral.

* As the value of a borrower's collateral fluctuates, if the value of the borrowed assets exceeds the value of the collateral, the protcol allows anyone to liquidate the collateral (similar to margin calls in traditional finance).

* If liquidated, the borrower usually has to pay a hefty liquidation fee, some of which goes to the liquidator (where the MEV opportunity comes in).

* Searchers compete to parse blockchain data as fast as possible to determine which borrowers can be liquidated and be the first to submit a liquidation transaction and collect the liquidation fee.

<br>

### strategy 1

* A detects a liquidation opportuniy at block B (after the execution of B). Then, A issues a liquidation transaction T, which is expected to be mined in the next block, B+1.
* A attempts to destructively front-run other competing liquidators by setting high transactions fees for their liquidation transaction T.

<br>

### strategy 2

* A observes a transaction T, which will create a liquidation opportunity (e.g., an oracle price update transaction which will render a collaterized debit liquidatable). A then back-runs T with a liquidation transaction Ti to avoid the transation fee bidding competition.


<br>

---

## resources

* [understanding compound's liquidation](https://zengo.com/understanding-compounds-liquidation/)
