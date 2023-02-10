## block builders on ethereum

<br>

### tl; dr

<br>

* block builders have the same 3 sources of tx as validators did before the merge. they can:
    1. act as searchers and include their own MEV-extracting transactions.
    2. include txs submitted to them privately, including those submitted by external searchers (through a "bribe" through either coinbase payments or `txsFees`).   
    3. include pending tx broadcasted in the public mempool
* `blockValue` = `txFees` + MEV
* builders will aggregate txs from users, MEV searchers, and own private order flow to make the highest value blocks possible
* builders having its blocks included consistently incentivizes more private order flow (searchers want their tx included)
* builder can be selling future blockspace upfront so market makers or protocols can secure block space for their transactions or users


<br>


<img width="530" src="https://user-images.githubusercontent.com/1130416/217417346-50916961-aaa2-49ef-ad10-2f623a959fa6.png">


<br>

----

### resources

<br>

* [builder specs, by the ef](https://github.com/ethereum/builder-specs)
* [flashbots builder](https://github.com/flashbots/builder)
* [etherscan blocks](https://etherscan.io/blocks), [mev blocks](https://etherscan.io/blocks/label/mev-block), and [mev builders](https://etherscan.io/accounts/label/mev-builder)
* [builder69.io endpoint for searchers (bundle/tx)](https://builder0x69.io)
* [mev-rs - gateway to a network of block builders](https://github.com/ralexstokes/mev-rs)
* [mev order flow, the king of block builders](https://coinyuppie.com/mev-order-flow-the-king-of-block-builders/)
* [manifold finance](https://www.manifoldfinance.com/)
* [flashbots block building algorithm](https://writings.flashbots.net/searching-post-merge#blockbuilding-algorithm)
* [block builder decentralization is coming, but maybe not so soon, by ballsyalchemist](https://bittokoin.substack.com/p/block-builder-decentralization-is)
