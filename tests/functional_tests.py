from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_get_jug_of_test(self):
        self.browser.get('http://localhost')

        self.assertIn('Jug of Punch', self.browser.title)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
