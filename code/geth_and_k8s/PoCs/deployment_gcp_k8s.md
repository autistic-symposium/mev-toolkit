# Deployment of geth in GCP + Kubernetes

## Deployment

```
NAMESPACE=ethereum
kubectl create namespace ${NAMESPACE}
kubectl apply --filename=deployment.yaml --namespace=${NAMESPACE}
```


## Accessing node without opening firewall


```
SERVICE=ethereum
NAMESPACE=ethereum

NODE=$(\
  kubectl get nodes \
  --output=jsonpath='{.items[0].metadata.name}')

PORT=$(\
  kubectl get services/${SERVICE} \
  --namespace=${NAMESPACE} \
  --output=jsonpath='{.spec.ports[?(@.name=="default")].nodePort}')

echo ${PORT}

gcloud compute ssh snowdevil \
--ssh-flag="-L ${PORT}:localhost:${PORT}" \
--project=shopify-dev
```


## Member connecting

```
docker run \
--rm \
--interactive \
--tty  \
--net=host \
ethereum/client-go attach http://localhost:${PORT}
```

### Dealing with secrets

```
kubectl create secret generic keystore \
--from-file=path/to/keystore \
--namespace=$NAMESPACE
```