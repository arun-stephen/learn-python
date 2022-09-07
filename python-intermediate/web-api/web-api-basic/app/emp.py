import datetime
from pydantic import BaseModel


class Emp(BaseModel):
    id: int
    name: str
    company: str
    place: str
    joining_date: datetime.date
