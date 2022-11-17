## Consensus mechanisms in PoS in Ethereum

>Proof-of-Stake Ethereum features two consensus mechanisms running in parallel, FFG Casper and LMD GHOST.

<br>


### casper FFG

* responsible for providing economic finality to the chain.
* when a checkpoint block (the start of an epoch) accumulates enough target votes, it becomes justified. When a recently justified source is used to justify a target checkpoint, the target checkpoint is justified and the source becomes finalised. no conflicting checkpoint block can be also finalised without at least 1/3 of the active stake getting slashed. there can be no re-org of the finalised chain without a massive loss of ETH by some party.

<br>

### LMD GHOST

* provide a dynamically available ledger - grow the chain while finalisation runs. headers in this chain accumulate weight by the head vote from attesters. the weight is used to figure out which branch the validator should follows if a fork happens.


<br>

### lexicon

* block trees: if ethereum gets out of sync (network latency, deliberate attack, etc.), the blockchain can quickly become a block tree. validators need a method to choose a branch and identigy a single canonical blockchain.
* checkpoint: a block every N blocks.
* root: always justified and finalized.
* supermajority link: ordered pair (x, y) of checkpoints where >2/3 of validators voted that y is the valid descedent from x.
* justification: a block is justified if there exists a supermajority link between it and a previously justified block.
* finalization: a block is finalized if it is justified and there is a supermajority link between the block and its direct descendent.
* when a new checkpoint is reached, each node broadcasts a vote to the network.
* votes contain a source (last justified) and a target (newlly added) checkpoint.
* validators must not publish two distinct votes such that 1) are the same height of the block tree, 2) overlapping votes.
* validators that break the casper voting rules are slashed: a portion of that validator stake is destroyed and the validator is removed from the network.
* validators have a responsibility to vote, failing to broadcast a vote will result in a small penalty, slowly draining the validators stake.

<br>


<br>

### resources 

* [Visualising the 7-block reorg on the Ethereum beacon chain](https://barnabe.substack.com/p/pos-ethereum-reorg?s=w)
