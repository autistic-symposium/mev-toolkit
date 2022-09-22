## MEV at KeeperDAO

<br>

* MEV refers to profit that can be extracted from a transaction from the transaction originator needing priority or control over the ordering of that transacion in a block (*the arbitrage has 45 WETH of MEV*).
* [As may of 2021, around $3-4mil of MEV is being captured daily](https://explore.flashbots.net/).
* MEV exists on any blockchain and layers where there is a party responsible for transaction ordering (eg. validators, rollup providers).
* Extracted MEV = Successful MEV transactions + Successful MEV transactions gas fees + Failed MEV transactions gas fees
* Common MEV strategies are front-running, back-running, and sandwiching.
* MEV should accrue to the originator of the transaction, or of the transactions or protocols that create the MEV in the first place.
* Using KeeperDAO's **coordination layer**, we can capture and recycle the MEV before it can be extracted.

<br>

### Arbitrage opportunity

* Results from a difference in prices between the same asset, listed on different DEXes.
* A transaction that makes the right swaps along the right arbitrage route will end up with profit.


### Keepers

* Bots observe Ethereum, and other blockchains, to faciliate sorts of transactions, such as arbitrage, liquidations, auctions.
* Automated agents that survey the state of the blockchain and compute all the different possibilitie in order to identifty transactions that can create profit.
* Once Keepers have identified a valuable transaction, they will broadcast that to the network. Other keepers can copy and broadcast the same transaction with themselves as the originators.
* MEV arises from the problem of "how can a keeper ensure that they are the one who gets a transaction settled first?
* Keepers compete with each other in a zero-sum game, transforming Ethereum into a highly zero-sum game.
* Inside KeeperDAO, keepers don't need to compete - but coordinate and capture on-chain profits efficiently. DeFi users, protocols, market makers can bring their activity to KeeperDAO and gain a portion of the profits as a reward.



<br>

### ➡️ MEV poses risks not only to the user but also to the consensus layer itself. The reorganisation of blocks, the reordering of transactions, and — even momentarily — the censorship of transactions can have profound impacts on the blockchain and breaks the assumptions of many applications.

### ➡️ Because block producers are able to prioritize transactions with higher gas fees, a bidding war between bots (who either try to arbitrage or front-run) can occur. This hurts ordinary users and DeFi platforms, because these bidding wars drive up gas fees (Priority Gas Auctions) and cause slippage and failed transactions



<br>

#### Gas golfing

* use addresss that start with a long string og zeroes (take less space, less gas, to store)
* leaving small ERC20 token balances in constracts since it cost more gas to initialize a storage slot then to update a storage slot


