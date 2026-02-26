#!/bin/sh
set -e
echo "Deploying LogiSafe to Kubernetes"

kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

echo "Deployment triggered successfully"
