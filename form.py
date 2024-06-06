from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

try:
    path = r"file:///C:/Users/PSH/Desktop/Practice/mid/Q2%20(1).html"

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    data = ["Hazik Ahmed", "Jawed Ahmed Khan", "Pathan","4130442633679","Hyderabad","Python","Male","Evening"]

    driver.get(path)
    driver.maximize_window()

    name_field = driver.find_element(By.ID,"name")
    name_field.send_keys(data[0])

    fname_field = driver.find_element(By.ID,"f_name")
    fname_field.send_keys(data[1])

    caste_field = driver.find_element(By.ID,"caste")
    caste_field.send_keys(data[2])

    cnic_field = driver.find_element(By.ID,"cnic")
    cnic_field.send_keys(data[3])

    select = driver.find_element(By.ID,"course")

    if data[4] ==  "Hyderabad":
        city_select= driver.find_element(By.ID,"hyd")
        city_select.click()

    if data[5] ==  "Python":
        course_select= driver.find_element(By.ID,"python")
        course_select.click()

    if data[6] ==  "Male":
        gender_select= driver.find_element(By.ID,"male")
        gender_select.click()    
    
    if data[7] ==  "Evening":
        shift_select= driver.find_element(By.ID,"evening")
        shift_select.click() 
    

    submit = driver.find_element(By.ID,"submit") 
    submit.click()        



except:
    print("error")
finally:
    time.sleep(20)
    print(driver.title)
    print(driver.current_url)
    driver.quit()    