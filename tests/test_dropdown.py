from selenium import webdriver
from selenium.webdriver.support.ui import Select

def test_dropdown():

    driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
    driver.maximize_window()
    driver.get("file:///C:/Users/Abhijit/Desktop/pratice.html")
    driver.implicitly_wait(50)

    drp_element = driver.find_element_by_id("carselect")
    drp_obj = Select(drp_element)
    # drp_obj.select_by_visible_text("Automation")
    # print("Test Passed")

    # to get all options from dropdown
    all_options = drp_obj.options
    for options in all_options:
        list_options = options.text
        store_in_list=list(list_options)
        print(type(store_in_list))
        print(store_in_list)

    driver.close()
