from db.database import create_database
from models.post import PostModel
import unittest
import os


class DataBaseIntegrationTests:

    def setUp(self):
        if os.path.exists('./db/data.db'):
            # os.system('rm ../db/data.db')
            os.remove('./db/data.db')
        create_database('./db/data.db')

    def test_post_model_create(self):
        self.post_model = PostModel(
            1,
            'www.test_perfil.com',
            'www.test_photo.com',
            '@Test',
            1, 10,
            [
                {
                    "login": "@loginComment1",
                    "comment": "comment1"
                },
                {
                    "login": "@loginComment2",
                    "comment": "comment2"
                }
            ]
        )
        self.assertIsNone(self.post_model.find_post(50))
        self.assertIsNotNone(self.post_model.find_post(1))

    def tearDown(self):
        # os.system('rm ./db/data.db')
        os.remove('./db/data.db')

if __name__ == '__main__':
    unittest.main()