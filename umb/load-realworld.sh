#!/bin/bash

set -eu
set -o pipefail

cd "$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd ..

. umb/vars.sh
. scripts/import-vars2.sh

mkdir -p ${UMBRA_SQL_SCRATCH_DIR}/
cp ${UMBRA_SQL_DIR}/create-role.sql ${UMBRA_SQL_SCRATCH_DIR}/
cp ${UMBRA_SQL_DIR}/schema3.sql ${UMBRA_SQL_SCRATCH_DIR}/
sed "s|PATHVAR|/data|" ${COMMON_SQL_DIR}/snb-load3-LB${LB}.sql > ${UMBRA_SQL_SCRATCH_DIR}/snb-load3.sql

echo -n "Creating and loading database . . ."
docker run \
    --volume=${UMBRA_DATABASE_DIR}:/var/db/:z \
    --volume=${UMBRA_SQL_SCRATCH_DIR}:/sql/:z \
    --volume=${REALWORLD_DATA_DIR}:/data/:z \
    ${UMBRA_DOCKER_IMAGE} \
    umbra_sql \
    --createdb \
      /var/db/ldbc.db \
      /sql/create-role.sql \
      /sql/schema3.sql \
      /sql/snb-load3.sql
echo " Database created."
