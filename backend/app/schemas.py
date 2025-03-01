from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class CourseBase(BaseModel):
    title: str
    price: float
    link: str


class CourseCreate(CourseBase):
    pass


class PromoCodeBase(BaseModel):
    code: str
    price: float
    expires_at: datetime
    active: bool = True
    course_id: Optional[int] = None


class PromoCodeCreate(PromoCodeBase):
    pass


class PromoCodeRead(PromoCodeBase):
    id: int

    class Config:
        orm_mode = True


class CourseRead(CourseBase):
    id: int
    promocode: Optional[PromoCodeRead] = None

    class Config:
        orm_mode = True
