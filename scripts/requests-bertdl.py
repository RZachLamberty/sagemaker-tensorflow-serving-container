#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module: requests_bert_dl
Created: 1912/17/

Description:

    simple requests to the local bert-dl endpoint to verify that I know wtf I
    am doing (which I don't, in sagemaker, right now)

Usage:

    >>> import requests_bert_dl

"""

import os

import requests

# ----------------------------- #
#   Module Constants            #
# ----------------------------- #

URL = 'http://localhost:8080/invocations'
ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
TEST_DIR = os.path.join(ROOT, 'test', 'resources_bertdl', 'inputs')

# ----------------------------- #
#   main function               #
# ----------------------------- #

def test_csv_file():
    f_test = os.path.join(TEST_DIR, 'couple_getting_married.inputs.csv')
    with open(f_test, 'rb') as fp:
        data = fp.read()
    headers = {'content-type': 'text/csv',
               'X-Amzn-SageMaker-Custom-Attributes': 'tfs-model-name=bert-dl'}
    resp = requests.post(url=URL, data=data, headers=headers)
    print(resp.json())


def test_json_file():
    f_test = os.path.join(TEST_DIR, 'couple_getting_married.inputs.json')
    with open(f_test, 'rb') as fp:
        data = fp.read()
    headers = {'content-type': 'application/json',
               'X-Amzn-SageMaker-Custom-Attributes': 'tfs-model-name=bert-dl'}
    resp = requests.post(url=URL, data=data, headers=headers)
    print(resp.json())


if __name__ == '__main__':
    test_csv_file()
    test_json_file()