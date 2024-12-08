#!/usr/bin/env python3
"""
This module provides a function to obfuscate specified fields
in a log message.
"""
import re
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields) -> None:
        """
        Initialize the formatter with the fields to redact.

        Args:
            fields (List[str]): A list of strings representing the fields to obfuscate.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord):
        """Format the log record by obfuscating specified fields."""
        record.msg = filter_datum(self.fields, RedactingFormatter.REDACTION, record.msg, RedactingFormatter.SEPARATOR)
        return super().format(record)


def filter_datum(fields,
                 redaction, message, separator):
    """Obfuscate specified fields in the log message."""
    pattern = r'(' + '|'.join(fields) + r')=[^' + f'{separator}' + r']+'
    return re.sub(pattern, r'\1=' + redaction, message)
