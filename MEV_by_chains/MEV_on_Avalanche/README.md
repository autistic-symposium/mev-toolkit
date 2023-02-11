## mev on avalanche

<br>


### tl; dr

<br>

* [on why a larger (stake) validator had arb advantages:](https://www.ddmckinnon.com/2022/11/27/all-is-fair-in-arb-and-mev-on-avalanche-c-chain/)
  - *"It all came down to sampling. Snowman-vintage validators would gossip new blocks to one another through a number of different message types. When a new potentially arb-creating transaction was proposed, the validator or node through whom it was communicated via its RPC endpoint, sent a PushQuery message to default 10 peers. Those 10 peers gossiped to 10 more and so on until a tipping point of validators accepted the block. This is described in more detail in the Ava Labs whitepaper. The PushQuery message contains both the peer nodes’ preference for the tip of the blockchain and the proposed new block. The sooner one receives and decodes this message, the sooner one can update the graph and fire an arb out in response. Being one of those first 10 nodes was a huge competitive advantage. Those 10 nodes were selected via a stake weighted process. The probability of hearing about a transaction first scaled linearly with the stake of that node. Thus, a bot connected to a massive AVAX stake would have a nearly insurmountable advantage in arbitrage on Avalanche without access to a large edge elsewhere."*


<br>



---

### resources

<br>

* [gmx resources](https://github.com/go-outside-labs/mev-toolkit/tree/main/MEV_by_chains/MEV_on_Arbitrum/gmx)
* [chainsight on avax mev](https://avax.chainsight.dev/)
* [all fair in arb and mev on avalanche](https://www.ddmckinnon.com/2022/11/27/all-is-fair-in-arb-and-mev-on-avalanche-c-chain/)
* [avalanche blockchain consensus](https://docs.avax.network/overview/getting-started/avalanche-consensus)

