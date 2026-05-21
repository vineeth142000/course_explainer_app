import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Course Explainer', response.data)

    def test_index_lists_courses(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Introduction to Python', response.data)
        self.assertIn(b'Web Development with Flask', response.data)
        self.assertIn(b'Data Science Fundamentals', response.data)

    def test_course(self):
        response = self.app.get('/course/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Course Details', response.data)

    def test_course_shows_details(self):
        response = self.app.get('/course/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Introduction to Python', response.data)
        self.assertIn(b'John Doe', response.data)
        self.assertIn(b'4 weeks', response.data)
        self.assertIn(b'Variables and Data Types', response.data)

    def test_course_two(self):
        response = self.app.get('/course/2')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Web Development with Flask', response.data)
        self.assertIn(b'Jane Smith', response.data)

    def test_course_three(self):
        response = self.app.get('/course/3')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Data Science Fundamentals', response.data)
        self.assertIn(b'Alice Johnson', response.data)

    def test_course_not_found(self):
        response = self.app.get('/course/999')
        self.assertEqual(response.status_code, 404)

    def test_course_zero_not_found(self):
        response = self.app.get('/course/0')
        self.assertEqual(response.status_code, 404)

    def test_videos_page(self):
        response = self.app.get('/videos')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Videos', response.data)

    def test_videos_contains_course_names(self):
        response = self.app.get('/videos')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Introduction to Python', response.data)
        self.assertIn(b'Web Development with Flask', response.data)
        self.assertIn(b'Data Science Fundamentals', response.data)

    def test_videos_contains_youtube_embed(self):
        response = self.app.get('/videos')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'youtube.com/embed', response.data)

if __name__ == '__main__':
    unittest.main()
