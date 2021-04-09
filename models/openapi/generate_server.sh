#!/usr/bin/env bash

cd `dirname $0`

export IMPULSE_APPS_SERVER_DIR=${PWD}/../../backend
export IMPULSE_APPS_SERVER_PACKAGE_NAME=base
rm -rf ${IMPULSE_APPS_SERVER_DIR}/${IMPULSE_APPS_SERVER_PACKAGE_NAME}

rm -rf generate-server-tmp
mkdir generate-server-tmp

docker run --rm -v ${PWD}:/local \
  openapitools/openapi-generator-cli:v4.3.1 \
  generate \
  -i /local/apps.yaml \
  -g python-flask \
  -o /local/generate-server-tmp \
  -p packageName=base

cp -n -r generate-server-tmp/ ${IMPULSE_APPS_SERVER_DIR}
sed '/^security:/,/^[^ ]*:/!n;/[ ]\{1,\}-[ ]\{1,\}BearerAuth/d'  apps.yaml | sed '/^security/d'  > apps_no_authentication.yaml
docker run --rm -v ${PWD}:/local \
  openapitools/openapi-generator-cli:v4.3.1 \
  generate \
  -i /local/apps_no_authentication.yaml \
  -g python-flask \
  -o /local/generate-server-tmp \
  -p packageName=base

mv generate-server-tmp/${IMPULSE_APPS_SERVER_PACKAGE_NAME}/openapi/openapi.yaml ${IMPULSE_APPS_SERVER_DIR}/${IMPULSE_APPS_SERVER_PACKAGE_NAME}/openapi/openapi_no_authentication.yaml
rm -rf generate-server-tmp
rm apps_no_authentication.yaml