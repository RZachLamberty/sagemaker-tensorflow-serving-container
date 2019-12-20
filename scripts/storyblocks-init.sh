#!/bin/bash
#
# download and untar the needed archive

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ROOT=$(dirname ${DIR})
MODEL_DIR=${ROOT}/test/resources_bertdl/models/

# current model located here
aws s3 cp \
  s3://videoblocks-ml/models/bert-for-download-prediction/bert-output/label-ever/frozen-models/model.tar.gz \
  $MODEL_DIR/

HERE=$(pwd)
cd $MODEL_DIR
tar -xzvf model.tar.gz
rm model.tar.gz

cd $HERE

exit 0