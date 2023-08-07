from select import select

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice")


driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
driver.find_element(By.ID, "exampleCheck1").click()

driver.find_element(By.CSS_SELECTOR,"input[value='option1'")


driver.find_element(By.CSS_SELECTOR,"input[name='name'").send_keys("TestUser")
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()

#Static drop down
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
#dropdown.select_by_value("teach")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)

assert "Success!" in message

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("helloagain")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()