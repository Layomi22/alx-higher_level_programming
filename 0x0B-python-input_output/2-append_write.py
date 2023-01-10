#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 2-append_write.py
"""
Created on Tuesday Jan 10 18:46 2023

@author: Layomi22
"""


def append_write(filename="", text=""):
    """
    Appends inputed text into a utf-8 encoded text file

    Arguments:
        filename (str): The name of the file to open
        text (str): The text to append

    Return:
        A file with appened text
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
