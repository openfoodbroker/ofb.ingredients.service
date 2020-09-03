#!/bin/bash

set -ex

PRODUCT="ofb.ingredients.service"
PRODUCT_IMAGE=$PRODUCT

docker rm -f $PRODUCT || true
docker rmi -f $PRODUCT_IMAGE || true

FLASK_PORT=5000
HOST_PORT=8081

docker build -t $PRODUCT_IMAGE .
docker run -it -e STAGE=dev --name $PRODUCT -p $HOST_PORT:$FLASK_PORT $PRODUCT_IMAGE