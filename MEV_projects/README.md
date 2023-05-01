## projects and research

<br>

### tl; dr

<br>


* public discussion around MEV started by [pmcgooohan](https://twitter.com/pmcgoohancrypto?lang=en) on [e/ethereum](https://www.reddit.com/r/ethereum/comments/2d84yv/miners_frontrunning/), and it was formalized by [phildaiann et. al](https://twitter.com/phildaian)'s paper [flash boys 2](https://arxiv.org/abs/1904.05234). [here are the main essays and papers from the last years](history.md).

<br>

----

### what's the future of mev rewards?

<br>

here are some ideas (and below are some of the projects working on specific problems and solutions):

<br>

#### mev burning

* instead of having to deal with certain centralized actors, the network would put in place mechanism to burn mev (inspired by the burn mechanism found within EIP-1559).
* targets the centralizing potential that mev can have on validators, but removing the economic incentives of mev for validators.
* in this [ethresear.ch](https://ethresear.ch/t/burning-mev-through-block-proposer-auctions/14029/11) discussion, domothy recommends implementing an auction for the "right to build a block" on the network (happening at the validator level). network’s slot times would change from 12 seconds to 16 seconds to allow for the period of bidding on block proposal rights.

<br>

#### mev smoothing

* in this [ethresear.ch](https://ethresear.ch/t/committee-driven-mev-smoothing/10408) and [this](https://notes.ethereum.org/cA3EzpNvRBStk1JFLzW8qg), francesco propose "Smoothing MEV means reducing the variance in the MEV that is captured by each validator, with the ultimate goal of getting the distribution of rewards for each validator to be as close as possible to uniform: a staker would then get a share of rewards proportional to their stake, just like with issuance."
* while smoothing is not available as an in-protocol ethereum, the general principle can be seen via smoothing liquid staking pools. rocketpool operates a [voluntary smoothing pool](https://docs.rocketpool.net/guides/node/fee-distrib-sp.html#initializing-the-fee-distributor) see also [eigenlayer discussions](https://twitter.com/sreeramkannan/status/1561736268005814273). [mev-share from flashbots](https://github.com/go-outside-labs/mev-toolkit/tree/main/MEV_projects/flashbots) has also introduced a proposal for programmable provate orderflow that rewards users (through a matchmaking protocol between users and searchers).

<br>

#### mev sharing

* while MEV smoothing/burning focuses on the end of the MEV supply chain and interactions between block builders and validators, mev sharing is in the beginning of the supply chain, for example with block builders that provide rebates (e.g. wallet-boost from blocknative).

<br>

####


<br>

---

### mev-related projects

<br>

* [flashbots](flashbots)
* [manifold](manifold)
* [shutter](shutter)
* [dflow](dflow)
* [eden](eden)
* [jito](jito)
* [skip](skip)
* [cow](cow_protocol)


<br>

---

### resources

<br>

* [quantification of mev sharing designs (ofas), by danning sui](https://docs.google.com/presentation/d/1_pKKkUr_D-OvR2Kah56B0C0LYdO6zMECftBA_q7bM2c/edit#slide=id.g21fe09f5970_0_325)
* [projects addressing private order flows primitives](https://github.com/go-outside-labs/mev-toolkit/blob/main/MEV_searchers/private_order_flows/projects.md)
* [diamonds are forever, lvr is not, by mcmenamin et al.](https://arxiv.org/abs/2210.10601)
* [mev capturing amm, by josojo](https://ethresear.ch/t/mev-capturing-amm-mcamm/13336)
* [mev-protected cross-chain swaps, by cashmere](https://cashmerelabs.medium.com/cashmerelabs-testnet-1-0-2c11e23f36)
