#!/usr/bin/env python3
"""
Main file
"""

import email
from filtered_logger import get_db



db = get_db()
cursor = db.cursor()
cursor.execute("SELECT COUNT(*) FROM users;")
for row in cursor:
    print(row[0])
cursor.close()
db.close()
