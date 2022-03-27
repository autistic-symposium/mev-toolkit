## KeeperDAO notes

<br>

**KeeperDAO provides the infrastructure to make DeFi more secure, profitable and egalitarian for users, protocols and Keepers through proliferating the Keeper Economy and negating the possibility of predatory MEV extraction on blockchains.**

<br>

```
🏗️ KeeperDAO is building the Coordination Layer for DeFi.

We are creating a world where users and protocols own the value generated from their transactions, and where 
best execution and financial services are powered entirely by this value, rather than fees. Think of Citadel 
Securities, but as a public good, governed by a DAO, that returns nearly all the profit back to its users.

We have deep experience in blockchain automation, MEV, and financial systems, and want to join with others like us, 
or teach the best candidates about this exciting area of modern finance. 

DAOs are hard, so we are dedicated to creating the right environment for you to do your best work. At KeeperDAO you’ll 
have the opportunity to work on solving hard and important problems that will help innovate and improve the way value 
is exchanged on the blockchain. You will be surrounded by some of the brightest minds in web3 and given all the 
resources you need to do your best work.

We’re an early stage startup with a very healthy, liquid treasury (over US$100mm), putting us in a prime position 
to grow and scale over the coming years. By joining us now you will be in a position to help meaningfully shape 
the future of open finance on the blockchain.

We’re backed by some of the most reputed investors in web3: Three Arrows Capital, Polychain Capital and Amber Group.

♜
```



---

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

--- 

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




<br>

----

<br>

## Projects of interest

* [KeeperDAO analytics](https://github.com/keeperdao/analytics)
* [Keeper Improvement Proposals (KIPs)](https://github.com/keeperdao/kips)
* [KD UniV3 Challenge](https://github.com/keeperdao/solidity-challenge-2)
* [Security audits docs](https://github.com/keeperdao/docs/tree/master/audits)
* [kAave](https://github.com/keeperdao/kaave)


<br>

## Documents of interest


* [docs page](https://docs.keeperdao.com/reference/)
* [forum page](https://forum.keeperdao.com/)
* [Whitepaper](https://github.com/keeperdao/whitepaper)
* [Blog page](https://blog.keeperdao.com/)
* [Medium blog](https://medium.com/keeperdao)
* [The New Citadel: A vision for KeeperDAO](https://keeperdao-labs.notion.site/The-New-Citadel-A-Vision-for-KeeperDAO-125ed6222f4542d99d8e171ddbe2bc38)
* [KeeperDAO twitter](https://twitter.com/Keeper_DAO)
* [KeeperDAO treasure](https://app.zerion.io/0x9a67F1940164d0318612b497E8e6038f902a00a4/overview)
* [Youtube Town Halls](https://www.youtube.com/channel/UCDNHJWdB32MdwcHs0Btiaxg/videos)
* [Contracts registry](https://docs.keeperdao.com/reference/for-beginners/smart-contracts)

