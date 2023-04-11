#!/usr/bin/python3
# 5-to_json_string.py
# Megersa Oljira <motirase2022@gmial.com>
"""Defines a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a string object."""
    return json.dumps(my_obj)
