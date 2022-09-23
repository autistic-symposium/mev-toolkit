# 🍄 a pos brave new world

<br>


## resources

<br>

* [Ethereum Proof-of-Stake Consensus Specifications](https://github.com/ethereum/consensus-specs/tree/dev/specs)
* [Increasing censorship resistance of transactions under proposer/builder separation (PBS), by Vitalik et al](https://notes.ethereum.org/@vbuterin/pbs_censorship_resistance)


<br>

---

## tools 

<br>


### validators

* [official beacon chain explorer](https://beaconscan.com/)
* [another beacon chain explorer](https://prater.beaconcha.in/)
* [beacon chain validator ratings](https://www.rated.network/)
* [list of nodes as a service](https://ethereumnodes.com/)

<br>

### client stats

* [clients diversity](https://clientdiversity.org/)
* [ethereum mainnet stats](https://ethernodes.org/)
* [client diversity vs. prysm usage](https://pools.invis.cloud/)
* [consensus clients comparisons](https://www.slashed.info/)


<br>

### execution clients

* [geth]()
* [nethermind]()
* [besu]()
* [erigon]()
* [akula]()

<br>

### consensus clients

* [prysm](https://github.com/prysmaticlabs/prysm)
* [lighthouse](https://github.com/sigp/lighthouse)
* [teku](https://github.com/ConsenSys/teku)
* [nimbus]()
* [lodestar]()


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




