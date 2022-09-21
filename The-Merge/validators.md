## Notes on validators

<br>

* the validator is responsible for creating a new block and sending it out to other nodes on the network.
* to participate as a validators, a user must deposit 32 ETH into the deposit contract and run 3 pieces of software:
      - an execution client
      - a consensus client
      - a validator

* once activated, validators receive new blocsk from peers - the txs delivered in the block are re-executed, and the block signature is checked
* the validator then sends a vote (attestation) in favor of that block across the network
* the timing of blocks is not determined by the mining difficult anymore, but it's fixed:
     - slots (12 seconds)
     - epochs (32 slots)
* in every slot, a committee of validators is randomly chosen, whose votes are used to determine the validity of the block being proposed
* the first block in each epoch is a checkpoint
