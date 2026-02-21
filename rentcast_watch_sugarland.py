#!/usr/bin/env python3
import os
import re
import json
import sqlite3
import requests
from datetime import datetime, timezone

ZIP_CODES = ["77478", "77479"]
PROPERTY_TYPE = "Single Family"
BEDROOM_MIN = 4
BEDROOM_MAX = 6

RENTCAST_API_KEY = os.environ.get("RENTCAST_API_KEY", "")
DB_PATH = "watch.db"

RE_NUM_DOWN = re.compile(r"(\\d+)\\s*(bed|beds|bedroom|bedrooms).*?(down|first floor)", re.I)
RE_PRIMARY_DOWN = re.compile(r"(primary|master).*?(down|first floor)", re.I)

def infer_downstairs_beds(text):
    if not text:
        return None
    m = RE_NUM_DOWN.search(text)
    if m:
        return int
