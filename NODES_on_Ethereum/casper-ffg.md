## 🍺 Casper FFG

<br>

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
