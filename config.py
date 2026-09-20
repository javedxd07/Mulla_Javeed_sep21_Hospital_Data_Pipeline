"""
config.py
---------
This file stores the settings we need to connect to our MySQL database.

Think of this like a "settings card" for our database connection.
Instead of typing the same connection details in every file, we write
them once here, and every other file just imports this file.

If you are just practicing on your own laptop, you can temporarily replace
the os.environ.get(...) lines with your actual values, but for anything
you plan to share (GitHub, submission, etc.) always keep the environment
variable approach.
"""

from dotenv import load_dotenv
from urllib.parse import quote_plus
import os

load_dotenv()

DB_CONFIG = {
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "database": os.getenv("DB_NAME")
}

password = quote_plus(DB_CONFIG["password"])

CONNECTION_STRING = (
    f"mysql+mysqlconnector://"
    f"{DB_CONFIG['user']}:{password}"
    f"@{DB_CONFIG['host']}:3306/"
    f"{DB_CONFIG['database']}"
)