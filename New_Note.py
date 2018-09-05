from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from random import*
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
actionChains = ActionChains(driver)
driver.wait = WebDriverWait(driver, 20)

#login
driver.get("https://littlebitsofyou.com/")
driver.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'bt-login'))).click()
login = driver.find_element_by_class_name('bt-login').click()
window_before = driver.window_handles[0]
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
driver.implicitly_wait(15)
driver.find_element_by_id("identifierId").send_keys('polina.sobolevskaya@eleken.co')
driver.find_element_by_id("identifierNext").click()
driver.implicitly_wait(15)
driver.find_element_by_name("password").send_keys('xromosopiens')
element = driver.find_element_by_id('passwordNext')
driver.execute_script("arguments[0].click();", element)
driver.implicitly_wait(10)
driver.switch_to.window(window_before)

# Add_new_note
x = randint(1, 1000)
driver.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'src-containers-QuickCreation-styles-styles__addABit'))).click()
driver.find_element_by_class_name('src-containers-Editor-dependencies-Textarea-styles-styles__textarea').send_keys("Тестовая заметка" + " " + str(x))
driver.find_element_by_class_name('src-containers-CreateEditNote-dependencies-Panel-styles-styles__add').click()

# Add_new_note_with_photo
wait = driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#editor > div > div.src-containers-QuickCreation-styles-styles__wrapper > div.src-containers-QuickCreation-styles-styles__addABit'))).click()
text_area = driver.find_element_by_class_name('src-containers-Editor-dependencies-Textarea-styles-styles__textarea').click()
img_bttn = driver.find_element_by_css_selector('#editor > div > div.src-containers-CreateEditNote-styles-styles__container > div.src-containers-CreateEditNote-dependencies-Panel-styles-styles__container > div.src-containers-CreateEditNote-dependencies-Panel-styles-styles__left > svg:nth-child(2) > path').click

# logout
dd_menu = driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#root > div:nth-child(2) > div.src-containers-Header-styles-styles__Header > div.src-'
                                                                   'containers-Header-styles-styles__offsetRight.src-containers-Header-styles-styles__headerMenu '
                                                                   '> div.undefined.src-components-atoms-DropDown-styles-styles__dropdown'))).click()
logout_btn = driver.find_element_by_css_selector('#root > div:nth-child(2) > div.src-containers-Header-styles-styles__Header > div.src-containers-Header-'
                                    'styles-styles__offsetRight.src-containers-Header-styles-styles__headerMenu > div.undefined.src-components-atoms-DropDown-'
                                    'styles-styles__dropdown > ul > li.src-components-atoms-DropDown-styles-styles__red.src-components-atoms-DropDown-styles-styles__item').click()

driver.quit()

