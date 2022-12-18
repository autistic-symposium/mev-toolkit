FROM ethereum/client-go:stable

RUN apk add --no-cache bash

COPY entrypoint.sh /entrypoint.sh
COPY genesis.json /genesis.json

ENTRYPOINT /entrypoint.sh
