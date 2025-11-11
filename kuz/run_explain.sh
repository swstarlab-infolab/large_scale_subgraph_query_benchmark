#!/bin/bash

set -eu
set -o pipefail

cd "$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd ..


. kuz/vars.sh
. scripts/import-vars.sh

QUERY_IDS=("7" "8" "9")
# QUERY_IDS=("1" "1-short" "2" "3" "4" "5" "6" "7" "8" "9")
REPEAT_TIMES=1

for QUERY_ID in "${QUERY_IDS[@]}"; do
  python3 kuz/client_explain.py ${SF} ${QUERY_ID} $@
done
