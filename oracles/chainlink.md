## chainlink 

<br>

A decentralized oracle network consisting of three key smart contracts:

* a reputation contract: keep track of data providers' performance.
* an order-matching contract: selects bids from oracles using the reputation contract.
* an aggregation contract—and an off-chain registry of data providers.


One of the main challenges with such a decentralized approach is the formulation of the aggregation function. 
ChainLink proposes calculating a weighted response, allowing a validity score to be reported for each oracle response. 
