#!/usr/bin/env bash

set -ex

GETH_DATADIR=${GETH_DATADIR:-"/data"}

geth_init() {
    ls -al "$GETH_DATADIR"

    if [[ -d "$GETH_DATADIR/keystore" ]]; then
        echo "Chain already initialized"
        return 0
    fi

    echo "Initializing using Genesis"
    geth init --datadir "$GETH_DATADIR" /genesis.json
}

geth_custom_start() {
    echo "Starting node with custom arguments $@"
    exec geth $@
}

geth_normal_start() {
    echo "Starting node"
    local identity=${GETH_IDENTITY:-"<docker container alias>"}
    local http_corsdomain=${GETH_HTTP_CORSDOMAIN:-"http://localhost:3000"}
    local http_vhosts=${GETH_HTTP_VHOSTS:-"localhost"}
    local networkid=${GETH_NETWORKID:-"137"}
    local enable_mining=${ENABLING_MINING:-"YES"}

    local mining_args=""
    if [[ "$enable_mining" == "YES" ]]; then
        local miner_etherbase=${GETH_MINER_ETHERBASE:-"<add etherbase>"}
        local miner_threads=${GETH_MINER_THREADS:-1}
        mining_args="$mining_args --mine"
        mining_args="$mining_args --miner.threads $miner_threads"
        mining_args="$mining_args --miner.etherbase $miner_etherbase"
    fi

    exec geth \
        --identity "$identity" \
        --nodiscover \
        --http \
        --http.addr 0.0.0.0 \
        --http.corsdomain "$http_corsdomain" \
        --http.vhosts "$http_vhosts" \
        --networkid "$networkid" \
        --datadir "$GETH_DATADIR" \
        $mining_args \
        "$@"
}

main() {
    local should_initialize=${SHOULD_INITIALIZE:-"YES"}
    local custom_start=${CUSTOM_START:-"NO"}

    if [[ "$should_initialize" == "YES" ]]; then
        geth_init
    fi

    if [[ "$custom_start" == "YES" ]]; then
        geth_custom_start "$@"
    else
        geth_normal_start "$@"
    fi
}

main "$@"
