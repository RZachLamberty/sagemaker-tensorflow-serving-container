#!/bin/bash
#
# Some example curl requests to try on local docker containers.

echo "model: d0"
echo "Content-Type: text/csv"
echo "Accept: application/json"
curl -X POST \
  --data 'videoblocks-ml/data/object-detection-research/videoblocks/dev/sampled-items/jpg/fps-method-01/000000296/000015-0.5005.jpg' \
  -H 'Content-Type: text/csv' \
  -H 'X-Amzn-SageMaker-Custom-Attributes: tfs-model-name=efficientdet_d0_coco17_tpu-32' \
  http://localhost:8080/invocations