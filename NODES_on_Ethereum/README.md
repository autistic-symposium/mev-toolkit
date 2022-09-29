# 🍄 a pos brave new world

<br>

## in this dir

<br>

* [running nodes / validators](https://github.com/bt3gl-labs/1337_mev_toolkit/blob/main/nodes/running-a-node.md)
* [running nodes / validators (advanced)](https://github.com/bt3gl-labs/1337_mev_toolkit/blob/main/nodes/running-a-node-advanced.md)
* [geth on kubernetes](geth_and_k8s)


<br>

----

## articles

<br>

* [Ethereum Proof-of-Stake Consensus Specifications](https://github.com/ethereum/consensus-specs/tree/dev/specs)
* [Increasing censorship resistance of transactions under proposer/builder separation (PBS), by Vitalik et al](https://notes.ethereum.org/@vbuterin/pbs_censorship_resistance)


<br>

---

## nodes and validators stats

<br>

* [ethereum.org launchpad](https://launchpad.ethereum.org/en/)
* [official beacon chain explorer](https://beaconscan.com/)
* [another beacon chain explorer](https://beaconcha.in/)
* [prater/goerli beacon chain explorer](https://prater.beaconcha.in/)
* [beacon chain validator ratings](https://www.rated.network/)
* [list of nodes as a service](https://ethereumnodes.com/)
* [node watch](https://www.nodewatch.io/)
* [archive node access](https://archivenode.io/)
* [list of nodes as a service](https://ethereum.org/en/developers/docs/nodes-and-clients/nodes-as-a-service/)
* [economics post-merge](https://docs.google.com/spreadsheets/d/15tmPOvOgi3wKxJw7KQJKoUe-uonbYR6HF7u83LR5Mj4/edit#gid=1018097491)


<br>

### consensus layer

* [client diversity vs. prysm usage](https://pools.invis.cloud/)
* [consensus clients comparisons](https://www.slashed.info/)

<br>

### execution layer

* [ethereum mainnet stats](https://ethernodes.org/)
* [execution clients tracker](https://etherscan.io/nodetracker)

<br>

### both layers

* [project sunshine](https://ethsunshine.com/)
* [clients diversity](https://clientdiversity.org/)

<br>

----

## clients

<br>

### execution layer

* [geth](https://geth.ethereum.org/)
* [nethermind](https://nethermind.io/)
* [besu](https://besu.hyperledger.org/en/stable/)
* [erigon](https://github.com/ledgerwatch/erigon)
* [akula](https://akula.app/)
* [execution api specification](https://github.com/ethereum/execution-apis)

<br>

### consensus layer

* [prysm](https://github.com/prysmaticlabs/prysm)
* [lighthouse](https://github.com/sigp/lighthouse)
* [teku](https://github.com/ConsenSys/teku)
* [nimbus](https://nimbus.team/)
* [lodestar](https://lodestar.chainsafe.io/)


<br>

### engine api

* [engine api docs](https://github.com/ethereum/execution-apis/blob/main/src/engine/specification.md)
* [ethereum json-rpc api](https://ethereum.org/en/developers/docs/apis/json-rpc/)

<br>

---


## lexicon

<br>

* **attestation**: at designated times, each validator is responsible for publishing different attestations that formally declare this validator's view of the chain, including the last finalized checkpoint and the current head of the chain.

* **block time**: the time interval between blocks being added to the blockchain.

* **block proposer**: the specific validator chosen to create a block in a particular slot.

* **base fee**: every block's reserve price known. It is the minimum gas fee a user must pay to include a transaction in the next block.

* **LMD-GHOST**: latest message drive greediest heaviest observed subtree, the fork choice rule determining which block is viewed as the current chain head.

* **Casper-FFG**: proof-of-stake consensus protocol used in conjunction with the LMD-GHOST fork choice algorithm to allow consensus clients to agree on the head of the Beacon Chain.

* **Gasper**: Ethereum’s PoS implementation, a combination of the LMD-GHOST fork choice rule, Casper FFG, and the specific reward/penalty scheme.

* **RANDAO**: random number generation scheme used to select block proposers, sort validators into committees, etc.

* **BLS**: cryptographic signature scheme used for validator attestations.

* **inactivity leak**: validators which don’t submit attestations are penalized if the chain stops finalizing.

* **slashing**: validators which maliciously propose or attest to multiple blocks at the same height have their stake reduced.

* **proposer boost**: a modification to LMD-GHOST giving additional weight to blocks proposed earlier in the slot to defend against avalanche attacks, see an explanation of a 7-block reorg in the beacon chain while this update was being rolled out.

* **distributed hash table (DHT)**: data structure containing (key, value) pairs used by Ethereum nodes to identify peers to connect to and determine which protocols to use to communicate.

* **committee**: group of at least 128 validators assigned to validate blocks in each slot. One of the validators in the committee is the aggregator.

* **slots**: a time period of 12 seconds in which a randomly chosen validator has time to proposa a block. 32 seconds = 1 epoch.

* **epoch**: represents 32 slots and takes ~6.4 minutes.

* **deposit contract**: the gateway to ethereum 2.0. It accepts any transaction with a minumum amount of 1 ETH and a valid input data.

* **input data**: also called deposit data, is a user generated, 842 long sequence of characters. it represents the validator pub key and the withdrawal pub key, which were signed with by the validator priv key. the input data needs to be added to the transaction to the deposit contract to be identified by the beacon-chain.

* **unique index**: every validator receives its unique index.

* **finality**: a transaction has "finality" when it's part of a block that can't change without a significant amount of ETH getting burned (this is managed using "checkpoint" blocks).

