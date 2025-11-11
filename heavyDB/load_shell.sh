 #!/usr/bin/env bash

MAPD_TCP_PORT=${MAPD_TCP_PORT:=6274}

echo "- adding schema"
/opt/heavyai/bin/heavysql heavyai -u admin -p HyperInteractive --port "$MAPD_TCP_PORT" < /var/lib/heavyai/LSQB/LSQB_schema.sql

csv_files=(/var/lib/heavyai/LSQB/sf${SF}/*csv)

csv_count=${#csv_files[@]}

if [ "$csv_count" -eq 0 ]; then
  echo "ERROR"
  exit 1
fi

for csv in "${csv_files[@]}"; do
  table=$(basename "$csv" .csv)

  echo "${table}: ${csv}"
  echo "copy $table from '${csv}' with (delimiter='|', quoted='true');" | /opt/heavyai/bin/heavysql heavyai -u admin -p HyperInteractive --port "$MAPD_TCP_PORT"
done
