## 🧀 liquidations

<br>

* Lending protocol (e.g. Aave or Maker) liquidations present a well-known MEV opportunity.
* They work by requiring users to deposit some collateral. Users can then borrow different assets and toekns from others depending on what they need, up to a certain amount of their deposited collateral.
* As the value of a borrower's collateral fluctuates, if the value of the borrowed assets exceeds the value of the collateral, the protcol allows anyone to liquidate the collateral (similar to margin calls in traditional finance).
* If liquidated, the borrower usually has to pay a hefty liquidation fee, some of which goes to the liquidator (where the MEV opportunity comes in).
* Searchers compete to parse blockchain data as fast as possible to determine which borrowers can be liquidated and be the first to submit a liquidation transaction and collect the liquidation fee.
