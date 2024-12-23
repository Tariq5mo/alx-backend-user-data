#!/usr/bin/env python3
"""
This module provides a function to obfuscate specified fields
in a log message.
"""
import re
from typing import List
import logging
import os
import mysql.connector


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
    Returns a logging.Logger object configured for user data logging.
    """
    logger: logging.Logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    formatter = RedactingFormatter(fields=list(PII_FIELDS))
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger


""" Task 3 """


def get_db() -> mysql.connector.connection.MySQLConnection:
    """This function returns a connector to the database."""
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db = os.getenv("PERSONAL_DATA_DB_NAME")

    connection = mysql.connector.connect(
        user=username, password=password, host=host, database=db
    )
    return connection


""" Task 4 """


def main():
    """ Main function """
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    logger = get_logger()

    for data in cur.fetchall():
        user_data = {
            "name": data[0],
            "email": data[1],
            "phone": data[2],
            "ssn": data[3],
            "password": data[4],
            "ip": data[5],
            "last_login": data[6],
            "user_agent": data[7]
        }
        log_message = "; ".join([f"{key}={value}"
                                 for key, value
                                 in user_data.items()])
        logger.info(log_message)

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
