import restx
from app import app, db
from app import routers
from app import models

from app.models.base import BaseModel
BaseModel.set_session(db.session)
