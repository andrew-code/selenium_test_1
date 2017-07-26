from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.airindia.in/")
list_elements = driver.find_element_by_css_selector('div.footerLinks').text
print(list_elements)
driver.quit()
