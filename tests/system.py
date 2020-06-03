import requests
import unittest
import json
import os
from db.database import create_database


class PostEndpointTest(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        if os.path.exists('../db/data.db'):
            # os.system('rm ../db/data.db')
            os.remove('../db/data.db')
        create_database('../db/data.db')
        cls.uri = 'http://127.0.0.1:5000'

    def test_posts_status_code(cls):
        cls.uri += '/posts'
        uri_request = requests.get(cls.uri)
        cls.assertEqual(200, uri_request.status_code)

    def test_posts_response_check(cls):
        cls.uri += '/posts'
        uri_request = requests.get(cls.uri).content
        content_decode = json.loads(uri_request.decode('utf-8'))
        counter = 1
        for post in content_decode.get('posts'):
            cls.assertEqual(counter, post.get('id'))
            counter += 1

    @classmethod
    def tearDownClass(cls):
        os.system('rm ../../db/data.db')

if __name__ == '__main__':
    unittest.main(verbosity=2)