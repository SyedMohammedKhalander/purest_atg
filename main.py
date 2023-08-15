import unittest
import requests


class TestWebsiteLoading(unittest.TestCase):
    def test_website_loading(self):
        url = 'https://atg.world'

        # Send a GET request to the website
        response = requests.get(url)

        # Print the response status code for debugging
        print("Response Status Code:", response.status_code)

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200, "Website did not load properly")


if __name__ == '__main__':
    unittest.main()
