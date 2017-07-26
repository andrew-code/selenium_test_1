import unittest

from selenium import webdriver


class TestOne(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_print_list(self):
        driver = self.driver
        driver.get("http://www.airindia.in/")
        list_elements = driver.find_element_by_css_selector('div.footerLinks').text
        print(list_elements)
        print("\nTest PASS!!!!!!!!!!")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()


''' Out:
About Air India
Engineering Services
Air India Airport Services
Conditions of Carriage
US DOT Regulations
Contact Details

Test PASS!!!!!!!!!!
'''