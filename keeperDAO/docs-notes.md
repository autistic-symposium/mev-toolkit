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


### Maximal
