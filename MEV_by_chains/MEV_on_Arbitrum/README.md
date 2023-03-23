## mev on arbitrum

<br>

### tl; dr

<br>

* avm architecture: arbitrum is fully compatible with the evm, but it also has its vm called arbitrum virtual machine:
  * execution flow and structure: arbitrum has an operating system and its core called arbos, which ensures the solitary existence, optimal performance and efficient analytics of smart contracts.
  * dispute settlement speed: the avm has a custom protocol for dispute management, so that it can be acquired out on a standard vm.
  * natives tuples: the avm uses tuples to define and references types in its merkle tree. the tuples can be referenced in looking up the merkle root of any tx on the evm merkle tree. 
* optimistic rollup, with no mempool for bots to frontrun
* currently has a centralized sequencer and whitelisted proof validation while having upgradable contracts
* faster tx processing: ethereum is operating under 15-20 tps, while the arbitrum network can process ~40 tps
* lower tx fees: in ethereum, a significant percentage of validators need to confirm the genuineness of a tx; arbitrum average fee is $~.2 compared to $6.5 (source: [nansen](https://pro.nansen.ai/multichain/eth-vs-arbitrum))
 
<br>

----

### in this dir

<br>

* [gmx and glp vaults](gmx)
* [fair order sequencing](fair_ordering_sequencing)

<br>

---

### resources

<br>

* [transaction ordering policy](https://research.arbitrum.io/t/transaction-ordering-policy/127)
* [arbitrum bridge tutorial](https://arbitrum.io/bridge-tutorial/)
* [arbitrum gas fee, by dune](https://dune.com/blog/fueling-gas-spells-arbitrum)
* [time boost: a new tx ordering policy proposal](https://research.arbitrum.io/t/time-boost-a-new-transaction-ordering-policy-proposal/8173)
