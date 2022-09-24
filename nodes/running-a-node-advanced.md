## 🍕 More dets on running validators

<br>
<br>

<p align="center">
<img width="547" alt="Screen Shot 2022-09-23 at 8 46 39 PM"  width="70%" src="https://user-images.githubusercontent.com/1130416/192078957-0ed3b60b-7354-4e02-b439-332b92ff0613.png">
</p>

<br>
<br>


### tl;dr architecture

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

----

### tl;dr block creation

<br>

1. execution clients gossip transactions over the execution-layer peer-to-peer network (encrypted communication)
2. a validator is selected to propose a block, and transactions from the node's local transaction pool is passed to consensus clients via a local RPC connection, which will be packaged into Beacon blocks
3. consensus clients then gossip Beacon blocks across their p2p network
4. the process requires two separate p2p networks: one connecting execution clients for transaction gossip and one connecting consensus clients for block gossip




---

### validator lifecycle

<br>

The sequence of states that a validator can exist in:

1. deposited: At least 32 ETH has been deposited to the deposit contract by the validator.
2. pending: the validator is in the activation queue waiting to be voted into the network by existing validators.
3. active: currently attesting and proposing blocks.
4. slashing: the validator has misbehaved and is being slashed.
5. exiting: the validator has been flagged for exiting the network, either voluntarily or because they have been ejected.

<br>

----

#### network addresses

<br>

* three standardized formats that any Ethereum node can understand


##### multiaddr

* universal format designed for peer-to-peer networks
* for example, a classic IPv4 listing to TCP port 33000 `/ip4/192.168.22.27/tcp/33000`, plus an node id (a hash of the pub key)


<br>

##### enode

* identify an Ethereum node using a URL address format

<br>

##### ethereum node records (ENRs)

* allow greater informational exchange between nodes
* contains a signature, sequence number and fields detailing the identity scheme used to generate and validate signatures
* key-value pairs contain the node's IP address and information about the sub-protocols the node is able to use
* consensus clients use a specific ENR structure to identify boot nodes


<br>

---

### the JSON-RPC interface

<br>

* interface that allows us to write programs that use an Ethereum client as a gateway to an Ethereum network and blockchain.
* the RPC interface is offered as an HTTP service on port 8545. For security reasons it is restricted, by default, to only accept connections from localhost.

<br>

----

### setting a dedicated hardware

<br>

##### execution client

<br>

* [check estimate of the blockchain size](https://bitinfocharts.com/ethereum/).
* minimum specs:
  - CPU with 4+ cores
  - 16 GB+ RAM
  - fast SSD with at least 1TB free space, up to 12TB+ (bottleneck for your hardware is mostly disk space.
  - interent bandwith ~1.2-1.3 GB download and ~0.9-1 GB upload per hour.


<br>

##### consensus client

<br>

* ~200GB for beacon data.

<br>

##### engine api

<br>

* in order to connect a consensus client, the execution client must generate a jwtsecret:


```
openssl rand -hex 32 > jwtsecret
```

<br>

##### other considerations

<br>

* after downloading a client release and its signature, use some PGP to verify them.
* your router and firewall needs to accept connections on listening ports. By default Ethereum clients use a listener (TCP) port and a discovery (UDP) port, both on 30303 by default.
* execution clients offer RPC API endpoints that you can use to submit transactions, interact with or deploy smart contracts on Ethereum.
* the consensus clients all expose a Beacon API that can be used to check the status of the consensus client or download blocks and consensus data.
* a privacy-preserving way to set up a publicly reachable endpoint is to host the node on your own Tor onion service.

