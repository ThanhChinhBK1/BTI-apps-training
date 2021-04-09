#!/usr/bin/env bash

cd `dirname $0`

export IMPULSE_APPS_CLIENT_DIR=${PWD}/../../frontend/bti-training-frontend/src/app/services/bti-training-api
rm -rf ${IMPULSE_APPS_CLIENT_DIR}

rm -rf generate-client-tmp
mkdir generate-client-tmp

docker run --rm -v ${PWD}:/local \
  openapitools/openapi-generator-cli:v4.3.1 \
  generate \
  -i /local/apps.yaml \
  -g typescript-angular \
  -o /local/generate-client-tmp \
  --additional-properties="apiModulePrefix=ImpulseApps"


mv generate-client-tmp ${IMPULSE_APPS_CLIENT_DIR}

rm -rf generate-client-tmp