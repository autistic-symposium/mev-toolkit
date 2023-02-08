## frontrunning 

<br>

### tl, dr

<br>


* frontrunning is the process by which an adversary observes txs on the network layer and then acts upon this information by, for instance, issuing a competing tx, with the hope that this tx is mined before a victim's tx.


* example: transaction A is broadcasted with a higher gas price than an already pending transaction B so that A gets mined before B.


* **generalized frontrunners** are bots that watch the mempool to detect profitable transactions, copy their code, replace addresses with theirs, then submit the modified tx with a higher gas price.

* **specialized frontrunners**, also known as longtails, are covered [here](https://github.com/go-outside-labs/mev-toolkit/tree/main/longtails)

<br>

---

### resources

<br>

* [anatomy of frontrunner bots](https://github.com/go-outside-labs/mev-toolkit/blob/main/anatomy_of_mev_bots/bots/frontrunners.md)
* [shutter frontrunning protection](https://github.com/shutter-network/shutter)

##### cool txs and stories

* [generalized frontrunner copied the exploiter's 4 tx on past 50 blocks](https://twitter.com/bertcmiller/status/1613257826654392320)


##### some history

* [improving frontrunning of x*y=k mm, by vitalik](https://ethresear.ch/t/improving-front-running-resistance-of-x-y-k-market-makers/1281)
* [on cryptokitties `giveBirth()` frontrunning](https://maven11.substack.com/p/modular-mev-part-1the-introduction)
* [bancor ico frontrunning](https://hackingdistributed.com/2017/06/19/bancor-is-flawed/?ref=hackernoon.com)
* [150 lines of python frontrunning bancor](https://hackernoon.com/front-running-bancor-in-150-lines-of-python-with-ethereum-api-d5e2bfd0d798)
