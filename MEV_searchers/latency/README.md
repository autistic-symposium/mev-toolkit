## latency optimization

<br>

### tl; dr

<br>


#### builders

* builders might delay before proposing a full block to maximize the amount of potential mev for inclusion in the block. this requires extremely low latency for proposing blocks and views of the mempool.

<br>

#### searcher

##### compute latency

* transaction parsing and filtering
* simulation


##### transport latency

* sending bundles to builder
* builder rate limits


##### searcher responses

* proprietary compute improvements
* bundle timing in slot periods
* co-locate with builder (searching in the same region, etc.)

<br>


---


### resources

<br>


* [web3-toolkit-yul](https://github.com/go-outside-labs/web3-toolkit-yul/blob/main/README.md)
* [mev-boost+ latency notes](https://hackmd.io/@layr/SkBRqvdC5#Latency)
* [manifold's openmev latency benchmarking](https://docs.openmev.org/technical-reference/benchmarking)
