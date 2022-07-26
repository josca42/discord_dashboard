from typing import Any, Dict, List, Optional

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
import pandas as pd
from typing import List
from .base import CRUDBase
from src.db import models, db


class CRUDMessage(CRUDBase[models.Message, Session]):
    ...


message = CRUDMessage(models.Message, db.SessionLocal)
