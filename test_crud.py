import random
import data
import uuid

from unittest import TestCase
from crud import *
from database import SessionLocal, Base, engine

session = SessionLocal()


class CrudTest(TestCase):

    # Create database and tables
    # def setUp(self):
    #     Base.metadata.create_all(bind=engine)
    #     pass

    """
    Unit test for user
    """

    def test_create_user(self):
        # Generate an uuid as user_id for test
        user_id = str(uuid.uuid4())
        preferred_username = "user-" + user_id.split("-")[0]

        # Mock user data
        user_data = {
            "id": user_id,
            "username": preferred_username,
            "sso_sub": "0000000-0000-0000-0000-00000000000",
            "sso_preferred_username": "user0",
            "sso_email": "user0@example.com",
            "sso_given_name": "User",
            "sso_family_name": "Name",
            "sso_name": "User Name",
            "preferred_username": preferred_username,
            "preferred_email": "user1@example.com",
        }

        # Create user
        result = create_user(db=session, user=user_data)

        # Check if a user is created
        user = get_user(db=session, user_id=result.id)
        expected_u_id = user_id

        self.assertEqual(expected_u_id, user.id, f"The user id {user.id} is not match {expected_u_id}.")

    def test_get_user_by_id(self):
        # Check if a user is existed
        user = get_user(session, user_id=data.user['id'])
        expected_u_id = "fd2vyoq6"

        self.assertEqual(expected_u_id, user.id, f"The user id {user.id} is not match {expected_u_id}.")

    def test_get_maximum_users(self):
        users = get_users(session, skip=0, limit=100)
        self.assertEqual(len(users), 100, "The number of records are not match.")

    def test_get_limited_users(self):
        users = get_users(session, skip=0, limit=28)
        self.assertEqual(len(users), 28, "The number of records are not match.")

    def test_get_pagination_users(self):
        users = get_users(session, skip=100, limit=100)
        self.assertGreater(len(users), 1, "The number of records are not match.")

    """
    Unit test for course
    """

    def test_create_course(self):
        # Mock course id for test
        course_id = random.randint(1, 10000)

        cs_135 = {
            "id": course_id,
            "subject": "CS",
            "catalog_number": "135",
            "semester": "F23",
            "hidden": False
        }

        course = create_course(db=session, course=cs_135)

        expected_course_id = course.id
        expected_subject = "CS"
        expected_catalog_number = "135"
        expected_semester = "F23"

        self.assertEqual(course.id, expected_course_id, "The course id is not match.")
        self.assertEqual(course.subject, expected_subject, "The course subject is not match.")
        self.assertEqual(course.catalog_number, expected_catalog_number, "The catalog number is not match.")
        self.assertEqual(course.semester, expected_semester, "The semester term is not match.")

    def test_get_course(self):
        course = get_course(db=session, catalog_number="135", semester="F23", subject="CS")
        # for c in course.__dir__():
        #     value = getattr(course, c)
        #     if not c.startswith("_"):
        #         print(f"{c}: {value}")

        if course is not None:
            expected_catalog_number = "135"
            expected_semester = "F23"
            expected_subject = "CS"

            self.assertEqual(course.semester, expected_semester, "The semester term is not match.")
            self.assertEqual(course.subject, expected_subject, "The course subject is not match.")
            self.assertEqual(course.catalog_number, expected_catalog_number, "The catalog number is not match.")
        else:
            self.assertIsNotNone(course, "Can't find the record.")

    def test_get_limited_courses(self):
        courses = get_courses(db=session, skip=0, limit=8)
        self.assertEqual(len(courses), 8, "The number of records are not match.")

    def test_get_maximum_courses(self):
        courses = get_courses(db=session, skip=0, limit=100)
        self.assertEqual(len(courses), 100, "The number of records are not match.")

    def test_get_pagination_courses(self):
        courses = get_courses(db=session, skip=100, limit=100)
        self.assertGreater(len(courses), 1, "The number of records are not match.")

    """
    Unit test for service
    """

    def test_create_service(self):
        # Mock service id for test
        service_id = random.randint(1, 10000)
        service_name = f"linux_remote_container_{service_id}"

        service_data = {
            "id": service_id,
            "name": service_name,
            "display_name": "Linux Container Remote Desktop",
        }

        res = create_service(db=session, service=service_data)

        expected_name = service_name
        expected_id = res.id
        expected_display_name = res.display_name

        self.assertEqual(res.name, expected_name, "The service name is not match.")
        self.assertEqual(res.id, expected_id, "The service id is not match.")
        self.assertEqual(res.display_name, expected_display_name, "The service display name is not match.")

    def test_get_service(self):
        service_name = "linux_remote_container_408"

        res = get_service(db=session, name=service_name)

        expected_name = service_name
        expected_id = 408
        expected_display_name = "Linux Container Remote Desktop"

        self.assertEqual(res.name, expected_name, "The service name is not match.")
        self.assertEqual(res.id, expected_id, "The service id is not match.")
        self.assertEqual(res.display_name, expected_display_name, "The service display name is not match.")

    def test_get_limited_services(self):
        res = get_services(db=session, skip=0, limit=23)
        self.assertEqual(len(res), 23, "The number of records are not match.")

    def test_get_pagination_service(self):
        res = get_services(db=session, skip=100, limit=100)
        self.assertGreater(len(res), 1, "The number of records are not match.")

    def test_get_maximum_service(self):
        res = get_services(db=session, skip=0, limit=100)
        self.assertEqual(len(res), 100, "The number of records are not match.")

    """
    Unit test for submission
    """

    def test_create_submission(self):
        # Mock user id for test
        user_id = random.randint(1, 100)

        user = get_users(db=session, skip=0, limit=100)
        course = get_courses(db=session, skip=0, limit=1)
        service = get_services(db=session, skip=0, limit=1)

        sub = {
            "user": user[user_id],
            "courses": course,
            "services": service
        }

        res = create_submission(db=session, submission=sub)
        expected_user_id = user[user_id].id

        self.assertEqual(res.user_id, expected_user_id, "The user id is not match.")

    def test_get_submission(self):
        res = get_submission(db=session, id=1)

        expected_user_id = "a1d5c3d4-3437-4246-af23-acb12701775e"

        self.assertEqual(res.user_id, expected_user_id, "The submission id is not match.")

    """
    Unit test for environment
    """

    def test_create_environment(self):
        # Mock user id for test
        user_id = random.randint(1, 100)

        environment_id = data.env_dict["id"] + '_' + str(random.randint(1, 1000))

        user = get_users(db=session, skip=0, limit=100)

        env = {
            "id": environment_id,
            "user": user[user_id],
            "document": data.env_dict
        }

        res = create_environment(db=session, environment=env)

        self.assertEqual(res.user_id, user[user_id].id, "The user id in environment is not match.")

    def test_get_environment(self):
        res = get_environment(db=session, id="expl_env_626")

        expected_id = "expl_env_626"
        expected_document = data.env_dict
        expected_user_id = "be930003-19f1-494f-ace7-81430f936a66"

        self.assertEqual(res.id, expected_id, "The environment id is not match.")
        self.assertEqual(res.user_id, expected_user_id, "The user id in environment is not match.")
        self.assertEqual(res.document, expected_document, "The document in environment is not match.")

    def test_get_limited_environments(self):
        res = get_environments(db=session, skip=0, limit=5)

        self.assertEqual(len(res), 5, "The number of records is not match.")

    def test_get_environment_by_user_id(self):
        res = get_environment_by_user_id(db=session, id="c29963eb-418f-4d1c-8f34-1847c1969f55")

        expected_id = "expl_env_918"
        expected_document = data.env_dict
        expected_user_id = "c29963eb-418f-4d1c-8f34-1847c1969f55"

        self.assertEqual(res.id, expected_id, "The environment id is not match.")
        self.assertEqual(res.user_id, expected_user_id, "The user id in environment is not match.")
        self.assertEqual(res.document, expected_document, "The document in environment is not match.")

    def test_get_pagination_environment(self):
        res = get_environments(db=session, skip=100, limit=100)
        self.assertGreater(len(res), 1, "The number of records is not match.")

    def test_get_maximum_environment(self):
        res = get_environments(db=session, skip=0, limit=100)
        self.assertEqual(len(res), 100, "The number of records is not match.")

    def test_update_environment(self):
        user = get_user(db=session, user_id="07d93a47-cd53-45cb-8d5a-978018a5cc83")

        environment = {
            "id": "expl_env_332",
            "user": user,
            "document": data.env_dict_no_vscode
        }

        res = update_environment(db=session, env=environment)

        self.assertEqual(res.id, environment["id"], "The environment id is not match.")
        self.assertEqual(res.user_id, user.id, "The user id in environment is not match.")
        self.assertEqual(res.document, data.env_dict_no_vscode, "The document in environment is not match.")

    # Remove database
    # def tearDown(self):
    #     session = SessionLocal()
    #     session.close()
    #     Base.metadata.drop_all(bind=engine)
    #     pass


session.close()
