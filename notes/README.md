## Notes on MEV

<br>

### How the blockchain works 101

* Each block in the blockchain contains a list of transactions in a particular order, enconding a sequence of updates to the blockchain sate (world state).
* Anyone can broadcast a transaction to the network, which means that the transaction is public. A broadcast is a request. In order for that request to be carried out, someone must place the transaction in a block and add the block to the blockchain.
* Anyone can listen for transactions being broadcast and gather them into a list. In order to a turn a list into a block, it needs to be validated. Validation creats a mathematical (cryptographic) proof that the state changes are consistent.
* In a proof-of-work blockchain, block producers are miners. In a proof-of-stake blockchain, they are validators.
* The act of converting a transaction into a block is called *settlement*. The process of block production is called *settlement layer* or *consensus layer*.
