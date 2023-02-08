## glp vaults

<br>

### tl; dr

<br>

* vaults are suites of trustless defi strategies to generate delta-minimized returns on $GLP assets (gmx's lp token, which receives 70% of gmx's fee revenue). 
* vaults can provide liquidity on gmx to collect yield from $GLP. they are also the counterparty to margin traders (benefiting from trader losses). 
* vault should be backtested against months of real-world market data (including edge cases), usually with a baseline such as a standalone usdc vault
* hedges are algorithmically rebalanced at regular intervals. hedging on gmx incurs fees for minting and burning of $GLP, opening and closing positions, and funding for open interest.

<br>

### resources

<br>
