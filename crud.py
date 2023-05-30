from pydantic import validate_arguments, ValidationError
from sqlalchemy import select
from sqlalchemy.orm import Session

from . import models, schemas

class ModelAlreadyExistsError(Exception):
    pass

#User
def get_user(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):

    u = schemas.UserCreate.parse_obj(user)

    statement = select(models.User).filter_by(sso_sub=u.sso_sub)
    result = db.execute(statement).scalars().first()

    if result is None:
        new_user = models.User(**user)
        db.add(new_user)
        db.commit()
    else:
        raise ModelAlreadyExistsError

#Course
def get_course(db: Session, subject: str, catalog_number: str, semester:str):
    return db.query(models.Course).filter(
        subject==subject,
        catalog_number==catalog_number,
        semester==semester,
    ).first()

def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Course).offset(skip).limit(limit).all()

def create_course(db: Session, course: schemas.CourseCreate):

    c = schemas.CourseCreate.parse_obj(course)

    statement = select(models.Course).filter_by(
        subject=c.subject,
        catalog_number=c.catalog_number,
        semester=c.semester)

    result = db.execute(statement).scalars().first()

    if result is None:
        new_course = models.Course(**course)
        db.add(new_course)
        db.commit()
    else:
        raise ModelAlreadyExistsError


#Service
def get_service(db: Session, name: str):
    return db.query(models.Service).filter(
        name==name
    ).first()

def get_services(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Service).offset(skip).limit(limit).all()

def create_service(db: Session, service: schemas.ServiceCreate):

    s = schemas.ServiceCreate.parse_obj(service)

    statement = select(models.Service).filter_by(name=s.name)

    result = db.execute(statement).scalars().first()

    if result is None:
        new_service = models.Service(**service)
        db.add(new_service)
        db.commit()
    else:
        raise ModelAlreadyExistsError

#Service
def get_submission(db: Session, id: int):
    return db.query(models.Service).filter(
        id==id
    ).first()

def create_submission(db: Session, submission: schemas.SubmissionCreate):

    s = schemas.SubmissionCreate.parse_obj(submission)
    
    new_submission = models.Submission(**submission)
    db.add(new_submission)
    db.commit()

    db.refresh(new_submission)

    return new_submission
