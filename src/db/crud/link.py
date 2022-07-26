from sqlalchemy.orm import Session
from .base import CRUDBase
from src.db import models, db


class CRUDLink(CRUDBase[models.Link, Session]):
    ...


link = CRUDLink(models.Link, db.SessionLocal)
