from typing import Any, Dict, List, Optional

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
import pandas as pd
from typing import List
from .base import CRUDBase
from src.db import models, db
from typing import List


class CRUDMessage(CRUDBase[models.Message, Session]):
    def get_channel_messages(self, channel_ids: List[int]) -> pd.DataFrame:
        with self.session() as db:
            query = db.query(self.model).filter(self.model.channel_id.in_(channel_ids))
            df = pd.read_sql_query(query.statement, db.bind)
        return df


message = CRUDMessage(models.Message, db.SessionLocal)
