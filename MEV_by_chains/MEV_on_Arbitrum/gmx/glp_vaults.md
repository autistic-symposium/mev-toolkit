## glp vaults

<br>

### tl; dr

<br>

* vaults are suites of trustless defi strategies to generate delta-minimized returns on $GLP assets (gmx's lp token, which receives 70% of gmx's fee revenue). 
* vaults can provide liquidity on gmx to collect yield from $GLP. they are also the counterparty to margin traders (benefiting from trader losses). 
* vault should be backtested against months of real-world market data (including edge cases), usually with a baseline such as a standalone usdc vault
* hedges are algorithmically rebalanced at regular intervals. hedging on gmx incurs fees for minting and burning of $GLP, opening and closing positions, and funding for open interest.

<br>

### pool exposures

<br>

* the first component of a pool are the available assets, which are the vault assets minus reserved assets (assets set aside to cover longs).
* by covering longs, a reserved $BTC that would move with $BTC is used to cover a long position by surrendering all the upside gains to the counterparty (but also taking all collaterals of the counterparty when the price of $BTC goes down).
* conversely, a short against the pool becomes a synthetic long as its credit gains to the pool when the price goes up (but takes money from the pool when the price goes down).
* hedging $GLP means taking short positions, either on GMX or on a CEX. The short pays when the directional asset goes down, and loses when the opposite happens.
* the spread of hedged $GLP over $ETH is a good measure of $GLP's performance, and why a hedged strategy might be a better holding strategy that minimises volatility.

<br>

### resources

<br>

* [rage-gmx vaults](https://mirror.xyz/0x507c7777837B85EDe1e67f5A4554dDD7e58b1F87/KztyQ37Nfq7QT1BWrLz30jfqdtV23TtilJK1cbyXpxk0)
* [sentiment.xyz](https://www.sentiment.xyz/)
* [stfx](https://twitter.com/STFX_IO)
* [gmd protocol](https://twitter.com/GMDprotocol)
* [yield yak](https://twitter.com/yieldyak_)
* [vesta finance](https://twitter.com/vestafinance)
* [jones dao](https://twitter.com/DAOJonesOptions)
* [dopex](https://twitter.com/dopex_io)
* [olive app](https://oliveapp.finance/trade/options/zero-capital-risk/glp-glp?chainID=42161)
* [vovo finance](https://twitter.com/VovoFinance)
* [perpy finance](https://twitter.com/PerpyFinance)
* [lyra finance](https://twitter.com/lyrafinance)
* [neutra finance](https://twitter.com/Neutrafinance)
* [tender.fi](https://twitter.com/tender_fi)
* [gml vault tech overview](https://gmx-io.notion.site/gmx-io/GMX-Technical-Overview-47fc5ed832e243afb9e97e8a4a036353)
* [dune board on protocol strategies on top of $GLP](https://dune.com/dbustos20/protocol-strategies-on-top-of-glp)
