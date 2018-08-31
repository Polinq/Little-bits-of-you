from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def time(self, sec=10):
    sec = sec


driver = webdriver.Firefox()

actionChains = ActionChains(driver)
driver.get("http://204.48.25.228:2000/")

driver.implicitly_wait(10)
login = driver.find_element_by_class_name('bt-login').click()

driver.implicitly_wait(10)

window_before = driver.window_handles[0]
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
driver.implicitly_wait(15)

url = 'https://www.google.com/accounts/Login?hl=ja&continue=http://www.google.com.ua/' # https://www.google.com/accounts/Login?hl=ja&continue=http://www.google.co.jp
driver.get(url)

driver.find_element_by_id("identifierId").send_keys("***")
driver.find_element_by_id("identifierNext").click()
driver.implicitly_wait(20)
driver.find_element_by_name("password").send_keys("***")
element = driver.find_element_by_id('passwordNext')
driver.execute_script("arguments[0].click();", element)

driver.implicitly_wait(10)

driver.switch_to.window(window_before)

login = driver.find_element_by_class_name('bt-login').click()

driver.implicitly_wait(10)


add_text = ActionChains(driver).move_to_element(driver.find_element_by_class_name('src-containers-QuickCreation-styles-styles__addABit')).\
    click().send_keys('Без качественного тестирования невозможно разрабатывать и '
                      'поддерживать крупный веб-сервис. На ранних этапах его развития '
                      'часто можно обходиться только ручным тестированием по заданному тест-плану, но с появлением новых '
                      'фич и увеличением количества тест-кейсов довольствоваться только им становится все сложнее и '
                      'сложнее. В этой статье мы расскажем о том, как автоматизируем функциональное тестирование веб-интерфейса '
                      'Яндекс.Почты с помощью Selenium WebDriver и Node.js.' * 3).perform()

driver.implicitly_wait(10)

add_button = ActionChains(driver).move_to_element(driver.find_element_by_class_name('src-containers-CreateEditNote-dependencies-Panel-styles-styles__add')).\
     click().perform()

driver.quit()
