from pydantic import BaseModel
from typing import List


class Answer(BaseModel):
    text: str
