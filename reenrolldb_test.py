#!/usr/bin/env python3
import sys
import json

from sqlalchemy import select

from reenrolldb.database import engine, SessionLocal, Base
from reenrolldb.models import User, Course, Service, Submission
from reenrolldb import crud

Base.metadata.create_all(bind=engine)

session = SessionLocal()

#User
u = {
      'id' : 'fd2vyoq6',
      'username' : '',
      'sso_sub' : '0000000-0000-0000-0000-00000000000',
      'sso_preferred_username' : 'user1',
      'sso_email' : 'user1@example.com',
      'sso_given_name' : "User",
      'sso_family_name' : 'Name',
      'sso_name' : 'User Name',
      'preferred_username' : 'user1',
      'preferred_email' : 'user1@example.com',
    }

try:
    crud.create_user(session, u)
except crud.ModelAlreadyExistsError:
    print('User model already exists in database.')

#Course

#CS135
c = {
  'subject' : 'CS',
  'catalog_number' : '135',
  'semester' : 'F23',
  'hidden': False,
}

try:
    crud.create_course(session, c)
except crud.ModelAlreadyExistsError:
    print('Course model already exists in database.')

#CS202
c = {
  'subject' : 'CS',
  'catalog_number' : '202',
  'semester' : 'F23',
  'hidden': False,
}

try:
    crud.create_course(session, c)
except crud.ModelAlreadyExistsError:
    print('Course model already exists in database.')

#Service
s = {
  'name' : 'linux_remote_container',
  'display_name' : 'Linux Container Remote Desktop',
}

try:
    crud.create_service(session, s)
except crud.ModelAlreadyExistsError:
    print('Service model already exists in database.')

#Submission
user = crud.get_user(session, u['id'])
course = crud.get_course(session, c['subject'], c['catalog_number'], c['semester'])
service = crud.get_service(session, s['name'])
print(f'{user}, {course}, {service}')

sub = {
  'user' : user,
  'courses': [course],
  'services': [service],
}

submission = crud.create_submission(session, sub)

submissions = session.query(Submission).all()

for sm in submissions:
  print(sm.id)