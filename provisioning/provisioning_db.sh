#!/usr/bin/env bash
export FWDIR="$(cd "`dirname "$0"`"; pwd)"
export CASSANDRA_HOST=${CASSANDRA_HOST:-localhost}
export TENANT_NAME=${TENANT_NAME:-impulse}
export ENV_NAME=${ENV_NAME:-dev}
export KEYSPACE=${TENANT_NAME}_${ENV_NAME}
export REPLICATION_CLASS=${REPLICATION_CLASS:-SimpleStrategy}
export REPLICATION_FACTOR=${REPLICATION_FACTOR:-1}
export CQL_OPTION=${CQL_OPTION: }
for file in ${FWDIR}/*.sql; do
    cqlsh ${CQL_OPTION} ${CASSANDRA_HOST} -k ${KEYSPACE} -f "$file" --cqlversion="3.4.4"
done
echo "End execution."