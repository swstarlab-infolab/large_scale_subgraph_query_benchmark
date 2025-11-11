#!/bin/bash

set -eu
set -o pipefail

cd "$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd ..

. umb/vars.sh
. scripts/import-vars2.sh

QUERY_IDS=("2" "5")
REPEAT_TIMES=1
TIMEOUT_DURATION="1h"

./umb/stop-and-rm.sh > /dev/null 2>&1
for QUERY_ID in "${QUERY_IDS[@]}"; do
  echo start $QUERY_ID
  for ((i=1; i<=REPEAT_TIMES; i++)); do
    ./umb/start.sh > /dev/null 2>&1
    sync
    sudo sh -c "echo 1 > /proc/sys/vm/drop_caches"
    sudo sh -c "echo 2 > /proc/sys/vm/drop_caches"
    sudo sh -c "echo 3 > /proc/sys/vm/drop_caches"
    
    timeout "${TIMEOUT_DURATION}" python3 pos/client_realworld.py ${LB} ${DATASET} ${QUERY_ID} $@ || {
      echo "QUERY_ID ${QUERY_ID} timed out after ${TIMEOUT_DURATION}. Moving to next query."
      sleep 20
    }
    ./umb/stop-and-rm.sh > /dev/null 2>&1
  done
done
