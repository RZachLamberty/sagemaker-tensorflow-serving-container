#!/bin/bash
#
# Start a local docker container.

set -euo pipefail

source scripts/shared.sh

parse_std_args "$@"

if [ "$arch" == 'gpu' ]; then
    docker_command='nvidia-docker'
else
    docker_command='docker'
fi


MODEL_DIR="$(cd "test/resources_efficientdet/models" > /dev/null && pwd)"
$docker_command run \
    --rm \
    -v "$MODEL_DIR":/opt/ml/model:ro \
    -p 8080:8080 \
    -e "SAGEMAKER_TFS_DEFAULT_MODEL_NAME=efficientdet_d0_coco17_tpu-32" \
    -e "SAGEMAKER_TFS_NGINX_LOGLEVEL=error" \
    -e "SAGEMAKER_BIND_TO_PORT=8080" \
    -e "SAGEMAKER_SAFE_PORT_RANGE=9000-9999" \
    -e "SAGEMAKER_MODEL_SERVER_TIMEOUT=600" \
    -e "AWS_ACCESS_KEY_ID=AKIAIUYXRK7DUY6HD7GA" \
    -e "AWS_SECRET_ACCESS_KEY=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" \
    $repository:$full_version-$device serve > log.txt 2>&1 &
