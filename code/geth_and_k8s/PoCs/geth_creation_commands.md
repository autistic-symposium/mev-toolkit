# geth creation commands


### Create a miner account

This will generate a public/private key pair. By default, keys are stored inside, `<datadir>/keystore`. Everything `geth` persists gets written inside `<datadir>`.

The following command returns a private testnet address (which should be saved together with the password):

```
geth account new --datadir /path/to/data
```

### Start mining

With `NetworkID`:

```
geth --mine --rpc --networkid NetworkID --datadir /path/to/data
```

Start mining:

```
> miner.start()
```

To end mining, type:

```
> miner.stop()
```



### Pre-fund the account

Deploying contracts or making transactions requires test ether, which has no value and can be acquired for free from several "faucets".

The command `geth removedb` deletes the locally synced blockchain data of the public testnet (i.e., resyncs with the chain).

To add magic ether, remove the created blockchain database:

```
geth removedb --datadir /path/to/data
```

Modify `genesis.json` as necessary, including multiple accounts in the seed if wanted.

Finally, re-initialize the genesis block:

```
geth --identity <project name> --nodiscover --networkid 1337 --datadir /path/to/data init /path/to/genesis.json
```

### Create new accounts

```
geth --datadir . account new
```

### List accounts

```
geth --datadir . account list
```


### Connect to the testnet

```
geth attach
```

You will enter into the **Geth Javascript console**, where you can run JavaScript code.
