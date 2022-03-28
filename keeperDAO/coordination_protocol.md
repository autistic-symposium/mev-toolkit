# Coordination protocol

<br>


<br>

**KeeperDAO uses the power of Coordination to create more efficient markets by capturing and recycling MEV to the 
users and protocols that create it.**

<br>

**KeeperDAO is a decentralised and coordinated Keeper commonwealth making the Ethereum network more egalitarian, profitable, and secure for all the actors involved.**

<br>

<br>

## Coordination Game

<br>

* First protocol that allows generalized MEV to be internalized at the application layer, protecting users and protocols from negative externalities, reducing the total MEV available at the consensus layer, and ensuring that less value overall is being extracted from markets and protocols by miners and validators.

* Design a comprehensive system that can flexibly capture a wide variety of application-layer transaction flow, creating posiive-feedback flywheel that aggregates and re-distributes MEV among participants in a way that increases overall network and market efficiency.

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


<br>

<img width="985" alt="Screen Shot 2022-03-27 at 6 12 10 PM" src="https://user-images.githubusercontent.com/1130416/160285641-3639f584-55af-4e0f-b85e-25d84f933bd6.png">


<br>


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

* KeeperDAO uses a proprietary reputation algorithm that's a simple scoring system based on actions performed by keepers.
* reputation values are fed to the coordinator's greenlight algorithm to help select the winnter of an auction

### Greenlight algorithm

* bid quantity (the higher the better)
* reputation
* randomness
* fill quantity (larger fill quantities)
* staked ROOK quantity (the more the best)

<br>

---

<br>

## How Market Makers benefit

<br>

* KeeperDAO provides arbitrage as a service (using the Rook Network)

* KeeperDAO is the most convenient, secure, and profitable network for on-chain market makers:
   * 1) one single integration to access all DeFi and CeFi liquidity: orders will be arbitraged against KeeperDAO users, other market makers, Uniswap, Curve, Balancer, Bancor, Binance, etc...
   * 2) KeeperDAO provides market makers with three different profit mechanisms: i) capture spreads or hedge fills, ii) earn arbitrage rewards in ROOK on every trade, 3) weekly pilot program rewards

* Before KeeperDAO, DeFi asked market makers to execute their own trades, meaning they had to navigate gas, fees, liquidity, bridging, routing, L2s, settlements, MEV.

<br>

<img width="950" alt="Screen Shot 2022-03-27 at 8 58 52 PM" src="https://user-images.githubusercontent.com/1130416/160292233-685b42de-aa3d-412e-afa4-be811a8b664b.png">


<br>

### MM integration guide

* [APIs and code here](https://docs.keeperdao.com/reference/integrate/run-a-market-maker/automated-trading)

<br>

---

<br>

## Running a Keeper

<br>

### Example keeper bot technicuqes

* DeFi arbitrage, cross the user with Uniswap or other on-chain  DEX
* CeFi arbitrage, cross the user with Coinbase, etc
* Liquidation facilitation
* Front running, tailgating, etc.
* Keepers can also fill a user's order

<br>

<img width="495" alt="Screen Shot 2022-03-27 at 9 24 22 PM" src="https://user-images.githubusercontent.com/1130416/160293080-c1fc9881-f09f-4b64-b41d-6180c3ade8fd.png">


<br>


### Keeper bot architecture

* a keeper bot: integrated with the coordinator and hidingbook components
* Coordinator websocket server: keepers connect and communicate with the coordinator using this server. When they find arbitrage they place a bid via web sockets noting the specific order/liquidation. The coordinator prevents gas auctions and bad behaviors, and broadcast the winner of the auction letting the greenlit keeper know they can take the order/liquidation. The keeper can then capture the arbitrage or MEV they way they like (mempool, flashbots, eden, miningdao, etc).
* Coordinator http server: keepers provide and gather critical info from this server (must register their addresss with the coordinator)
* HidingBook http server: the orderbook containing user order only fillable by whitelisted KeeperDAO keepers.
* HidingBook websocket server: keepers listen to real time order update events using this endpoint. This ensures they get orders as soon as they are posted and know when the order is filled or expired.


<br>

---

<br>

## Payment channels

* Keepers transact with the coordinator off-chain using payment channels.
* They will open this payment channel by staking ROOK into a contract and then pass signed commitments with the Coordinator.
* Having this payment channel off-chain reduces gas costs for keepers participating in the Cordination game.


