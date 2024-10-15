## TWAP oracles

### tl; dr


<br>

* an asset’s time-weighted average price (TWAP) is the measure of an asset’s average price over a predetermined period of time (any specified duration).
* TWAP trading algorithms seek to optimize average price while executing over a specified time period. 
* generally used to execute large orders that are expected to have significant market impact.

<br>

---

### tl; dr oracle attacks 


<br>

* on pos ethereum, block builder building successive block might be able to manipulate oracles for multi-block MEV extraction, as proposers know one epoch (32 blocks or 6 minutes and 24 seconds) ahead if they are the next block proposer.
* with mev-boost, an attacker could observe the set of upcoming proposers. if they finds two successive proposers that have both been proposing blocks, then the attacker can anticipate the attack.
* a potential attack vector is on lending protocols, where an attacker can borrow assets that are immediately undercollateralized.


<img width="791" src="https://user-images.githubusercontent.com/1130416/209031792-52d7671e-480e-497b-9736-4e22e1810fab.png">

<br>

___

### resources

* [multi- block MEV by flashbots](https://collective.flashbots.net/t/multi-block-mev/457/2?u=nerolation)
* [statistical analysis on ethereum k-consecutive block proposal](https://alrevuelta.github.io/posts/ethereum-mev-multiblock)
* [uniswap v3 twap oracles](https://uniswap.org/blog/uniswap-v3-oracles)
* [multi-block mev, by chainsecurity](https://chainsecurity.com/oracle-manipulation-after-merge/)
