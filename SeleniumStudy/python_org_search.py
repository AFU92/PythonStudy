from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://liftit.co")
assert "Liftit" in driver.title
# elem = driver.find_element_by_name("q")
elem = driver.find_element_by_xpath('//*[@id="root"]/div[2]/ul/li[5]/a')
elem.click()
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
driver.close()