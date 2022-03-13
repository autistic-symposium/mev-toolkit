## ⚡🧱⛓ [scratch space] Stateful Blockchains, MEV, Solidity, Flashbots...

<br>


## ☠️ My notes

<br>

* [Chapter I: `geth` and running an Ethereum node](https://github.com/bt3gl-labs/Getting-Started-MEVs-and-Flashbots/blob/main/chapter_I.md)
* [Chapter II: The Mempool and MEV](https://github.com/bt3gl-labs/Getting-Started-MEVs-and-Flashbots/blob/main/chapter_II.md)
* [Chapter III: Flashbots](https://github.com/bt3gl-labs/Getting-Started-MEVs-and-Flashbots/blob/main/chapter_III.md)
* [Chapter IV: Flashbots bundle](https://github.com/bt3gl-labs/Stateful-Blockchains-and-Flashbots/blob/main/chapter_IV.md)

<br>
<br>

---

## ☠️ My code

<br>

* [PoCs having `geth` in Docker and K8s](https://github.com/bt3gl-labs/Stateful-Blockchains-and-Flashbots/tree/main/geth_and_k8s)
* [Solidity scratch space](https://github.com/bt3gl-labs/Stateful-Blockchains-and-Flashbots/tree/main/solidity)


<br>
<br>


---

## ☠️ Some terminology

<br>

#### Merkle tree: a type of binary tree, composed of a set of notes with a large number of leaf nodes at the bottom of the tre containing the underlying data, a set of intermediate nodes where each node is the hash of its two children, and finally a single root node, also formed from the hash of its two children, representing the top of the tree.


<br>

#### 𝕄𝕒𝕩𝕚𝕞𝕒𝕝 𝕖𝕩𝕥𝕣𝕒𝕔𝕥𝕒𝕓𝕝𝕖 𝕧𝕒𝕝𝕦𝕖 (MEV, formerly "miner" in the context of Proof of Work) refers to the maximum value that can be extracted from block production in excess of the standard block reward and gas fees by censoring and/or changing the order of transactions in a block.

<br>

#### The 𝕞𝕖𝕞𝕡𝕠𝕠𝕝 is the set of pending, unconfirmed transactions in the EVM... when someone sends a transaction in the blockchain, there is a delay between the time when the transaction is broadcasted to the network and when it is actually mined into a block. During this period, transactions sit in a pending transaction pool, the mempool, where contents are visible to everyone. 

<br>

#### 𝔽𝕣𝕠𝕟𝕥𝕣𝕦𝕟𝕟𝕚𝕟𝕘, also known as Priority Gas Auctions (PGAs), happens when a miner steals a profitable opportunity (such as arbitrage) for themselves by sending the same transaction with a higher gas price. For example, a transaction A is broadcasted with a higher gas price than an already pending transaction B so that A gets mined before B (e.g., to snatch a Uniswap price arbitrage trade to rebalance a pool).

<br>

#### 𝔹𝕒𝕔𝕜𝕣𝕦𝕟𝕟𝕚𝕟𝕘 happens when a transaction A is broadcasted with a slightly lower gas price than already pending transaction B so that A gets mined right after B in the same block. (eg. to execute a DyDx liquidation after a price oracle update that triggers a DyDx loan to go under the required collateralization ratio).

<br>

#### 𝕊𝕒𝕟𝕕𝕨𝕚𝕔𝕙𝕚𝕟𝕘 is the profiting off slippage in liquidity pools by buying and selling before and after large transactions posted in the mempool.

<br>


#### 𝔻𝔼𝕏 𝕒𝕣𝕓𝕚𝕥𝕣𝕒𝕘𝕖 happens when two DEXes are offering a token at two different prices and one can buy the token on the lower-priced DEX and sell it on the higher-priced DEX.


<br>

#### 𝕃𝕚𝕢𝕦𝕚𝕕𝕒𝕥𝕚𝕠𝕟𝕤 happens when the value of a borrowed asset exceeds the collateral and anyone can liquidate the collateral and collect the liquidation fee for themselves.


<br>


#### Long Tail MEV encompasses all other forms of MEV not described here. Long Tail MEV describes niche, arcane, undiscovered MEV often realized through interacting with lesser known protocols, event based strategies, or unorthodox economic mechanisms.


<br>





---

## ☠️ Further resources

<br>

- [Flashbots](https://github.com/flashbots/pm) maintains a proof-of-concept communication channel for users to send their Ethereum transactions directly to miners.
- [MEV wiki](https://www.mev.wiki/)
- [Etherscan data on flashbots](https://etherscan.io/blocks/label/flashbots)
- [MEV Dashboard by Flashbots](https://explore.flashbots.net/).
- [Sandwiched?](https://sandwiched.wtf/)
- [How to use Flashbots](https://cryptomarketpool.com/how-to-use-flashbots/)
- [Flashbots bundle explore](https://flashbots-explorer.marto.lol/)
* [Flash Boys 2.0, the original article](https://arxiv.org/pdf/1904.05234.pdf)
* [Ethereum is a Dark Forest by Paradigm](https://www.paradigm.xyz/2020/08/ethereum-is-a-dark-forest)
* [Escaping the Dark Forest by samczsun](https://samczsun.com/escaping-the-dark-forest/)
* [How to Build an Ethereum Mining Pool by Dragonfly research](https://medium.com/dragonfly-research/how-to-build-an-ethereum-mining-pool-6be356520b7a)
* [MEV and Me by Paradign](https://research.paradigm.xyz/MEV)
   - "if block rewards are small enough compared to MEV, it can be rational for miners to destabilize consensus."
   - "The rate at which MEV accumulates on a given blockchain is generally proportional to the complexity of its application-layer behavior."
* [Return to the Dark Forest by rekt](https://rekt.news/return-to-the-dark-forest/)
* [Modern MEV sandwich attacks on Ethereum routers by totlsota](https://mirror.xyz/totlsota.eth/9JaNkZ1XQfQD6Y79aLYHC_kb_dSBoJ2JYiag5BuGGM8)
* [Dr. Reorg or: How I Learned to Stop Worrying and Love MEV by Saneel Sreeni](https://medium.com/dragonfly-research/dr-reorg-or-how-i-learned-to-stop-worrying-and-love-mev-2ee72b428d1d)
* [Hiding in Plain Sight by samczsun](https://samczsun.com/hiding-in-plain-sight/)
* [We Live In A Mempool: Backrunning the MEV Crisis by Tom Schmidt](https://medium.com/dragonfly-research/we-live-in-a-mempool-backrunning-the-mev-crisis-a4ea0b493b05)
* [How To Light Up The Dark Forest by Robert Miller](https://writings.flashbots.net/writings/the-anatomy-of-an-inspector/)
* [KeeperDAO's whitepaper](https://github.com/keeperdao/whitepaper/blob/main/whitepaper.pdf)

<br>
<br>

