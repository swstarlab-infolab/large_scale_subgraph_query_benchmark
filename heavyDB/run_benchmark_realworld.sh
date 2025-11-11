#!/bin/bash

MAPD_TCP_PORT=${MAPD_TCP_PORT:=6274}
TIMEOUT_DURATION="1h"

QUERY_IDS=("1" "2" "3" "4" "5")
QUERY_DIR="/var/lib/heavyai/realworld/query"

for QUERY_ID in "${QUERY_IDS[@]}"; do
  
  if [ "$LB" -eq 1 ]; then
    QUERY_FILE="${QUERY_DIR}/realworld-unlabeled-q${QUERY_ID}.sql"
  else
    QUERY_FILE="${QUERY_DIR}/realworld-labeled-q${QUERY_ID}.sql"
  fi
  echo "Executing query from: $QUERY_FILE"
  docker restart 9ab

  sleep 10

  START_TIME=$(date +%s%N)

  docker exec -it 9ab timeout $TIMEOUT_DURATION bash -c "cat \"$QUERY_FILE\" | /opt/heavyai/bin/heavysql heavyai -u admin -p HyperInteractive --port \"$MAPD_TCP_PORT\"" || {
    echo "TIMEOUT"
  }

  END_TIME=$(date +%s%N)

  ELAPSED_SECONDS=$(( (END_TIME - START_TIME) / 1000000000 ))
  ELAPSED_MILLISECONDS=$(( (END_TIME - START_TIME) / 1000000 % 1000 ))
  echo "time: $ELAPSED_SECONDS.$ELAPSED_MILLISECONDS sec"
done
