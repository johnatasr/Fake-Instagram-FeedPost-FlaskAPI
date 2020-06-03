import sys
sys.path.append('../..')
from models.post import PostModel
import unittest


class PostModelTests(unittest.TestCase):

    def setUp(self):
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

    def test_post_model_params(self):
        self.assertEqual(1, self.post_model.id)
        self.assertEqual('www.test_perfil.com', self.post_model.url_perfil)
        self.assertEqual('www.test_photo.com', self.post_model.url_photo)
        self.assertEqual('@Test', self.post_model.login_user)
        self.assertEqual(1, self.post_model.liked)
        self.assertEqual(10, self.post_model.likers)
        self.assertEqual(
            [
                {
                    "login": "@loginComment1",
                    "comment": "comment1"
                },
                {
                    "login": "@loginComment2",
                    "comment": "comment2"
                }
            ], self.post_model.comments
        )

    def test_json_return(self):
        output = {
            'id': 1,
            'url_perfil': 'www.test_perfil.com',
            'url_photo': 'www.test_photo.com',
            'login': '@Test',
            'liked': 1,
            'likers': 10,
            'comments': [
                {
                    "login": "@loginComment1",
                    "comment": "comment1"
                },
                {
                    "login": "@loginComment2",
                    "comment": "comment2"
                }
            ]
        }
        self.assertEqual(output, self.post_model.json())

if __name__ == '__main__':
    unittest.main(verbosity=2)