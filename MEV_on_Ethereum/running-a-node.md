## 🌭 running a node

<br>

* [check my step-by-step article to run validator](https://mirror.xyz/steinkirch.eth/F5PI4eqShKTGlx0GzL0Lq0-vHQ6b14OoV4ylE2FMsAc)


#### how a node creates a block is created in ethereum:

    1. the validator client requests a block from the consensus node
    2. the consensus node requests an execution payload from the execution node and incorporates it into the block
    3. the validator client signs the block
    4. the validator client sends the signed block to the consensus node
    5. the consensus node broadcasts the signed block to the network

<br>

#### how does mev affect block times:
    1. the validator client requests a block without transactions (blinded block) from the consesnsus node
    2. the consensus node queries multiple MEV relays for best bid, incorporating the best block into the returned binded blocl
    3. the validator client signs the binded block
    4. the validator client requests the consensus node to unblind and broadcast the signed block
    5. the consensus node requests the winning MEV relay to unblind the singed block and broadcasts it to the network


<br>

----

### infrastructure


<br>

#### solo staking 

<br>

* [eth docker](https://eth-docker.net/docs/About/Overview)
* [stereum solo node infra](https://stereum.net/ethereum-node-setup/)
* [staking deposit cli](https://github.com/ethereum/staking-deposit-cli)
* [ethereum staking guides](https://github.com/SomerEsat/ethereum-staking-guides)

<br>

#### pool staking

<br>

* [stakewise](https://app.stakewise.io/)
* [rocketpool](https://rocketpool.net/)
* [lido](https://lido.fi/)
* [stafi.io](https://www.stafi.io/)
* [nice node](https://www.nicenode.xyz/)
* [ankr](https://www.ankr.com/)
* [stakefish](https://v1.stake.fish/)

<br>

#### staking as a service

<br>


* [alchemy](https://www.alchemy.com/)
* [infura](https://infura.io/)
* [kaleido](https://www.kaleido.io/)
* [moralis](https://moralis.io/)
* [nownodes](https://nownodes.io/)
* [pokt](https://www.pokt.network/)
* [watchdata](https://www.watchdata.io/)
* [zmok](https://zmok.io/)
* [quicknode](https://www.quicknode.com/)
* [rivt](https://rivet.cloud/)
* [sensei](https://www.senseinode.com/)
* [settlemint](https://console.settlemint.com/)
* [blockdaemon](https://blockdaemon.com/)
* [chainstack](https://chainstack.com/)
* [figment](https://datahub.figment.io/)
* [getblock](https://getblock.io/)
* [infstones](https://infstones.com/)

<br>



-----

### light nodes

<br>


* [running a light node with geth](https://ethereum.org/en/developers/tutorials/run-light-node-geth/)
* [ethereum arm docs](https://ethereum-on-arm-documentation.readthedocs.io/en/latest/)

<br>


----


### testnets

<br>

##### goerli

<br>

* [goerli launchpad](https://goerli.launchpad.ethereum.org/en/)
* [run a node on goerli/prater](https://notes.ethereum.org/@launchpad/goerli)
* [guide to join the goerli/prater (besu/teku)](https://github.com/remyroy/ethstaker/blob/main/merge-goerli-prater.md)
* [staking guide for goerli/parter (lighthouse)](https://agstakingco.gitbook.io/eth-2-0-staking-guide-prater-lighthouse/)
* [goerli testnet staking guides](https://github.com/SomerEsat/ethereum-staking-guides#goerli-testnet-staking-guides)
* [goerli testnet (geth/prysm)](https://kb.beaconcha.in/archive/eth1-infura)
* [how to create a merge testnet](https://notes.ethereum.org/@parithosh/H1MSKgm3F)

<br>

##### kiln

<br>

* [kiln launchpad](https://notes.ethereum.org/@launchpad/kiln) (and [here](https://kiln.launchpad.ethereum.org/en/))
* [running kiln testnet on a rasp pi 4](https://ethereum.org/en/developers/tutorials/run-node-raspberry-pi/)


<br>

----

### plug and play solutions

<br>

* [dappnode](https://dappnode.io/en-us/collections/frontpage)
* [avado](https://ava.do/)


<br>


----

### monitoring

<br>

* [guide to monitor a validator](https://github.com/remyroy/ethstaker/blob/main/monitoring.md)
* [guide to alerting a validator](https://github.com/remyroy/ethstaker/blob/main/alerting.md)

<br>

---

### other useful resources

<br>

* [ethereum.org official page on becoming a validator](https://launchpad.ethereum.org/en/overview)
* [ethereum.org official page on running a node](https://ethereum.org/en/run-a-node/)
* [how to setup a validator for eth staking guide](https://www.coincashew.com/coins/overview-eth/guide-or-how-to-setup-a-validator-on-eth2-mainnet)
* [ethub docs on running a node](https://docs.ethhub.io/using-ethereum/running-an-ethereum-node/)
* [validator key generator](https://wagyu.gg/)
* [jwt decoder](https://jwt.io/)
* [eth staker community](https://ethstaker.cc/)
* [cli for managing tasks](https://github.com/wealdtech/ethdo)
