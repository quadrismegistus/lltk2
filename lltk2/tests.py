from imports import *

# --------------------
# Tests
# --------------------

class TestIndexView(TestCase):
    def test_success(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
