#!/bin/bash

set -eu
set -o pipefail

cd "$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd ..

. umb/vars.sh
. scripts/import-vars.sh

mkdir -p ${UMBRA_SQL_SCRATCH_DIR}/
cp ${UMBRA_SQL_DIR}/create-role.sql ${UMBRA_SQL_SCRATCH_DIR}/
cp ${UMBRA_SQL_DIR}/schema2.sql ${UMBRA_SQL_SCRATCH_DIR}/
cp ${COMMON_SQL_DIR}/views2.sql ${UMBRA_SQL_SCRATCH_DIR}/
sed "s|PATHVAR|/data|" ${COMMON_SQL_DIR}/snb-load2.sql > ${UMBRA_SQL_SCRATCH_DIR}/snb-load2.sql

echo -n "Creating and loading database . . ."
docker run \
    --volume=${UMBRA_DATABASE_DIR}:/var/db/:z \
    --volume=${UMBRA_SQL_SCRATCH_DIR}:/sql/:z \
    --volume=${IMPORT_DATA_DIR_PROJECTED_FK}:/data/:z \
    ${UMBRA_DOCKER_IMAGE} \
    umbra_sql \
    --createdb \
      /var/db/ldbc.db \
      /sql/create-role.sql \
      /sql/schema2.sql \
      /sql/views2.sql \
      /sql/snb-load2.sql
echo " Database created."
