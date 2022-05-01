from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=chrome_options)
driver.get('https://passport.yandex.ru/auth?origin=home_desktop_ru&retpath=https%3A%2F%2Fmail.yandex.ru%2F&backpath=https%3A%2F%2Fyandex.ru')

elem = driver.find_element(By.ID, 'passp-field-login')
elem.send_keys('artur.tzaturyan2011@yandex.ru')
elem.send_keys(Keys.ENTER)

time.sleep(2)
elem = driver.find_element(By.ID, 'passp-field-passwd')
elem.send_keys('qwe357357qwe')
elem.send_keys(Keys.ENTER)

WebDriverWait(driver, 5).until(EC.title_contains('Входящие'))
assert 'Входящие' in driver.title

mails = []
for i in range(1):
    time.sleep(3)
    items = driver.find_elements(
        By.XPATH, "//a[@class='mail-MessageSnippet js-message-snippet toggles-svgicon-on-important toggles-svgicon-on-unread']")
    actions = ActionChains(driver)
    for item in items:
        link = item.get_attribute('href')
        mail = {'link': link}
        mails.append(mail)
    actions.move_to_element(items[-1])
    actions.perform()


emails = []
for a in mails:
    driver.get(a['link'])
    email = {
        'author': driver.find_element(By.XPATH, "//button[@class='Button2 Button2_size_s Button2_view_clear SenderName_sender_F3wYv undefined Sender_senderName_BQ7TB qa-MessageViewer-SenderName']").get_attribute('title'),
        'date': driver.find_element(By.XPATH,  "//a[@class='Header_dateLink_Y2p9n qa-MessageViewer-Header-dateLink']").text,
        'object': driver.find_element(By.XPATH, "//span[@class='Title_subject_tyZv5']").text,
        #'body': driver.find_element(By.XPATH, "//div[@class='abedfe1e221dfbfecontent']/p").text
    }
    emails.append(email)
    driver.back()
    WebDriverWait(driver, 5).until(EC.title_contains('Входящие'))

    #'body': driver.find_element(By.XPATH, "//h1[@class='3ed373ba2bce3db8dark-theme-blackText-4tggG']").text






    #while pages < 3:
    #wait = WebDriverWait(driver, 10)
    #button = wait.until(EC.element_to_be_clickable(
    #    (
    #        By.CLASS_NAME, 'ns-view-messages-item-wrap ns-view-id-123 mail-MessageSnippet-Wrap js-messages-item-checkbox-controller js-cbt-item js-message-snippet-wrap js-messages-item mid-179018085188012924 js-message-wrap-179018085188012924 is-checked'
    #    )
    #))
    #button.click()
    #pages +=1
# Клики перехватываются сайтом


#driver.get('https://mail.yandex.ru/?uid=123796009#inbox')
#driver.find_element(By.XPATH, "//a[@class='mail-MessageSnippet js-message-snippet toggles-svgicon-on-important toggles-svgicon-on-unread']").get_attribute('href')
#driver.find_elements(By.XPATH, "//div[@class='ns-view-container-desc mail-MessagesList js-messages-list']")


#urls_marker = WebDriverWait(driver, 30).until(
    #EC.visibility_of_element_located(By.XPATH, '//a[@class = 'mail-MessageSnippet js-message-snippet toggles-svgicon-on-important toggles-svgicon-on-unread']'))

#url_list = driver.find_elements(By.XPATH, '//a[@class = 'mail-MessageSnippet js-message-snippet toggles-svgicon-on-important toggles-svgicon-on-unread']')
#url_set = set()

#for a in url_list:
    #url_set.add(a.get_attribute('href'))  # собираем ссылки, пока они видны на экране

#while len(url_set) != 15:
    #actions = ActionChains(driver)
    #actions.move_to_element(url_list[-1])
    #actions.perform()
    #time.sleep(1)
    #url_list = driver.find_elements(By.XPATH, "//a[@class = 'mail-MessageSnippet js-message-snippet toggles-svgicon-on-important toggles-svgicon-on-unread']")
    #for a in url_list:
        #url_set.add(a.get_attribute('href'))  # собираем ссылки, пока они видны на экране
   # print(f"Собрано URL'ов: {len(url_set)}")









print()


driver.quit()