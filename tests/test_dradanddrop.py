from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import pytest
import allure

@pytest.skip
def test_draganddrop():

    driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://www.seleniumeasy.com/test/")
    driver.implicitly_wait(50)
    driver.find_element_by_xpath('//*[@id="navbar-brand-centered"]/ul[2]/li[4]/a').click()
    driver.find_element_by_xpath('//*[@id="navbar-brand-centered"]/ul[2]/li[4]/ul/li[1]/a').click()
    actionchains=ActionChains(driver)
    source_element=driver.find_element_by_xpath('//*[@id="todrag"]/span[1]')
    target_element=driver.find_element_by_xpath('//*[@id="mydropzone"]')
    actionchains.click_and_hold(source_element,target_element).perform()
    driver.close()