#!/usr/bin/env bash
set -e

SCRIPT_PATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

minikube start --mount-string="${SCRIPT_PATH}/airflow-data:/host" --mount

echo "Logging into docker registry"
./docker_login.sh

kubectl apply -f mykube/
