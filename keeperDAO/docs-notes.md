# [KeeperDAO notes](https://docs.keeperdao.com/reference/)


<br>

**KeeperDAO uses the power of Coordination to create more efficient markets by capturing and recycling MEV to the 
users and protocols that create it.**

<br>

**KeeperDAO is a decentralised and coordinated Keeper commonwealth making the Ethereum network more egalitarian, profitable, and secure for all the actors involved.**

<br>


## Core Products

<br>

### The Hiding Game

* Gasless limit order system that sources liquidity from all means supported by KeeperDAO Keepers.
* If a user's order creates a MEV opportunity, the user will be reward with a share of the MEV profits in the form of ROOK.

### The Hiding Vault

A generalized liquidation-mitigation lending and borrowing NFT product. 
* The first platform supported by Hiding Vaults is Compound Finance. 
* Using a Hiding Vault mitigates both the risks and the impacts of the liquidation of users using Compound Finance. 
* If a user's position is liquidated, the user will be reimbursed with a share of the liquidation profits in the form of ROOK.

### Liquidity Pools

* KeeperDAO offer five single-asset LP that yield ROOK tokens (ETH, WETH, USDC, renBTC, and DAI): users earn ROOK rewards based on the number  of ROOK rewards allocated to the pool each quarter.


<br>

## MEV

<br>

### How the blockchain works
* Each block in the blockchain contains a list of transactions in a particular order, enconding a sequence of updates to the blockchain sate (world state).
* Anyone can broadcast a transaction to the network, which means that the transaction is public. A broadcast is a request. In order for that request to be carried out, someone must place the transaction in a block and add the block to the blockchain.
* Anyone can listen for transactions being broadcast and gather them into a list. In order to a turn a list into a block, it needs to be validated. Validation creats a mathematical (cryptographic) proof that the state changes are consistent.
* In a proof-of-work blockchain, block producers are miners. In a proof-of-stake blockchain, they are validators.
* The act of converting a transaction into a block is called *settlement*. The process of block production is called *settlement layer* or *consensus layer*.

### Arbritage opportunity

* Results from a difference in prices between the same asset, listed on different DEXes.
* A transaction that makes the right swaps along the right arbritage route will end up with profit.


### Keepers

* Bots that observe Ethereum, and other blockchains, to faciliate sorts of transactions, such as arbitrage, liquidations, auctions.
* Automated agents that survey the state of the blockchain and compute all the different possibilitie in order to identifty transactions that can create profit.
* Once Keepers have identified a valuable transaction, they will broadcast that to the network. Other keepers can copy and broadcast the same transaction with themselves as the originators.
* MEV arises from the problem of "how can a keeper ensure that they are the one who gets a transaction settled first?
* Keepers compete with each other in a zero-sum game, transforming Ethereum into a highly zero-sum game.
* Inside KeeperDAO, keepers don't need to compete - but coordinate and capture on-chain profits efficiently. DeFi users, protocols, market makers can bring their activity to KeeperDAO and gain a portion of the profits as a reward.


### Maximal extractable value

* Refers to profit that can be extracted from a transaction from the transaction originator needing priority or control over the ordering of that transacion in a block (*the arbitrage has 45 WETH of MEV*).
* [As may of 2021, around $3-4mil of MEV is being captured daily](https://explore.flashbots.net/).
* MEV exists on any blockchain and layers where there is a party responsible for transaction ordering (eg. validators, rollup providers).
* Extracted MEV = Successful MEV transactions + Successful MEV transactions gas fees + Failed MEV transactions gas fees

<br>

### ➡️ While it seems simple, MEV poses risks not only to the user but also to the consensus layer itself. The reorganisation of blocks, the reordering of transactions, and — even momentarily — the censorship of transactions can have profound impacts on the blockchain and breaks the assumptions of many applications.

### ➡️ Because block producers are able to prioritize transactions with higher gas fees, a bidding war between bots (who either try to arbitrage or front-run) can occur. This hurts ordinary users and DeFi platforms, because these bidding wars drive up gas fees (Priority Gas Auctions) and cause slippage and failed transactions


### MEV strategies

* Common MEV strategies are front-running, back-running, and sandwiching.
* MEV should accrue to the originator of the transaction, or of the transactions or protocols that create the MEV in the first place.
* Using KeeperDAO's **coordination layer**, we can capture and recycle the MEV before it can be extracted.





