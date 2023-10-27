from sqlalchemy import ForeignKey, JSON, Column, String, Integer, Boolean
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "reenroll_users"

    id = Column(String, primary_key=True, index=True)

    # SSO Properties
    sso_sub = Column(String)
    sso_preferred_username = Column(String)
    sso_email = Column(String)
    sso_given_name = Column(String)
    sso_family_name = Column(String)
    sso_name = Column(String)

    # Preferred values
    preferred_username = Column(String, unique=True)
    preferred_email = Column(String)

    username = Column(String)

    document = Column(JSON)

    user_submissions = relationship(
        "Submission",
        back_populates="user"
    )

    environments = relationship(
        "Environment",
        back_populates="user"
    )


class Course(Base):
    __tablename__ = "reenroll_courses"
    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String)
    catalog_number = Column(String)
    semester = Column(String)
    hidden = Column(Boolean)

    submissions = relationship(
        "Submission",
        secondary="reenroll_submission_courses",
        back_populates="courses",
    )

    # course_submissions = relationship(
    #    "SubmissionCourse",
    #    back_populates="course"
    # )


class Service(Base):
    __tablename__ = "reenroll_services"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    display_name = Column(String)

    submissions = relationship(
        "Submission",
        secondary="reenroll_submission_services",
        back_populates="services",
    )


class SubmissionCourse(Base):
    __tablename__ = 'reenroll_submission_courses'

    course_id = Column(ForeignKey("reenroll_courses.id"), primary_key=True)
    submission_id = Column(ForeignKey("reenroll_submissions.id"), primary_key=True)

    # course = relationship(
    #    "Course", 
    #    back_populates="course_submissions"
    #    )

    # submission = relationship(
    #    "Submission",
    #    back_populates="submission_courses"
    #    )


class SubmissionService(Base):
    __tablename__ = 'reenroll_submission_services'

    service_id = Column(ForeignKey("reenroll_services.id"), primary_key=True)
    submission_id = Column(ForeignKey("reenroll_submissions.id"), primary_key=True)


class Submission(Base):
    __tablename__ = "reenroll_submissions"
    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(ForeignKey("reenroll_users.id"))

    user = relationship(
        "User",
        back_populates="user_submissions"
    )

    courses = relationship(
        "Course",
        secondary="reenroll_submission_courses",
        back_populates="submissions"
    )

    services = relationship(
        "Service",
        secondary="reenroll_submission_services",
        back_populates="submissions"
    )

    environments = relationship(
        "Environment",
        back_populates="submission"
    )

    # submission_courses = relationship(
    #    "SubmissionCourse",
    #    back_populates="submission"
    # )


class Environment(Base):
    __tablename__ = "reenroll_environments"
    id = Column(String, primary_key=True, index=True)
    document = Column(JSON)

    user_id = Column(ForeignKey("reenroll_users.id"))
    user = relationship("User", back_populates="environments")

    submission_id = Column(ForeignKey("reenroll_submissions.id"))
    submission = relationship("Submission", back_populates="environments")
