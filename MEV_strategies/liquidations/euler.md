## euler

<br>

### tl; dr

<br>

* protocols with larger amounts of bad debt usually suffer oracle attacks (e.g. mango markets). euler tries to improve existing liquidation mechanism to prevent bad debt.
* euler presents optimizations on liquidations through debt tokens (dTokens) and suply tokens (eTokens), and offering sliding and muliplying discounts to liquidators (dutch auction)
* it calculates health scores using risk-adjusted metrics for collateralized assets, by adjusting them against their market value to a more conservative risk-adjusted one.
* once a user healthy's score has flagged for liquidation, anyone can transfer dTokens and eTokens to their own account, buying both their collateral and debit.
* **soft liquidation**: only enough collateral and debt are transferred under liquidation to return to a healthy score. 
* mev resistance comes from the multipliers euler offers to liquidators with deposits in their account.

<br>

----

### resources

<br>

* [inovative liquidation, by euler](https://www.euler.finance/blog/eulers-innovative-liquidation-engine)
