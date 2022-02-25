# Creating an Ethereum blockchain

To create this blockchaon, we use [geth](https://geth.ethereum.org/), the official client software provided by the Ethereum Foundation written in the Golang.

By default, geth implements [Clique](https://eips.ethereum.org/EIPS/eip-225#:~:text=Clique%20is%20a%20proof%2Dof,any%20client%20with%20minimal%20effort.), a proof-of-authority mechanism to reach consensus. Moreover, a number of accounts a defined to produce new blocks in the chain.

A custom Ethereum testnet contains three components:

* a custom [genesis file](/genesis.json
* a custom data directory, which we define with `GETH_DATADIR`
* a custom `NetworkID` , which we set `137`


### Gas

Gas refers to the unit that measures the computational effort required to execute specific operations on the Ethereum network.

### Nodes

Running nodes are responsible for the following tasks:

- store blockchain data,
- participates in block validation (verifying blocks and states),
- serve the network and provides data on request.

### Storage

More details to be added soon.

### Faucet

More details to be added soon.

---

## Interacting with the client


You can run commands directly in the console:


##### Getting total coinbase

```
> web3.fromWei(eth.getBalance(eth.coinbase), "ether")
```

##### Getting a balance from an account

```
> web3.fromWei(eth.getBalance("2ee8D80de1c389f1254e94bc44D2d1Bc391eD402"), "ether")
```
#### txpool API

Access to several non-standard RPC methods to inspect the contents of the transaction pool containing all the currently pending transactions as well as the ones queued for future processing:

```
txpool
```

#### Other useful checks

```
admin.nodeInfo
```



### Setting this chain on MetaMask

Click a `Custom RPC` network and add:

```
Network Name: "<project name>"
New RPC URL: localhost
Chain ID: 137
```

---

## References

* [geth commands](https://geth.ethereum.org/docs/interface/command-line-options)

