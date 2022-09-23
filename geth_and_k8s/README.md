# [experiment] deploy a private ethereum blockchain on kubernetes

<br>

### tl;dr

<br>

* deploy it with your own [geth](https://geth.ethereum.org/) and a customized genesis file and all.

* geth implements [Clique](https://eips.ethereum.org/EIPS/eip-225#:~:text=Clique%20is%20a%20proof%2Dof,any%20client%20with%20minimal%20effort.), a proof-of-authority mechanism to reach consensus. Moreover, a number of accounts a defined to produce new blocks in the chain.

* a custom Ethereum testnet contains three components:
      * a custom [genesis file](/genesis.json
      * a custom data directory, which we define with `GETH_DATADIR`
      * a custom `NetworkID` , which we set `137`

<br>

---

<br>

### documentation for this work

<br>

* [genesis block explanation](https://github.com/bt3gl-labs/1337_mev_toolkit/blob/main/geth_and_k8s/genesis_block_explanation.md)
* [deployment on gcp and docker](https://github.com/bt3gl-labs/1337_mev_toolkit/blob/main/geth_and_k8s/deployment_gcp_docker.md)
* [deployment of geth in gcp + kubernetex](https://github.com/bt3gl-labs/1337_mev_toolkit/blob/main/geth_and_k8s/deployment_gcp_k8s.md)
* [running a node in ethereum with geth](https://github.com/bt3gl-labs/1337_mev_toolkit/blob/main/geth_and_k8s/running-a-node-geth.md)
* [geth creation commands](https://github.com/bt3gl-labs/1337_mev_toolkit/blob/main/geth_and_k8s/geth_creation_commands.md)

<br>

---

<br>

### nodes

<br>

* running nodes are responsible for the following tasks:
     - store blockchain data,
     - participates in block validation (verifying blocks and states),
     - serve the network and provides data on request.


* interacting with the client:

<br>


##### getting total coinbase

```bash
web3.fromWei(eth.getBalance(eth.coinbase), "ether")
```



##### getting a balance from an account

```bash
web3.fromWei(eth.getBalance("2ee8D80de1c389f1254e94bc44D2d1Bc391eD402"), "ether")
```


##### txpool api

* access to several non-standard RPC methods to inspect the contents of the transaction pool containing all the currently pending transactions as well as the ones queued for future processing:

```bash
txpool
```


##### useful checks

```bash
admin.nodeInfo
```



##### setting this chain on metamask



* click a `custom RPC` network and add:

```bash
Network Name: "<project name>"
New RPC URL: localhost
Chain ID: 137
```

<br>

---

<br>

### references

* [geth commands](https://geth.ethereum.org/docs/interface/command-line-options)

