#!/usr/bin/env python3
"""Filtered logger module"""

import re
from typing import List
import logging
import mysql.connector
from os import getenv

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """A function to filter required fields in a log"""
    for field in fields:
        message = re.sub(
            f"{field}=.+?{separator}", f"{field}={redaction}{separator}", message
        )
    return message


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Formatting method for logs"""
        msg = filter_datum(self.fields, self.REDACTION,
                           record.getMessage(), self.SEPARATOR)
        return (self.FORMAT %
                {"name": record.name, "levelname": record.levelname, "asctime":
                 self.formatTime(record, self.datefmt), "message": msg})


def get_logger() ->logging.Logger:
    """A function which returns a logging object"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream = logging.StreamHandler()
    stream.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(stream)
    return logger


def get_db() ->mysql.connector.connection.MySQLConnection:
    """A function which returns a connector to database"""
    connection = mysql.connector.connection.MySQLConnection(
        user=getenv("PERSONAL_DATA_DB_USERNAME","root"),
        password=getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        host=getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        database=getenv("PERSONAL_DATA_DB_NAME")    
    )
    return connection


def main():
    """Obtains a database connection using get_db and retrieves all rows"""
    db_connection = get_db()
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM users;")
    fields = [i[0] for i in cursor.description]
    
    logger = get_logger()
    
    for row in cursor:
        str_row = "".join(f"{f}={str(r)}; " for r, f in zip(row,fields))
        logger.info(str_row.strip())
        
    cursor.close()
    db_connection.close()
    
    
if __name__ == "__main__":
    main()
