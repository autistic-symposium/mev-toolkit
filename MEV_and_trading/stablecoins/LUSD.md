## LUSD

<br>

### tl; dr

* issued by [liquity protocol](https://twitter.com/LiquityProtocol), $LUSD has zero governance, fully decentralized collateral, instant liquidation, lower liquidity level than $DAI, and no loss to holders since launch.
* **redemption**: $LUSD uses CDP model where 1 $LUSD is minted via deposit of at least $1.1 worth of $ETH, so that 1 $LUSD is always backed by > $$1.1 worth of $ETH
  - during arbs, $LUSD received will pay back the debt of troves with the lowest collateral ratio (CR)
  - troves with low CR's are incentivized to improve CR (either top-up their collateral or repay loans)
  - redemption reduces debtors' $ETH exposure, and the fee makes it unattractive for arb
* **stability pool**: pooling a $LUSD reservoir for instant liquidation of troves with low CR. those depositing $LUSD into it become liquidators, and profit from liquation is ~10%.
  - $LUSD premium in times of market turmoil.
  - like DCA into $ETH at prices lower than usual by buying liquidations. e.g., provide $LUSD into the stability pool.
* **redistribution**: in case there is 0 $LUSD left in the stability pool, the system redistributes both the debt and collateral from liquidated troves to all other existing troves, based on a portion of collateral of each trove vs. total collateral of all troves.
  - retribution causes individual troves' CR to decrease and be more prone to liquidation (but for each 1 $LUSD they can get > $1 $ETH).
  - buy the dip of $ETH: deposit $ETH into the stability pool when 1) $ETH market price is ~ prices troves are liquidated, or 2) when TCR is almost < 150%. 



<br>

---

### resources
