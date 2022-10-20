
# 🍮 cow.fi

<br>

<img width="500" alt="Screen Shot 2022-10-19 at 8 11 15 PM" src="https://user-images.githubusercontent.com/1130416/196847611-7d8d677a-e26b-4884-969d-11a6d6d7cd88.png">


<br>

#### [cow swap](https://swap.cow.fi/#/faq?chain=mainnet) is the first trading interface built on top of cow protocol.
#### it's a meta dex aggregator that allows you to buy and sell tokens using gasless orders that are settled p2p among users or into any on-chain liquidity while providing mev protection
#### meta: the protocol matches trades via batch auctions for a variety of on-chain liquidity sources.
#### traders can be settled via underlying on-chain amms directly or via dex aggregators, depending on which pool/path offers the best price -> a dex aggreagator of dex aggregators

<br>

<img width="700" alt="Screen Shot 2022-10-19 at 8 09 41 PM" src="https://user-images.githubusercontent.com/1130416/196847398-b1be7347-8699-4a67-86b8-d1cb29c0833b.png">



<br>

## tl; dr

* proposed solutions to mev
  - base layer: enforce random ordering, encrypt tx content (time-locked, commit-reveal), separate tx sequencing & tx execution
  - infrastructure level: flashbots (mev geth), mistx, archer swap
  - dapp level (rook, 0x rfq orders, gnosis protocol)
* core ideas
  - delegate trade execution with gpv2
  - coincidence of wants (fully mev protected, max gas efficient, no lp fees)
  - batch auditions

<br>

## cow protocol

at high level, CoW Protocol strives to achieve the following:

- Competitiveness. Provide the best possible prices for its users, and in particular, prices that are at least as good as the users can find in any DEX.
- Fairness. Provide uniform exchange rates for all orders trading the same token pair.
- Decentralization. Provide such prices in a decentralized way.
- Protocol viability. Ensure the long-term viability of the protocol and its token.

<br>

### solver competition

- decentralized price-finding mechanism by entitites, known as solver
- excess is settled in the same transaction with the best available AMM. 
- the transaction is sent by professional “solvers” which set tight slippage bounds. 
- two traders each hold an asset the other wants, an order can be settled directly between them without an external market maker or liquidity provider, solvers compete with each other to achieve best prices for the user.

<br>

* [type of solvers](https://docs.cow.fi/off-chain-services/solvers/type-of-solvers)

<br>

---

## links

* [cow.fi](https://cow.fi/)
* [cow protocol forum](https://forum.cow.fi/)
* [cow swap at mev.wtf 2022](https://docs.google.com/presentation/d/1vClubmyECHzYpT7-DzU6D45bc7iNpjF1NuiEblY-8ZQ/edit#slide=id.ge33f22559c_0_580)
* [gnosis on cow protocol](https://docs.google.com/presentation/d/1vClubmyECHzYpT7-DzU6D45bc7iNpjF1NuiEblY-8ZQ/edit#slide=id.ge33f22559c_0_580)
* [gnosis protocol dune dashboard](https://dune.com/cowprotocol/Gnosis-Protocol-V2)
