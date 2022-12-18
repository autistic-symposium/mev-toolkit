# Deployment of geth in GCP + docker

In this deployment, we use **Container-Optimized OS** to permit the deployment of a Docker image to a **Google Compute Engine VM**.

This is the simplest way to run the `ethereum/client-go` image. This will install `geth`, the **Golang CLI Ethereum client** for running a full Ethereum node and interacting with Ethereum networks.

---

### Installing

Install [google cloud sdk](https://cloud.google.com/sdk/docs/quickstart) and configure it with:

```
gcloud init
gcloud auth login
gcloud config set project <project name>
```

### Create the instance


```
gcloud beta compute instances create-with-container <docker container alias> \
--boot-disk-size=500GB \
--boot-disk-type=pd-ssd \
--container-image=ethereum/client-go \
--container-arg="--rpc" \
--container-arg="--rpcaddr=0.0.0.0" \
--container-restart-policy=always \
--container-mount-host-path=\
mount-path=/root,\
host-path=/tmp/client-go,\
mode=rw \
--image-family=cos-stable \
--image-project=cos-cloud \
--zone=<which zone?> \
--project=<project name>
```


The instance should be available at the project's [GCP dashboard](https://console.cloud.google.com/compute/instances).


`Geth` needs to have a special CORS setting enabled to allow MetaMask to connect to it by default, so try starting it with this command:

```
geth --rpc --rpccorsdomain="chrome-extension://<hash>"
```

### Start `konlet-startup`

`konlet-startup` is the `systemd` service that corresponds to the docker image deployment in the **Container-Optimized OS**.

Run:

```
gcloud compute ssh <docker container alias>  \
--command="sudo journalctl --unit=konlet-startup --follow" \
--project=<project name>
```

### Confirm that the container is running

```
gcloud compute ssh <docker container alias> \
--command="docker ps --format='[{{.ID}}] {{.Names}}: {{.Status}}'" \
--project=<project name>
```


### SSH and port-forwarding

```
gcloud compute ssh <docker container alias> \
--ssh-flag="-L 8545:localhost:8545" \
--project=<project name>
```

Success looks like:

```
  ########################[ Welcome ]########################
  #  You have logged in to the guest OS.                    #
  #  To access your containers use 'docker attach' command  #
  ###########################################################

<user>@<project name> >
```

### Additional configuration for the intance

* [Alocate a static IP](https://console.cloud.google.com/networking/addresses/).
* [Prevent deletion](https://console.cloud.google.com/compute/instancesDetail/).
* Configure CORS [here]().


----

## Creating the Testnet

The command to create a testnet with `geth` is:

```
geth init --datadir data ./genesis.json

```

and then starting the node:

```
geth --datadir data --networkid NetworkID
```

`NetworkID` helps ensure the privacy of your network. You can use any number and peers joining the network must use the same number.

### Starting the genesis block

Inside the instance, create the `genesis.json` file:

```
vim ~/genesis.json
```
with
```
{
    "config": {
      "chainId": 137,
      "homesteadBlock": 0,
      "eip150Block": 0,
      "eip155Block": 0,
      "eip158Block": 0,
      "byzantiumBlock": 0,
      "constantinopleBlock": 0,
      "petersburgBlock": 0
    },
    "difficulty": "0x400",
    "gasLimit":"0x2100000",
    "alloc": {
        "3282791d6fd713f1e94f4bfd565eaa78b3a0599d": {
          "balance": "1337000000000000000000"
        }
    }
}
```

Start the testnet with:

```
geth --identity <project name> --nodiscover --networkid 137 --datadir ~/data init ~/genesis.json
```

Where `geth` flags are:
  * `--datadir` indicates the data for our local testnet.
  * `--nodiscover`, `--maxpeers 0`, `--rpc`, `--rpcapi` make sure the network is private.





---

## Interacting with the testnet

### Connecting to a member node

From another terminal, run:

```
docker run \
--rm \
--interactive \
--net=host \
--tty \
ethereum/client-go \
  attach http://localhost:8545
```

or

```
geth attach http://localhost:8545
```

Success looks like:

```
Welcome to the Geth JavaScript console!
>
```

### Monitoring

* GCP logs can be found [here](https://console.cloud.google.com/logs).
* To look at the output from the tesnet run:

```
FILTER="resource.type=\"global\" "\
"logName=\"projects/<project-name>/logs/gcplogs-docker-driver\" "

gcloud logging read "${FILTER}" \
--project=<project name> \
--format="value(jsonPayload.data)" \
--order=asc
```

