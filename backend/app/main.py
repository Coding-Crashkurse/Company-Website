from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
import datetime

from app.database import Base, engine, get_db
from app import models, schemas

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Courses Backend", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/courses", response_model=list[schemas.CourseRead])
def get_courses(db: Session = Depends(get_db)):
    courses = db.query(models.Course).all()
    for course in courses:
        if course.promocode is not None:
            course.link = f"{course.link}?couponCode={course.promocode.code}"
    return [schemas.CourseRead.from_orm(course) for course in courses]


@app.post("/api/courses", response_model=schemas.CourseRead)
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    db_course = models.Course(**course.dict())
    db.add(db_course)
    try:
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    db.refresh(db_course)
    return schemas.CourseRead.from_orm(db_course)


@app.get("/api/promocode", response_model=list[schemas.PromoCodeRead])
def get_all_promocodes(db: Session = Depends(get_db)):
    promocodes = db.query(models.PromoCode).all()
    return [schemas.PromoCodeRead.from_orm(p) for p in promocodes]


@app.get("/api/promocode/{promo_id}", response_model=schemas.PromoCodeRead)
def get_promocode(promo_id: int, db: Session = Depends(get_db)):
    promo = db.query(models.PromoCode).filter(models.PromoCode.id == promo_id).first()
    if not promo:
        raise HTTPException(status_code=404, detail="Promo code not found")
    return schemas.PromoCodeRead.from_orm(promo)


@app.post("/api/promocode", response_model=schemas.PromoCodeRead)
def create_promocode(pc: schemas.PromoCodeCreate, db: Session = Depends(get_db)):
    if pc.course_id is not None:
        course = (
            db.query(models.Course).filter(models.Course.id == pc.course_id).first()
        )
        if not course:
            raise HTTPException(status_code=404, detail="Course not found")
        existing_promo = (
            db.query(models.PromoCode)
            .filter(models.PromoCode.course_id == pc.course_id)
            .first()
        )
        if existing_promo:
            db.delete(existing_promo)
            try:
                db.commit()
            except Exception as e:
                db.rollback()
                raise HTTPException(status_code=400, detail=str(e))
    try:
        db_pc = models.PromoCode(**pc.dict())
        db.add(db_pc)
        db.commit()
    except IntegrityError as ie:
        db.rollback()
        raise HTTPException(status_code=400, detail="Integrity error: " + str(ie.orig))
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    db.refresh(db_pc)
    return schemas.PromoCodeRead.from_orm(db_pc)


@app.patch("/api/promocode/{promo_id}", response_model=schemas.PromoCodeRead)
def update_promocode(
    promo_id: int, pc: schemas.PromoCodeCreate, db: Session = Depends(get_db)
):
    promo = db.query(models.PromoCode).filter(models.PromoCode.id == promo_id).first()
    if not promo:
        raise HTTPException(status_code=404, detail="Promo code not found")
    update_data = pc.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(promo, key, value)
    try:
        db.commit()
    except IntegrityError as ie:
        db.rollback()
        raise HTTPException(status_code=400, detail="Integrity error: " + str(ie.orig))
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    db.refresh(promo)
    return schemas.PromoCodeRead.from_orm(promo)
