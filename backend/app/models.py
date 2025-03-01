from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database import Base


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    link = Column(String, nullable=False)

    promocode = relationship("PromoCode", back_populates="course", uselist=False)


class PromoCode(Base):
    __tablename__ = "promocodes"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, nullable=False, unique=True)
    price = Column(Float, nullable=False)
    expires_at = Column(DateTime, nullable=False)
    active = Column(Boolean, default=True)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=True)

    course = relationship("Course", back_populates="promocode")
