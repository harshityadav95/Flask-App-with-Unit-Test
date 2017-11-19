import unittest
from app import app
from random import randint




class testApp(unittest.TestCase):


 
    def test_login_works(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
       # self.assertTrue(True)

    def test_post_api(self):
        tester = app.test_client(self)
        response = tester.get('/', follow_redirects=True)
        self.assertIn(b'input', response.data)

    def test_posts_api(self):
        tester = app.test_client(self)
        response = tester.post('/post_location',data=dict( 
        key="111",
        place_name="AAA",
        admin_name1="AAA",
        latitude="1.0",
        longitude="1.0",
        accuracy="1"),
        follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_post_pincode(self):
        tester = app.test_client(self)
        response = tester.post('/post_location',data=dict( 
        key="IN/110001",
        place_name="AAA",
        admin_name1="AAA",
        latitude="1.0",
        longitude="1.0",
        accuracy="1"),
        follow_redirects=True)
        self.assertIn(b'failed', response.data)

    def test_post_cordinates(self):
        tester = app.test_client(self)
        a=randint(0,9999999)
        response = tester.post('/post_location',data=dict( 
        key=a,
        place_name="AAA",
        admin_name1="AAA",
        latitude="28.6333",
        longitude="77.2167",
        accuracy="1"),
        follow_redirects=True)
        self.assertIn(b'failed', response.data)


    def test_post_missing_key(self):
        tester = app.test_client(self)
        response = tester.post('/post_location',data=dict( 
        key="",
        place_name="AAA",
        admin_name1="AAA",
        latitude="28.6333",
        longitude="77.2167",
        accuracy="1"),
        follow_redirects=True)
        self.assertIn(b'failed', response.data)




if __name__ == '__main__':
    unittest.main()



