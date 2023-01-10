#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 3-to_json_string.py
"""
Created on Tuesday jan 10 2023

@author: Layomi22
"""
import json


def to_json_string(my_obj):
    """
    Returs a json string containing object's representation

    Arguments:
        my_obj (str): The inputed object to convert in json format

    Return:
        A json format text
    """
    return json.dumps(my_obj)
