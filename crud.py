import models
import schemas

from sqlalchemy import update
from sqlalchemy.orm import Session
from models import Environment


class ModelAlreadyExistsError(Exception):
    pass


# Customized Error Message
class RecordNotFoundError(Exception):
    def __int__(self, message):
        super().__init__(message)


# User
def get_user(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    u = schemas.UserCreate.parse_obj(user)

    new_user = models.User(**u.dict())

    db.add(new_user)
    db.commit()

    db.refresh(new_user)

    return new_user


# Course
def get_course(db: Session, subject: str, catalog_number: str, semester: str):
    return db.query(models.Course).filter(
        models.Course.subject == subject,
        models.Course.catalog_number == catalog_number,
        models.Course.semester == semester
    ).first()


def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Course).offset(skip).limit(limit).all()


def create_course(db: Session, course: schemas.CourseCreate):
    c = schemas.CourseCreate.parse_obj(course)

    new_course = models.Course(**c.dict())
    db.add(new_course)
    db.commit()
    db.refresh(new_course)

    return new_course


# Service
def get_service(db: Session, name: str):
    return db.query(models.Service).filter(
        models.Service.name == name
    ).first()


def get_services(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Service).offset(skip).limit(limit).all()


def create_service(db: Session, service: schemas.ServiceCreate):
    s = schemas.ServiceCreate.parse_obj(service)

    new_service = models.Service(**s.dict())
    db.add(new_service)
    db.commit()
    db.refresh(new_service)

    return new_service


# Submissions
def get_submission(db: Session, id: int):
    return db.query(models.Submission).filter(
        models.Submission.id == id
    ).first()


def create_submission(db: Session, submission: schemas.SubmissionCreate):
    s = schemas.SubmissionCreate.parse_obj(submission)

    new_submission = models.Submission(**submission)
    db.add(new_submission)
    db.commit()
    db.refresh(new_submission)

    return new_submission


# Environments
def get_environment(db: Session, id: str):
    return db.query(models.Environment).filter(
        models.Environment.id == id
    ).first()


def get_environment_by_user_id(db: Session, id: str):
    return db.query(models.Environment).filter(
        models.Environment.user_id == id
    ).first()


def get_environments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Environment).offset(skip).limit(limit).all()


def create_environment(db: Session, environment: schemas.EnvironmentCreate):
    schemas.EnvironmentCreate.parse_obj(environment)

    new_environment = models.Environment(**environment)
    db.add(new_environment)
    db.commit()

    db.refresh(new_environment)

    return new_environment


def update_environment(db: Session, env: schemas.Environment):
    try:
        schemas.Environment.parse_obj(env)

        new_env = schemas.Environment(**env)

        user_exist = get_user(db=db, user_id=new_env.user.id)

        # Check if user is existed before update the record
        if user_exist:
            update_stmt = (
                update(Environment)
                .where(Environment.user_id == new_env.user.id)
                .values(document=new_env.document)
            )

            db.execute(update_stmt)
            db.commit()

            # Check if environment data is updated.
            update_env = get_environment(db=db, id=new_env.id)

            if update_env:
                return update_env
            else:
                raise RecordNotFoundError(f"Environment {new_env.id} not found or update failed.")
        else:
            raise RecordNotFoundError(f"User {new_env.user.id} not found in the database.")
    except RecordNotFoundError as e:
        print(f"An error occurred: {e}")
