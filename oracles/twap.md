## TWAP oracles

### tl; dr


<br>


---

### oracle attacks

* on pos ethereum, block builder building successive block might be able to manipulate oracles for multi-block MEV extraction.
* with mev-boost, an attacker could observe the set of upcoming proposers. if they finds two successive proposers that have both been proposing blocks, then the attacker can anticipate the attack.
___

### resources

* [Multi Block MEV by flashbots](https://collective.flashbots.net/t/multi-block-mev/457/2?u=nerolation)
* [Statistical analysis on Ethereum k-consecutive block proposal](https://alrevuelta.github.io/posts/ethereum-mev-multiblock)
