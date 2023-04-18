from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import By


# create driver obj
driver = webdriver.Chrome("C: \\WebDrivers\\Chrome\\chromedriver.exe")


# open browser to google
driver.delete_all_cookies()
driver.get("https://google.com")

driver.implicitly_wait(3.0)

driver.find_element(By.XPATH, '//*[@id="APjFqb"]').send_keys(
    "pizza in shoreline, wa" + Keys.ENTER)

driver.implicitly_wait(3.0)
driver.find_element(
    By.CSS_SELECTOR,
    '#Odp5De > div > div > div > div.ba9qXc > div.JPvYTe > div > div > div:nth-child(1) > div'
).click()
driver.implicitly_wait(3.0)
if (driver.find_element(
        By.XPATH, '//*[@id="Odp5De"]/div/div/div/div[1]/div[1]/div/div/div[1]/div')).is_displayed():
    print('TEST PASS, closing web page...')
else:
    print('"Places" element not found!!!!')
    driver.implicitly_wait(20)


driver.implicitly_wait(3)
driver.close()
