import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from prueba import prueba

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

#https://sites.google.com/chromium.org/driver/ para descargar el chromedriver

driver.get("https://front.testadmincrac.com/home")

driver.maximize_window()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "button-close-popup"))
)

close_button_popup = driver.find_element(By.CLASS_NAME, "button-close-popup")
close_button_popup.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "combo-box-demo"))
)

input_element = driver.find_element(By.ID, "combo-box-demo")
#input_element.clear()
input_element.send_keys("Alcohol" + Keys.ENTER)

#elemento = driver.find_element("xpath", "//div[@id='contenido']")
#driver.execute_script("arguments[0].scrollIntoView();", elemento)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "product-title-name"))
)

product_item = driver.find_element(By.CLASS_NAME, "product-title-name")
product_item.click()

#WebDriverWait(driver, 5).until(
#    EC.presence_of_element_located((By.CLASS_NAME, "fa fa-plus"))
#)

add_item = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[2]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[5]/div/div/div/span[3]/i")

for i in range(5):
    add_item.click()

close_item_popup = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[2]/div[2]/div/div/div/div[1]/div/img")
close_item_popup.click()

cart_button = driver.find_element(By.CLASS_NAME, "cartCircle-image")
cart_button.click()

continue_purchase = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[4]/div[3]/button/span")
continue_purchase.click()

#-------------------------- DATOS -----------------------------------------

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div/div/div/div[1]/div[1]/div/button[1]/span"))
)

send_home = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div/div/div/div[1]/div[1]/div/button[1]/span")
send_home.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div[1]/input"))
)

firstName = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div[1]/input")
firstName.send_keys("Nombre Prueba" + Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div[2]/input"))
)

lastName = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div[2]/input")
lastName.send_keys("Apellido Prueba" + Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div[3]/input"))
)

dni = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div[3]/input")
dni.send_keys("34343434" + Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[2]/div[1]/input"))
)

email = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[2]/div[1]/input")
email.send_keys("mailfalso@mail.com" + Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[2]/div[2]/input"))
)

cellphone = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[2]/div[2]/input")
cellphone.send_keys("1121538795" + Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[3]/div[1]/input"))
)

address = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[3]/div[1]/input")
address.send_keys("Calle Prueba" + Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[3]/div[2]/input"))
)

address_number = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[3]/div[2]/input")
address_number.send_keys("1515" + Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[3]/div[3]/input"))
)

address_apartment = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[3]/div[3]/input")
address_apartment.send_keys("4A" + Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[4]/div[1]/input"))
)

zipcode = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[4]/div[1]/input")
zipcode.send_keys("1513" + Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[4]/div[2]/input"))
)

location = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[4]/div[2]/input")
location.send_keys("Localidad Prueba" + Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "react-select-5-input"))
)

province = driver.find_element(By.ID, "react-select-5-input")
province.click()
province.send_keys("Salta" + Keys.ENTER)

oca = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[8]/div[1]/div/label/input")
oca.click()

flete = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[8]/div[2]/div/label/input")

continue_button = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/button")
continue_button.click()

#Final de la compra

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div/div[2]/div/div[2]/button[2]"))
)
back_to_cart = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div/div[2]/div/div[2]/button[2]")
time.sleep(5)
back_to_cart.click()

continue_button = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/button")
continue_button.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div/div[2]/div/div[2]/a"))
)

abandon_purchase = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div/div[2]/div/div[2]/a")
abandon_purchase.click()

#---------------------------------------------------------------------------------------
time.sleep(5)

driver.quit()