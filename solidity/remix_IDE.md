## Remix IDE

Remix IDE is an open source web3 application and it's used for the entire journey of smart contract development.

<br>

<img width="414" alt="Screen Shot 2022-03-10 at 5 57 22 PM" src="https://user-images.githubusercontent.com/1130416/157715032-63dfbe5d-292d-48e3-8594-04902fb008f6.png">


<br>

* Everything in Remix is a plugin. The plugin mamanger is the place to load functionalities and create your own plugins.
* By default, Remix stores files in Workspaces, which are folders in the browser's local storage.
* You can publish all files from current workspace to a gist, using the Gist API.

#### Compiler (Solidity)

* You can compile (and deploy) contracts with versions of Solidity older than 0.4.12. However, the older compilers used a legacy AST.
* The "fork selection" dropdown list allows to compile code against a specific ehtereum hard fork.

#### Optimization

* The optimizer tries to simplify complicated expressions, which reduces both code size and execution cost. It can reduce gas needed for contract deployment as well as for external calls made to the contract.


#### Environment

* `JavaScript VM`: All transactions will be executed in a sandbox blockchain in the browser.
* `Injected Provider`: Metamaask is an example of a profiver that inject web3.
* `Web3 Provider`: Remix will connect to a remote node (you need to provide the URL to the selected provider: geth, parity or any ethereum client)

#### Setup

* Gas Limit: sets the amount of ETH, WEI, GWEI that is sent to ta contract or a payable function.
* Deploy: sends a transaction that deplpys the selected contract.
* atAdress: used to access a contract whtat has already been deployed (does not cost gas).
* To interact with a contract using the ABI, create a new file in Remix, with extension `.abi`.
* The Recorder is a tool used to save a bunch of transactions in a JSON file and rerun them later either in the same environment or in another.
* The Debugger shows the contract's state while stepping through a transaction.
* Using generated sources will make it easier to audit your contracts.
* Static code analysis can be done by a plugin, so that you can examine the code for security vulnerabilities, bad development practices, etc.
* Hardhat integration can be done with `hardhat.config.js` (Hardhat websocket listener should run at `65522`). Hardhat provider is a plugin for Remix IDE.



#### Generate artifacts

When a compilation for a Solidity file succeeds, Remix creates three Json files for each compiled contract, that can be seen in the `File Explorers plugin`:

1. `artifacts/<contractName>.json`: contains links to libraries, the bytecode, gas estimation, the ABI.
2. `articfacts/<contractName_metadata>.json`: contains the metadata from the output of Solidity compilation.
3. `artifcats/build-info/<dynamic_hash>.json`: contains info about `solc` compiler version, compiler input and output.


