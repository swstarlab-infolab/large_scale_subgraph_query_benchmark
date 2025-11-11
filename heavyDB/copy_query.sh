#!/bin/bash

cd "$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd ..

cp ./heavyDB/query/* ${RAW_DATASET_PATH}/heavyai/realworld/query
