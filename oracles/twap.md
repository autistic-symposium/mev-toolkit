## TWAP oracles

### tl; dr


<br>


---

### oracle attacks

* on pos ethereum, block builder building successive block might be able to manipulate oracles for multi-block MEV extraction.
* with mev-boost, an attacker could observe the set of upcoming proposers. if they finds two successive proposers that have both been proposing blocks, then the attacker can anticipate the attack.


<img width="791" alt="Screen Shot 2022-12-21 at 4 57 12 PM" src="https://user-images.githubusercontent.com/1130416/209031792-52d7671e-480e-497b-9736-4e22e1810fab.png">

___

### resources

* [Multi Block MEV by flashbots](https://collective.flashbots.net/t/multi-block-mev/457/2?u=nerolation)
* [Statistical analysis on Ethereum k-consecutive block proposal](https://alrevuelta.github.io/posts/ethereum-mev-multiblock)
* [uniswap v3 oracles](https://uniswap.org/blog/uniswap-v3-oracles)
