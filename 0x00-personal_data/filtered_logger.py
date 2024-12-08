#!/usr/bin/env python3
"""
This module provides a function to obfuscate specified fields
in a log message.
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """Function"""
    pattern = r'(' + '|'.join(fields) + r')=[^' + f'{separator}' + r']+'
    return re.sub(pattern, r'\1=' + redaction, message)
