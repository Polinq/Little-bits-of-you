from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from random import*

driver = webdriver.Chrome()

actionChains = ActionChains(driver)
driver.get("https://littlebitsofyou.com/")

driver.implicitly_wait(10)
login = driver.find_element_by_class_name('bt-login').click()

driver.implicitly_wait(10)

window_before = driver.window_handles[0]
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
driver.implicitly_wait(15)

url = 'https://www.google.com/accounts/Login?hl=ja&continue=http://www.google.com.ua/' # https://www.google.com/accounts/Login?hl=ja&continue=http://www.google.co.jp
driver.get(url)

<<<<<<< HEAD
driver.find_element_by_id("identifierId").send_keys('polina.sobolevskaya@eleken.co')
driver.find_element_by_id("identifierNext").click()
driver.implicitly_wait(20)
driver.find_element_by_name("password").send_keys('xromosopiens')
=======
driver.find_element_by_id("identifierId").send_keys("***")
driver.find_element_by_id("identifierNext").click()
driver.implicitly_wait(20)
driver.find_element_by_name("password").send_keys("***")
>>>>>>> c42029a5af24bce27f9c20c01340c2d64972ec2b
element = driver.find_element_by_id('passwordNext')
driver.execute_script("arguments[0].click();", element)

driver.implicitly_wait(10)

driver.switch_to.window(window_before)

login = driver.find_element_by_class_name('bt-login').click()

driver.implicitly_wait(5)


x = randint(1, 1000)

add_text = ActionChains(driver).move_to_element(driver.find_element_by_class_name('src-containers-QuickCreation-styles-styles__addABit')).\
    click().send_keys("тест" + " " + str(x)).perform()

driver.implicitly_wait(10)

add_button = ActionChains(driver).move_to_element(driver.find_element_by_class_name('src-containers-CreateEditNote-dependencies-Panel-styles-styles__add')).\
     click().perform()



# dd_menu = driver.find_element_by_class_name('src-components-atoms-DropDown-styles-styles__dropdown').click()
# logout = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div[3]/div[1]/ul/li[3]').click
# driver.quit()
