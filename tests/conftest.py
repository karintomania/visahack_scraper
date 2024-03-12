import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from const.db import const_db

const_db["database"] = "test_visahack_scraper"
