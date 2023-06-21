## ERC-4337: account abstraction

<br>

### tl; dr

<br>

* this change implements censorship-resistant account abstraction without making any changes to the consensus layer of ethereum, by creating a new mempool, a smart contract wallet standard, and a shared entry point contract for managing user operations.
* this enables wallets to have multi-sigs, social recovery, hardware enclaves, etc.
* **UserOperations** are pseudo-transactions objects that represent a user's intent.
* **Bundlers** are new actors that are either block builders, or users that can send transactions to block builders through a bundle marketplace. they package up a set of objects into a tx making a call to a special contract and sending objects to a separate mempool.
* the **EntryPoint** is a smart contract that receives **UserOperations** from **Bundlers**.
* Aggregators combines multiple signatures into a single signature, to validate multiple **UserOperatons** in one step.
* **Smart contract account** are the target of the **UserOperation** and will validate and execute the **UserOperation**.
* **Paymaster** create flexibility for how gas is paid and by whom.

<br>

### resources

<br>

* **[erc-4337 is on mainnet](https://twitter.com/erc4337/status/1631087958949531648)**
* **[account abstraction, by safe](https://safe.mirror.xyz/9KmZjEbFkmI79s28d9xar6JWYrE50F5AHpa5CR12YGI)**
* **[erc-4337 contract deployment](https://etherscan.io/address/0x0576a174D229E3cFA37253523E645A78A0C91B57#code)**
* **[unpacking erc-4337, by a. chiplunkar](https://frontier.tech/unpacking-erc-4337)**
* **[account abstraction series, by alchemy](https://www.alchemy.com/blog/account-abstraction)**
* **[erc-4337 bundler implementation in rust](https://github.com/Vid201/aa-bundler)**
* **[erc-4337: account abstraction using alt mempool](https://eips.ethereum.org/EIPS/eip-4337)**
* **[account abstraction gas benchmakrs, by eth-infinitism](https://github.com/eth-infinitism/account-abstraction/blob/develop/reports/gas-checker.txt)**


<br>

###### protocols that don't use erc-4337

<br>

* [gnosis safe](https://safe.global/)
* [avocado](https://avocado.instadapp.io/)


