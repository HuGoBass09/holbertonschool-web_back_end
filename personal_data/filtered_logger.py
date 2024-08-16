#!/usr/bin/env python3
"""Filtered logger module"""

import re
from typing import List


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """A function to filter required fields in a log"""
    for field in fields:
        message = re.sub(
            f"{field}=.+?{separator}", f"{field}={redaction}{separator}", message
        )
    return message


def main():
    pass


if __name__ == "__main__":
    main()
