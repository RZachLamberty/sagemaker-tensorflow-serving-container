#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module: requests_efficientdet
Created: 1912/17/

Description:

    simple requests to the local efficientdet endpoint to verify that I know
    wtf I am doing (which I don't, in sagemaker, right now)

Usage:

    >>> import requests_efficientdet

"""

import datetime
import os
import pickle
import sys

import requests

# ----------------------------- #
#   Module Constants            #
# ----------------------------- #

URL = 'http://localhost:8080/invocations'
ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
TEST_DIR = os.path.join(ROOT, 'test', 'resources_efficientdet', 'inputs')


# ----------------------------- #
#   main function               #
# ----------------------------- #

def test_img(v=0):
    f_test = ('videoblocks-ml/data/object-detection-research/videoblocks/dev'
             '/sampled-items/jpg/fps-method-01/000000296/000015-0.5005.jpg')
    t0 = datetime.datetime.now()
    headers = {'content-type': 'text/csv',
               'X-Amzn-SageMaker-Custom-Attributes': f'tfs-model-name=efficientdet_d{v}_coco17_tpu-32'}
    resp = requests.post(url=URL, data=f_test, headers=headers)
    t1 = datetime.datetime.now()
    print(t1 - t0)
    try:
        j = resp.json()
        return j['predictions'][0], 'success'
    except KeyError:
        return j, 'error'
    except:
        return resp.text, 'other'


def test_img_json(v=0):
    body = {'bucket': 'videoblocks-ml',
            'key': 'data/object-detection-research/videoblocks/dev/'
                   'sampled-items/jpg/fps-method-01/000000296/000015-0.5005.jpg'}
    headers = {'content-type': 'application/json',
               'X-Amzn-SageMaker-Custom-Attributes': f'tfs-model-name=efficientdet_d{v}_coco17_tpu-32'}
    t0 = datetime.datetime.now()
    resp = requests.post(url=URL, json=body, headers=headers)
    t1 = datetime.datetime.now()
    print(t1 - t0)
    try:
        j = resp.json()
        return j['predictions'][0], 'success'
    except KeyError:
        return j, 'error'
    except:
        return resp.text, 'other'



if __name__ == '__main__':
    v = sys.argv[1]

    print('doing 10 csv tests in a row')
    for i in range(10):
        z = test_img(v)
        print(z[1])
    with open(f'results.{v}.pkl', 'wb') as fp:
        pickle.dump(z, fp)

    print('doing json test')
    z = test_img_json(v)