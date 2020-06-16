from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Remote(command_executor='http://127.0.0.1:9515')
driver.get("http://www.google.com")
assert "Google" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("Дайрабаев Гилан")
elem.send_keys(Keys.RETURN)
content  = "LC20lb"
elements = driver.find_elements_by_class_name(content)[:5]
result = []
for element in elements:
    result.append(element.text)
print(result)
driver.close()