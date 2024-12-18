from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional
import uuid


class Message(BaseModel):
    id: str = uuid.uuid4()
    msg: str
    timestamp: datetime = str(datetime.now())


class Chat(BaseModel):
    token: str
    messages: List[Message]
    name: str
    session_start: datetime = str(datetime.now())