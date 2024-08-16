#!/usr/bin/env python3
"""filtered logger"""

import re
from typing import List


def filter_datum(
    fields: List[str], redaction: str, message: str, seperator: str
) -> str:
    """A function to filter required fields"""
    for item in fields:
        message = re.sub(
            f"{item}=.*?{seperator}", f"{item}={redaction}{seperator}", message
        )
    return message
