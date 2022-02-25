#!/usr/bin/env bash

set -ex

PORT=${PORT:-18545}

echo "Building local blockchain container"

docker build -t <docker container alias> .

echo "Starting blockchain network on port $PORT (use rpc URL http://localhost:$PORT)"

docker run -it --rm \
    -v $(pwd)/genesis.json:/genesis.json \
    -v $(pwd)/data:/data \
    -p $PORT:8545 \
    <docker container alias>
