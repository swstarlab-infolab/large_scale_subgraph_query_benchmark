#!/bin/bash

set -eu
set -o pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 <graph_name>"
  exit 1
fi

graph_name="$1" 

cd "$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd ${PEREGRINE_PATH}/Peregrine


QUERY_IDS=("1" "2" "3" "4" "5")
REPEAT_TIMES=1
TIMEOUT=3650

for QUERY_ID in ${QUERY_IDS[@]}; do
  for ((i=1; i<=REPEAT_TIMES; i++)); do
    sync
    sudo sh -c "echo 1 > /proc/sys/vm/drop_caches"
    sudo sh -c "echo 2 > /proc/sys/vm/drop_caches"
    sudo sh -c "echo 3 > /proc/sys/vm/drop_caches"

    grid_dir="${RAW_DATASET_PATH}/Peregrine/GraphData/${graph_name}"
    query="./query/LBX_q${QUERY_ID}.graph"
    num_threads=64

    output=$( { /usr/bin/time -f "%e" timeout $TIMEOUT ./bin/count "$grid_dir" "$query" "$num_threads"; } 2>&1 || echo "timeout" )
    
    if [[ "$output" == *"timeout"* ]]; then
      echo "${QUERY_ID} | timeout | timeout"
      continue
    fi

    total_counter=$(echo "$output" | grep -oP '\]:\s*\K[0-9]+')

    query_elapsed_time=$(echo "$output" | tail -n1)

    echo "${QUERY_ID} | ${graph_name} | ${total_counter} | ${query_elapsed_time}"
  done
done
