#!/bin/bash
#
# download and untar the needed archive

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ROOT=$(dirname ${DIR})
MODEL_DIR=${ROOT}/test/resources_efficientdet/models/

function doit() {
  # shitty logging
  echo
  echo "${1} ======================================================"

  HERE=$(pwd)
  cd /tmp
  wget http://download.tensorflow.org/models/object_detection/tf2/20200711/${1}.tar.gz
  tar -xzvf ${1}.tar.gz
  rm ${1}.tar.gz

  mkdir -p ${1}/1
  mv ${1}/saved_model/saved_model.pb ${1}/1
  mv ${1}/saved_model/variables ${1}/1

  rm -r ${1}/checkpoint
  rm -r ${1}/pipeline.config
  rm -r ${1}/saved_model

  cp -r ${1} ${MODEL_DIR}
  rm -r ${1}

  cd $HERE
}

# models in the google model zoo
#  https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md
doit efficientdet_d0_coco17_tpu-32
doit efficientdet_d1_coco17_tpu-32
doit efficientdet_d2_coco17_tpu-32
doit efficientdet_d3_coco17_tpu-32
doit efficientdet_d4_coco17_tpu-32
doit efficientdet_d5_coco17_tpu-32
doit efficientdet_d6_coco17_tpu-32
doit efficientdet_d7_coco17_tpu-32

cd $HERE

exit 0