#!/usr/bin/env python3
"""
This module provides a function to obfuscate specified fields
in a log message.
"""
import re


def filter_datum(fields, redaction, message, separator):
    """Function"""
    pattern = r'(' + '|'.join(fields) + r')=[^' + f'{separator}' + r']+'
    return re.sub(pattern, r'\1=' + redaction, message)
