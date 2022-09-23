## 🍕 More dets on validators

<br>

### tl;dr

<br>

- the validator is responsible for creating a new block and sending it out to other nodes on the network.
- to participate as a validators, a user must deposit 32 ETH into the deposit contract and run 3 pieces of software: 
      - an execution client 
      - a consensus client
      - the engine api
- once activated, validators receive new blocsk from peers (the txs delivered in the block are re-executed, and the block signature is checked).
- the validator then sends a vote (attestation) in favor of that block across the network.
- the timing of blocks is not determined by the mining difficult anymore, but it's fixed:
     - slots (12 seconds)
     - epochs (32 slots)
- in every slot, a committee of validators is randomly chosen, whose votes are used to determine the validity of the block being proposed.
- the first block in each epoch is a checkpoint.

<br>

### validator lifecycle

<br>

The sequence of states that a validator can exist in:

1. deposited: At least 32 ETH has been deposited to the deposit contract by the validator.
2. pending: the validator is in the activation queue waiting to be voted into the network by existing validators.
3. active: currently attesting and proposing blocks.
4. slashing: the validator has misbehaved and is being slashed.
5. exiting: the validator has been flagged for exiting the network, either voluntarily or because they have been ejected.

<br>

### the JSON-RPC interface

<br>

* interface that allows us to write programs that use an Ethereum client as a gateway to an Ethereum network and blockchain.
* the RPC interface is offered as an HTTP service on port 8545. For security reasons it is restricted, by default, to only accept connections from localhost.

<br>

### setting a dedicated hardware

<br>

* [Check estimate of the blockchain size](https://bitinfocharts.com/ethereum/).
* Minimum specs:
  - CPU with 4+ cores
  - 32 GB+ RAM
  - fast SSD with at least 1T free space
  - 25+ MBit/sec download internet service



<br>





