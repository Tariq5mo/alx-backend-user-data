#!/usr/bin/env python3
"""
Main file
"""
from re import sub
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Returns the log message obfuscated.

    Args:
        fields (List[str]): A list of strings representing all fields to obfuscate.
        redaction (str): A string representing by what the field will be obfuscated.
        message (str): A string representing the log line.
        separator (str): A string representing by which character is separating all fields in the log line (message).

    Returns:
        str: The obfuscated log message.
    """
    pattern = r'(' + '|'.join(fields) + r')=[^' + f'{separator}' + r']+'
    return sub(pattern, r'\1=' + redaction, message)