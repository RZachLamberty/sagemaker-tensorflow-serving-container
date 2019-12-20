#!/bin/bash
#
# Some example curl requests to try on local docker containers.

echo "text/csv test"
curl -X POST \
  --data-binary @test/resources_bertdl/inputs/couple_getting_married.inputs.csv \
  -H 'Content-Type: text/csv' \
  -H 'X-Amzn-SageMaker-Custom-Attributes: tfs-model-name=bert-dl' \
  http://localhost:8080/invocations

echo ""
echo "application/json test"
curl -X POST \
  --data-binary @test/resources_bertdl/inputs/couple_getting_married.inputs.json \
  -H 'Content-Type: application/json' \
  -H 'X-Amzn-SageMaker-Custom-Attributes: tfs-model-name=bert-dl' \
  http://localhost:8080/invocations