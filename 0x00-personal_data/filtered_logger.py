#!/usr/bin/env python3
"""
This module provides a function to obfuscate specified fields
in a log message.
"""
import re
from typing import List
import logging


""" Task 2 """
PII_FIELDS = ("name", "email", "ssn", "password", "phone")


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION: str = "***"
    FORMAT: str = (
        "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
        )
    SEPARATOR: str = ";"

    def __init__(self, fields: List[str]):
        """function"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields: List[str] = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format the log record by obfuscating specified fields."""
        record.msg = filter_datum(
            self.fields,
            RedactingFormatter.REDACTION,
            record.msg,
            RedactingFormatter.SEPARATOR,
        )
        return super().format(record)


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """Obfuscate specified fields in the log message."""
    pattern = r"(" + "|".join(fields) + r")=[^" + f"{separator}" + r"]+"
    return re.sub(pattern, r"\1=" + redaction, message)


""" Task 2 """


def get_logger() -> logging.Logger:
    """

    Returns:
        logging.Logger: _description_
    """
    logger: logging.Logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    formater = RedactingFormatter(fields=list(PII_FIELDS))
    handler.setFormatter(formater)

    logger.addHandler(handler)
    return logger
