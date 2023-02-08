## gmx

<br>

### tl; dr

<br>

* decentralized spot and perpetual futures exchange, built on arbitrum and avalanche, with low swap fees and zero price impact trades (large trades are set at the mark price).
* gmx enables traders to open up to 30x leveraged long or short positions via borrowing from a multi-asset pool known as [$GLP](https://gmxio.gitbook.io/gmx/glp) ($BTC, $ETH, $UNI, $LINK, and stablecoins), that earns lp fees through market making, swap fees, leverage trading, and asset rebalancing).
* $GLPs function as the counterparty, as it accrues values when traders loses, and devalues when traders win. $GLP accrues 70% of all trading fees, while stakers of the protocol governance token, earn 30%. $GLP is also emerging as a form of collateral, with lending protocols integrating the LP token into their product offerings.
* native token $GMX functions as a governance, utility, and value-accrual token. all collected fees fo to the $GMX fee pool, which issues fee rewards (e.g., ETH/AVAX).
* a floor price fund helps ensure liquidity in the $GLP pool, plus a reliable stream of $ETH rewards fo $GMX stakers.
* protocol's revenues come from: swap fees, trading fees, execution fees, liquidation fees, and borrow fees. protocol risks: liquidity risks, market/oracle manipulation, centralization risk, scalability risk.
* liquidation price: when (collateral - losses - borrow fee) is less than 1% of position's size. 
* the cost to open / close a position is 0.1% of the position size. long positions are opened at the higher price and closed at the lower price, short positions are opened at the lower price and closed at the higher price.

<br>

### in this dir

<br>

* [tokenomics](tokenomics.md)
* [oracle abuse](oracle_abuse.md)
* [glp vaults](glp_vaults)

<br>

---

### resources

<br>

* [gmx docs](https://gmxio.gitbook.io/gmx/)
* [synapse bridge](https://synapseprotocol.com/)
* [contracts](https://gmxio.gitbook.io/gmx/contracts)
* [gmx, by flood capital](https://twitter.com/FloodCapital/status/1562856005259902976)
* [gmx oracle, by pressiemoomboy](https://twitter.com/PressieMoonBoy/status/1562905337723748352)
