from sqlalchemy.orm import Session
from src.db.crud.base import CRUDBase
from src.db import models, db
import pandas as pd

Message = models.Message


class CRUDLink(CRUDBase[models.Link, Session]):
    def get_multi(self) -> pd.DataFrame:
        with self.session() as db:
            query = db.query(self.model, Message).join(Message)
            df = pd.read_sql_query(query.statement, db.bind).drop(columns=["id"])
        return df


link = CRUDLink(models.Link, db.SessionLocal)
