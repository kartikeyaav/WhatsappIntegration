from selenium import webdriver
from urllib.parse import quote
from selenium.webdriver.support.ui import WebDriverWait
from pyperclip import copy
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome(r'C:\Users\monu\Desktop\chromedriver.exe')
HOST = 'http://localhost:3000'
TARGET = 'achha'
PRODUCTION = False
SCANNED = False
browser.get('https://web.whatsapp.com')
wait = WebDriverWait(browser, 600)
while SCANNED is False:
    image = browser.find_element_by_tag_name('img')
    image_src = image.get_attribute('src')
    encoded = quote(image_src, safe='')
    url = HOST + '/' + encoded
    copy(url)
    print('\nLink copied to your clipboard, you got 20 seconds to visit it and scan your QR code.')
    print('Waiting QR Scanning...')
    sleep(20)
    try:
        notice = browser.find_element_by_class_name('_2dH1A')
        if notice.text == 'Keep your phone connected':
            SCANNED = True
            print('Success!')
    except NoSuchElementException:
        pass
group_title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '._3FRCZ.copyable-text.selectable-text')))
group_title.click()
group_title.send_keys(TARGET)
sleep(5)
group_title.send_keys(Keys.TAB)
chats = browser.find_elements_by_class_name('_210SC')
print(chats)
listDemo = ["demo1", "demo2", "demo3", "demo4","demo5"]
i=0
while True:
    if i>=len(listDemo):
        i=0
    try:
        online = browser.find_element_by_css_selector('._3-cMa._3Whw5').text
        print(online)
        #capturing the Target's online status
        if online == 'online':
            xpath ='//div[normalize-space(@class)="_3FRCZ copyable-text selectable-text"][@dir="ltr"][@data-tab="1"]'
            inputWin =wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            print(TARGET + ' is online!')
            inputWin.click()
            inputWin.send_keys("em chestunav "+listDemo[i])
            inputWin.send_keys(Keys.ENTER)
            sleep(10)
            i = i + 1
    except NoSuchElementException:
        pass
    sleep(2)



