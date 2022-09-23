## 🌶 rook

<br>

### tl,dr 

* rook provides the infrastructure to make DeFi more secure, profitable and egalitarian for users, protocols and Keepers through proliferating the Keeper Economy and negating the possibility of predatory MEV extraction on blockchains.
* the Rook Protocol is the first protocol that allows generalized MEV to be internalized at the application layer. This protects users and protocols from negative externalities, reduces the total MEV available at the consensus layer, and ensures that less value overall is being extracted from markets and protocols by miners and validators. Rook Labs has designed a comprehensive system that can flexibly capture a wide variety of application-layer transaction flow, and create a positive-feedback flywheel that aggregates and re-distributes MEV among participants in a way that increases overall network and market efficiency.
* rook Labs maintains several distinct API services that cater to specific use-cases, including market making, automated trading, dApps (e.g. DEXes, DEX aggregators, wallets), smart contracts, and a general-purpose RPC. Transactions enter the Rook Protocol’s virtual mempool, where only whitelisted Keepers, certified, high-powered bot operators who bid on the right to execute transactions and capture the maximal extractable value created, can settle those transactions to an actual blockchain by bidding on the opportunity. The winning bid is distributed by the Rook Protocol Bid Distribution Controller through a series of payment channels, to incentivize the various parties involved in the transaction.

<br>

---

### core products

<br>

#### [Coordination Protocol](https://github.com/bt3gl-labs/Scratch-Space-Stateful-Blockchains-and-MEV/blob/main/keeperDAO/coordination_protocol.md)

#### hiding game

* Gasless limit order system that sources liquidity from all means supported by KeeperDAO Keepers.
* If a user's order creates a MEV opportunity, the user will be rewarded with a share of the MEV profits in the form of `ROOK'.

#### hiding vault

* A generalized liquidation-mitigation lending and borrowing NFT product. 
* The first platform supported by Hiding Vaults is Compound Finance. 
* Using a Hiding Vault mitigates both the risks and the impacts of the liquidation of users using Compound Finance. 
* If a user's position is liquidated, the user will be reimbursed with a share of the liquidation profits in the form of `ROOK`.

#### liquidity pools

* KeeperDAO offers five single-asset LP that yield `ROOK` tokens (ETH, WETH, USDC, renBTC, and DAI): users earn `ROOK` rewards based on the number  of `ROOK` rewards allocated to the pool each quarter.


<br>

---

### projects of interest

<br>

* [KeeperDAO analytics](https://github.com/keeperdao/analytics)
* [Keeper Improvement Proposals (KIPs)](https://github.com/keeperdao/kips)
* [KD UniV3 Challenge](https://github.com/keeperdao/solidity-challenge-2)
* [Security audits docs](https://github.com/keeperdao/docs/tree/master/audits)
* [kAave](https://github.com/keeperdao/kaave)
* [Hiding book API info](https://hidingbook.keeperdao.com/api/v1/info)


<br>

---

### documents of interest

<br>

* [Docs page](https://docs.keeperdao.com/reference/)
* [Forum page](https://forum.keeperdao.com/)
* [Roadmap](https://www.keeperdao.com/files/roadmap.png)
* [Motivational whitepaper](https://github.com/keeperdao/whitepaper)
* [Technical whitepaper](https://www.keeperdao.com/files/gov-beigepaper.pdf)
* [Blog page](https://blog.keeperdao.com/)
* [Medium blog](https://medium.com/keeperdao)
* [The New Citadel: A vision for KeeperDAO](https://keeperdao-labs.notion.site/The-New-Citadel-A-Vision-for-KeeperDAO-125ed6222f4542d99d8e171ddbe2bc38)
* [KeeperDAO twitter](https://twitter.com/Keeper_DAO)
* [KeeperDAO treasure](https://app.zerion.io/0x9a67F1940164d0318612b497E8e6038f902a00a4/overview)
* [Youtube Town Halls](https://www.youtube.com/channel/UCDNHJWdB32MdwcHs0Btiaxg/videos)
* [Contracts registry](https://docs.keeperdao.com/reference/for-beginners/smart-contracts)
* [Gnosis multi-sig](https://gnosis-safe.io/app/eth:0xa8b0a855BE21568B93f32805b244158Cc61AD006/balances)

