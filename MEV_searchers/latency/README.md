## latency

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


### cool resources

<br>

* **[mev-boost+ latency notes](https://hackmd.io/@layr/SkBRqvdC5#Latency)**
* **[manifold's openmev latency benchmarking](https://docs.openmev.org/technical-reference/benchmarking)**
* **[defining the latencies involved in mev strategies, by taker](https://mirror.xyz/0x00000a2A02540A0D92e209F9f5F7e104745e06Ba/uYOelwkLc4K7nlo5XV_zpuqsV6MwIMMp-py4e-u4qnE)**
* **[latency is money, by data always](https://hackmd.io/@dataalways/latency-is-money)**
