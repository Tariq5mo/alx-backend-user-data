#!/usr/bin/env python3
""""""
from re import sub
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """"""
    pattern = r'(' + '|'.join(fields) + r')=[^' + f'{separator}' + r']+'
    return sub(pattern, r'\1=' + redaction, message)