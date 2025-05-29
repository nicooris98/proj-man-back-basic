from sqlmodel import SQLModel, Field
import uuid
from .base import TimestampMixin

class User(TimestampMixin, SQLModel, table=True):
    __tablename__ = 'users'
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    lastname: str
    email: str = Field(unique=True)
    password: str