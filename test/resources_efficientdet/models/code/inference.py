#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module: inference
Created: 2020-11-25

Description:

    inference.py: inference code for serving efficientdet models

"""
import datetime
import io
import json

import boto3
import numpy as np

from collections import namedtuple
from PIL import Image

Context = namedtuple('Context',
                     'model_name, model_version, method, rest_uri, grpc_uri, '
                     'custom_attributes, request_content_type, accept_header')


def load_s3_image(bucket, key):
    t0 = datetime.datetime.now()
    print(f'starting to load file {bucket}/{key}')
    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket=bucket, Key=key)
    image_as_bytes = io.BytesIO(obj['Body'].read())
    image = Image.open(image_as_bytes)
    instance = np.expand_dims(image, axis=0)
    t1 = datetime.datetime.now()
    print(f'file loaded in {t1 - t0}')
    return json.dumps({"instances": instance.tolist()})


def input_handler(data, context):
    """ Pre-process request input before it is sent to TensorFlow Serving REST API
    Args:
        data (obj): the request data, in format of dict or string
        context (Context): an object containing request and configuration details
    Returns:
        (dict): a JSON-serializable dict that contains request body and headers
    """
    if context.request_content_type == 'application/x-image':
        image_as_bytes = io.BytesIO(data.read())
        image = Image.open(image_as_bytes)
        instance = np.expand_dims(image, axis=0)
        # return json.dumps({"instances": instance.tolist()})
        j = json.dumps({"instances": instance.tolist()})
        print(f'leaving input_handler at {datetime.datetime.now()}')
        return j
    elif context.request_content_type == 'text/csv':
        input_data = data.read().decode('utf-8')
        i = input_data.find('/')
        bucket, key = input_data[:i], input_data[i + 1:]
        # return load_s3_image(bucket=bucket, key=key)
        j = load_s3_image(bucket=bucket, key=key)
        print(f'leaving input_handler at {datetime.datetime.now()}')
        return j
    elif context.request_content_type == 'application/json':
        j = json.loads(data.read().decode('utf-8'))
        bucket = j['bucket']
        key = j['key']
        # return load_s3_image(bucket=bucket, key=key)
        j = load_s3_image(bucket=bucket, key=key)
        print(f'leaving input_handler at {datetime.datetime.now()}')
        return j
    else:
        _return_error(415, 'Unsupported content type "{}"'.format(
            context.request_content_type or 'Unknown'))


def output_handler(data, context):
    """Post-process TensorFlow Serving output before it is returned to the client.
    Args:
        data (obj): the TensorFlow serving response
        context (Context): an object containing request and configuration details
    Returns:
        (bytes, string): data to return to client, response content type
    """
    print(f'entering output_handler at {datetime.datetime.now()}')
    if data.status_code != 200:
        raise Exception(data.content.decode('utf-8'))
    response_content_type = context.accept_header
    prediction = data.content
    return prediction, response_content_type


def _return_error(code, message):
    raise ValueError('Error: {}, {}'.format(str(code), message))
