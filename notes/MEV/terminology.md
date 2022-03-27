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
