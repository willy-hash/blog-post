import unittest
from flask import current_app
from app import create_app, db

#python -m unittest tests.test_instance

class Create_instance_test(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        db.session.remove()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_db_connection(self):
        try:
            with db.engine.connect() as connection:
                self.assertIsNotNone(connection)  # Verifica que la conexión no es None
        except Exception as e:
            self.fail(f"Cant connet to DB: {e}")

