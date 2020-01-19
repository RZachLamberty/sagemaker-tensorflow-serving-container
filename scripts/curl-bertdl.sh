#!/bin/bash
#
# Some example curl requests to try on local docker containers.

echo "Content-Type: application/json"
echo "Accept: application/json"
curl -X POST \
  --data-binary @test/resources_bertdl/inputs/couple_getting_married.inputs.json \
  -H 'Content-Type: application/json' \
  -H 'X-Amzn-SageMaker-Custom-Attributes: tfs-model-name=bert-dl' \
  http://localhost:8080/invocations

echo ""
echo "Content-Type: text/csv"
echo "Accept: application/json"
curl -X POST \
  --data-binary @test/resources_bertdl/inputs/couple_getting_married.inputs.csv \
  -H 'Content-Type: text/csv' \
  -H 'X-Amzn-SageMaker-Custom-Attributes: tfs-model-name=bert-dl' \
  http://localhost:8080/invocations

echo ""
echo "Content-Type: application/json"
echo "Accept: text/csv"
curl -X POST \
  --data-binary @test/resources_bertdl/inputs/couple_getting_married.inputs.json \
  -H 'Content-Type: application/json' \
  -H 'Accept: text/csv' \
  -H 'X-Amzn-SageMaker-Custom-Attributes: tfs-model-name=bert-dl' \
  http://localhost:8080/invocations

echo ""
echo "Content-Type: text/csv"
echo "Accept: text/csv"
curl -X POST \
  --data-binary @test/resources_bertdl/inputs/couple_getting_married.inputs.csv \
  -H 'Content-Type: text/csv' \
  -H 'Accept: text/csv' \
  -H 'X-Amzn-SageMaker-Custom-Attributes: tfs-model-name=bert-dl' \
  http://localhost:8080/invocations