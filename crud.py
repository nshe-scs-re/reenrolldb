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

    new_user = models.Submission(**user)
    db.add(new_user)
    db.commit()

    db.refresh(new_user)

    return new_user


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

    new_course = models.Course(**c)
    db.add(new_course)
    db.commit()
    db.refresh(new_course)

    return new_course

#Service
def get_service(db: Session, name: str):
    return db.query(models.Service).filter(
        name==name
    ).first()

def get_services(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Service).offset(skip).limit(limit).all()

def create_service(db: Session, service: schemas.ServiceCreate):

    s = schemas.ServiceCreate.parse_obj(service)

    new_service = models.Service(**s)
    db.add(new_service)
    db.commit()
    db.refresh(new_service)

    return new_service


#Submissions
def get_submission(db: Session, id: int):
    return db.query(models.Service).filter(
        id==id
    ).first()

def create_submission(db: Session, submission: schemas.SubmissionCreate):

    s = schemas.SubmissionCreate.parse_obj(submission)
    
    new_submission = models.Submission(**s)
    db.add(new_submission)
    db.commit()
    db.refresh(new_submission)

    return new_submission

#Environments
def get_environment(db: Session, id: str):
    return db.query(models.Environment).filter(
        id==id
    ).first()

def get_environments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Environment).offset(skip).limit(limit).all()

def create_environment(db: Session, environment: schemas.EnvironmentCreate):

    e = schemas.EnvironmentCreate.parse_obj(environment)

    new_environment = models.Environment(**environment)
    db.add(new_environment)
    db.commit()

    db.refresh(new_environment)

    return new_environment