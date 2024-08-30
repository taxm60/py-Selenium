import time
from selenium                         import webdriver
from selenium.webdriver.edge.service  import Service
from selenium.webdriver.common.by     import By
from selenium.webdriver.common.keys   import Keys
from selenium.webdriver.support.ui    import Select
from selenium.webdriver.edge.options  import Options as EdgeOP

# for IE mode
#  ie_options = webdriver.IeOptions()
#  ie_options.attach_to_edge_chrome = True
#  ie_options.edge_executable_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
#  driver = webdriver.Ie(options=ie_options)

# for Edge mode : setup Edge options, initialize the WebDriver
edge_options = EdgeOP()
edge_options.add_argument('--start-maximized')  # Optional: Start maximized
running_path = Service(executable_path="msedgedriver.exe")
driver = webdriver.Edge(service=running_path, options=edge_options)

url = "https://rahulshettyacademy.com/angularpractice/"
driver.get(url)

driver.find_element(By.XPATH, "//input[@name='name']").send_keys("Liu Iverson")
driver.find_element(By.XPATH, '//input[@name="email"]').send_keys("abc@hotmail.com")
driver.find_element(By.CSS_SELECTOR, "#exampleInputPassword1").send_keys("123456")

driver.find_element(By.CSS_SELECTOR, "#inlineRadio2").click()
driver.find_element(By.CSS_SELECTOR, "#exampleCheck1").click()

#static dropdown menu
gender = Select( driver.find_element(By.CSS_SELECTOR, "#exampleFormControlSelect1") )
gender.select_by_visible_text("Female")


driver.find_element(By.XPATH, "//input[@value='Submit']").click()

time.sleep(10)  # Wait 10 seconds to see the result
driver.quit()  # Close the browser
