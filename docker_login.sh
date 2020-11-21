#!/usr/bin/env bash

DEFAULT_SERVER="https://hub.docker.com/"
DEFAULT_USERNAME="${USER}"

read -p "Server[${DEFAULT_SERVER}]:" SERVER
if [ -z "${SERVER}" ]
then
  SERVER=${DEFAULT_SERVER}
fi

read -p "Username[${DEFAULT_USERNAME}]:" USERNAME
if [ -z "${USERNAME}" ]
then
  USERNAME=${DEFAULT_USERNAME}
fi

read -p "Email:" EMAIL
if [ -z "${EMAIL}" ]
then
  >&2 echo "ERROR: Email is required"
  exit 1
fi

read -p "Password:" -s PASSWORD
if [ -z "${PASSWORD}" ]
then
  >&2 echo "ERROR: Password is required"
  exit 1
fi

kubectl create secret docker-registry hub-docker-com \
  --docker-server="${SERVER}" \
  --docker-username=${USERNAME} \
  --docker-password="${PASSWORD}" \
  --docker-email="${EMAIL}"
