import unittest
import requests

class TestPythonRepos(unittest.TestCase):
    def setUp(self):
        self.url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
        self.headers = {'Accept': 'application/vnd.github.v3+json'}
        self.response = requests.get(self.url, headers=self.headers)
        self.response_dict = self.response.json()

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_repo_count(self):
        self.assertTrue('items' in self.response_dict)
        self.assertTrue(len(self.response_dict['items']) > 0)
    
    def test_total_repos(self):
        total_count = self.response_dict.get('total_count', 0)
        self.assertGreater(total_count, 1000)

if __name__ == '__main__':
    unittest.main()
