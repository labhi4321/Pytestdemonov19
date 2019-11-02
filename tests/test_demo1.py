from selenium import webdriver


def test_alert():
    driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
    driver.maximize_window()
    driver.get("file:///C:/Users/Abhijit/Desktop/pratice.html")
    driver.implicitly_wait(50)
    driver.find_element_by_name('enter-name').send_keys("Abhijit")
    driver.find_element_by_id('alertbtn').click()
    alert = driver.switch_to.alert
    test1 = alert.text
    print(test1)
    alert.accept()
    driver.close()
