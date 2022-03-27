# [KeeperDAO notes](https://docs.keeperdao.com/reference/)


<br>

**KeeperDAO uses the power of Coordination to create more efficient markets by capturing and recycling MEV to the 
users and protocols that create it.**

<br>

**KeeperDAO is a decentralised and coordinated Keeper commonwealth making the Ethereum network more egalitarian, profitable, and secure for all the actors involved.**

<br>


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

---


<br>

## KeeperDAO Coordination Game

<br>

* First protocol that allows generalized MEV to be internalized at the application layer, protecting users and protocols from negative externalities, reducing the total MEV available at the consensus layer, and ensuring that less value overall is being extracted from markets and protocols by miners and validators.

* Design a comprehensive syste that can flexibly capture a wide variety of application-layer transaction flow, creating posiive-feedback flywheel that aggregates and re-distributes MEV among participants in a way that increases overall netwoek and market efficiency.

<br>

<img width="861" alt="Screen Shot 2022-03-27 at 5 07 33 PM" src="https://user-images.githubusercontent.com/1130416/160282861-7677206b-d47e-4f54-bdc1-d44e24d43604.png">

<br>


### Coordination lifecycle outline


1) Keepers buy ROOK and stake it in the Coordinator smart contract. Keepers pend staked ROOK bidding on the right to execute transactions in the Coordination Game. 
2) Keepers watch incoming transactions, and search for the best way to profitably execute them.
3) When an opportunity is discovered, Keepers initiate a sub-second just-in-time auction that will decide who gets the right-of-way to execute the transaction. In the auction, Keepers place bids using their staked ROOK from (1).
4) The Coordinator Auction Module prevents Keepers from grim triggering each other during the auction, by balancing both upward and downward bid pressure to discover the fair value of the profit opportunity.
5) The Coordinator greenlights the winner of the auction, leaving them free to broadcast the transaction and collect the profit they discovered, while fulfilling the request of the user who originated the transaction.
6) Upon execution of the transaction, the bid that the winning Keeper paid to win the auction is distributed based on the image in the ROOK bid.

<br>

<img width="887" alt="Screen Shot 2022-03-27 at 6 05 38 PM" src="https://user-images.githubusercontent.com/1130416/160285393-d04754b1-4f44-4290-9d29-2b95c8b7cf85.png">


### Hiding Book


* Off-chain orderbook that hosts virtualized orders only filable by KeeperDAO keepers: single-connection access to the entire spectrum of on-chain and off-chain liquidity.
* The hiding book can act as an order relay, or a virtual mempool.
* Integrating the hiding book offers imit orders for dapps with benefits like ROOK rewards, MEV protection, and access to KeeperDAO's keepers.

### Auctions

* Keepers place a bid with the Coordinator, which is a `JSON` payload that includes: a signed bid commitment over the staked ROOK payment channel, the unique identifier of the user trade(s) being filler, the keeper's credentials, etc.

```
{
   "bids":[
      {
         "auctionId":"0x1234",
         ....
      },
      {
         "auctionId":"0x5678",
         ....
      }
   ],
   "type":"bid"
}
```

#### Auction life cycle

* *binding*:
   * all auctions are identified by an auctionID.
   * an auction begins with the first keeper bid on an auctionID
   * the auction is locked into this state where any bids received for this auctionID are competing against each other for greenlight
   * last not more than a few seconds

* *greenlight*:
  * once a keeper is greenlit to faciliate user trade, the coordinator waits a period of blocks for the keeper to mine their transaction
  * during this time, the auctionID remains locked

* *release*:
  * once the lock ends, a new auction can begin

### Reputation


<br>

<img width="985" alt="Screen Shot 2022-03-27 at 6 12 10 PM" src="https://user-images.githubusercontent.com/1130416/160285641-3639f584-55af-4e0f-b85e-25d84f933bd6.png">


<br>

