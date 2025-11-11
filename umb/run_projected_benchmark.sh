#!/bin/bash

set -eu
set -o pipefail

cd "$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd ..

. umb/vars.sh
. scripts/import-vars.sh

QUERY_IDS=("5")
#QUERY_IDS=("1" "1-short" "2" "3" "4" "5" "6" "7" "8" "9")
REPEAT_TIMES=1
TIMEOUT_DURATION="1h"

./umb/stop-and-rm.sh > /dev/null 2>&1
for QUERY_ID in "${QUERY_IDS[@]}"; do
  for ((i=1; i<=REPEAT_TIMES; i++)); do
    ./umb/start.sh > /dev/null 2>&1
    sync
    sudo sh -c "echo 1 > /proc/sys/vm/drop_caches"
    sudo sh -c "echo 2 > /proc/sys/vm/drop_caches"
    sudo sh -c "echo 3 > /proc/sys/vm/drop_caches"
    
    timeout "${TIMEOUT_DURATION}" python3 pos/client_projected.py ${SF} ${QUERY_ID} $@ || {
      echo "QUERY_ID ${QUERY_ID} timed out after ${TIMEOUT_DURATION}. Moving to next query."
    }
    ./umb/stop-and-rm.sh > /dev/null 2>&1
  done
done
