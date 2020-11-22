#libraries import
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
#WebDriver for chrome
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
browser = webdriver.Chrome(options=options,executable_path=r'C:\Users\monu\Desktop\chromedriver.exe')
HOST = 'http://localhost:3000'
#Target contact name
TARGET = 'monu'
PRODUCTION = False
SCANNED = True

#Youtube Search Function
def youtubesearch(browse,inputString):
    browse.execute_script("window.open('about:blank', 'tab2');")
    # youtube_window = browse.window_handles[1]
    ##switching to youtube to fetch video links
    browse.switch_to.window("tab2")
    browse.get("https://www.youtube.com/")
    #waiting for the page to load
    WebDriverWait(browse, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#search"))).send_keys(inputString)
    browse.find_element_by_css_selector("button.style-scope.ytd-searchbox#search-icon-legacy").click()
    return WebDriverWait(browse, 5).until(EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, "a.yt-simple-endpoint.style-scope.ytd-video-renderer#video-title")))[0].get_attribute("href")

#Meaning Function
def meaningofWord(browse,inputString):
    #window of chrome
    browse.execute_script("window.open('about:blank', 'tab2');")
    google_window = browse.window_handles[1]
    browse.switch_to.window("tab2")
    meaning =[]
    browse.get("https://www.google.com/")
    translatedText= "Sorry! unable to find word"
    example= "none"
    meaning.append(translatedText)
    meaning.append(example)
    try:
        element=WebDriverWait(browse, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.gLFyf.gsfi"))).send_keys(inputString+Keys.ENTER)
        WebDriverWait(browse, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.Tg7LZd")))
        #Xpath of meaning and the word usage
        xpath='//div[@data-dobid="dfn"]'
        xpath2= '//div[@class="vk_gy"]'
        meaning[0] = WebDriverWait(browse,5).until(EC.visibility_of_element_located((By.XPATH,xpath))).text
        meaning[1] = WebDriverWait(browse, 5).until(EC.visibility_of_element_located((By.XPATH, xpath2))).text
    except NoSuchElementException:
        pass
    except TimeoutException:
        pass
    return meaning
#Function to translate the text using Google Translate
def googletranslate(browse,inputString):
    browse.execute_script("window.open('about:blank', 'tab2');")
    google_window = browse.window_handles[1]
    browse.switch_to.window("tab2")
    browse.get("https://www.google.com/")
    translatedText= "Sorry! unable to find word"
    translatedText2 = ""
    translation=[]
    translation.extend([translatedText,translatedText2])
    try:
        element=WebDriverWait(browse, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.gLFyf.gsfi"))).send_keys(inputString+Keys.ENTER)
        WebDriverWait(browse, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.Tg7LZd")))
        xpath='//pre[normalize-space(@class)="tw-data-text tw-text-large XcVN5d tw-ta"]//span[@lang]'
        translated=WebDriverWait(browse,5).until(EC.visibility_of_element_located((By.XPATH,xpath)))
        translation[0] = translated.text
        xpath2='//pre[normalize-space(@class)="tw-data-text tw-text-small tw-ta"][@id="tw-target-rmn"]//span'
        translated2 = WebDriverWait(browse, 2).until(EC.visibility_of_element_located((By.XPATH, xpath2)))
        translation[1] = translated2.text
    except NoSuchElementException:
        pass
    except TimeoutException:
        pass
    return translation
#Function for dynamic Covid Status in India
def covidstatus(browse):
    browse.execute_script("window.open('about:blank', 'tab2');")
    google_window = browse.window_handles[1]
    browse.switch_to.window("tab2")
    browse.get("https://www.covid19india.org/")
    count = []
    Total= "Not updated"
    daily = "Not Updated"
    active= "Not updated"
    recovered_total ="Not updated"
    recovered_daily ="Not updated"
    deceased_total ="Not updated"
    deceased_daily ="Not updated"
    count.extend([Total,daily,active,recovered_total,recovered_daily,deceased_total,deceased_daily])
    try:
        xpath_confirmed_total = '//div[normalize-space(@class)="level-item is-confirmed fadeInUp"]//h1'
        Total_count=WebDriverWait(browse, 5).until(EC.presence_of_element_located((By.XPATH, xpath_confirmed_total)))
        xpath_confirmed_daily='//div[normalize-space(@class)="level-item is-confirmed fadeInUp"]//h4'
        daily_count=WebDriverWait(browse,5).until(EC.visibility_of_element_located((By.XPATH,xpath_confirmed_daily)))
        xpath_confirmed_active = '//div[normalize-space(@class)="level-item is-active fadeInUp"]//h1'
        active_count = WebDriverWait(browse, 5).until(
            EC.visibility_of_element_located((By.XPATH, xpath_confirmed_active)))
        xpath_confirmed_recovered_total = '//div[normalize-space(@class)="level-item is-recovered fadeInUp"]//h1'
        recovered_total_xpath = WebDriverWait(browse, 5).until(
            EC.visibility_of_element_located((By.XPATH, xpath_confirmed_recovered_total)))
        xpath_confirmed_recovered_daily = '//div[normalize-space(@class)="level-item is-recovered fadeInUp"]//h4'
        recovered_daily_xpath = WebDriverWait(browse, 5).until(
            EC.visibility_of_element_located((By.XPATH, xpath_confirmed_recovered_daily)))
        xpath_deceased_total = '//div[normalize-space(@class)="level-item is-deceased fadeInUp"]//h1'
        deceased_total_xpath = WebDriverWait(browse, 5).until(
            EC.visibility_of_element_located((By.XPATH, xpath_deceased_total)))
        xpath_deceased_daily = '//div[normalize-space(@class)="level-item is-deceased fadeInUp"]//h4'
        deceased_daily_xpath = WebDriverWait(browse, 5).until(
            EC.visibility_of_element_located((By.XPATH, xpath_deceased_daily)))
        count[0] =Total_count.text
        count[1] = daily_count.text.replace("+","")
        count[2] = active_count.text
        count[3] = recovered_total_xpath.text
        count[4] = recovered_daily_xpath.text.replace("+","")
        count[5] = deceased_total_xpath.text
        count[6] = deceased_daily_xpath.text.replace("+","")
    except NoSuchElementException:
        pass
    except TimeoutException:
        pass
    return count

browser.get('https://web.whatsapp.com')
whatsapp_window = browser.window_handles[0]
group_title = WebDriverWait(browser,20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '._1awRl.copyable-text.selectable-text')))
group_title.click()
#Searching for the target chat window
group_title.send_keys(TARGET)
sleep(2)
group_title.send_keys(Keys.TAB)
sleep(2)


def whatsappmessage(browse,link,wordList=[],n=0):
    browse.switch_to.window(whatsapp_window)
    xpath = '//div[normalize-space(@class)="_1awRl copyable-text selectable-text"][@dir="ltr"][@data-tab="6"]'
    inputWin = WebDriverWait(browse, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
    inputWin.click()
    if n==1:
        link = link.lower().replace("meaning of","")
        inputWin.send_keys("Definition: "+wordList[0].lower()+Keys.SHIFT+Keys.ENTER+"usage: "+wordList[1])
        inputWin.send_keys(Keys.ENTER)
    elif n==2:
        #text formatting for the COVID status message
        ActionChains(browse) \
            .send_keys("TOTAL CASES: "+ wordList[0].lower())\
            .key_down(Keys.SHIFT) \
            .key_down(Keys.ENTER) \
            .send_keys("day count: ") \
            .key_up(Keys.SHIFT) \
            .key_up(Keys.ENTER) \
            .send_keys(wordList[1]) \
            .key_down(Keys.SHIFT) \
            .key_down(Keys.ENTER) \
            .key_up(Keys.SHIFT) \
            .key_up(Keys.ENTER) \
            .send_keys("*----------------------*") \
            .key_down(Keys.SHIFT) \
            .key_down(Keys.ENTER) \
            .key_up(Keys.SHIFT) \
            .key_up(Keys.ENTER) \
            .send_keys("TOTAL ACTIVE:  "+ wordList[2])\
            .key_down(Keys.SHIFT) \
            .key_down(Keys.ENTER) \
            .key_up(Keys.SHIFT) \
            .key_up(Keys.ENTER) \
            .send_keys("*----------------------*") \
            .key_down(Keys.SHIFT) \
            .key_down(Keys.ENTER) \
            .key_up(Keys.SHIFT) \
            .key_up(Keys.ENTER) \
            .send_keys("TOTAL RECOVERED:  " + wordList[3]) \
            .key_down(Keys.SHIFT) \
            .key_down(Keys.ENTER) \
            .key_up(Keys.SHIFT) \
            .key_up(Keys.ENTER) \
            .send_keys("DAILY RECOVERED:  " + wordList[4]) \
            .key_down(Keys.SHIFT) \
            .key_down(Keys.ENTER) \
            .key_up(Keys.SHIFT) \
            .key_up(Keys.ENTER) \
            .send_keys("*----------------------*") \
            .key_down(Keys.SHIFT) \
            .key_down(Keys.ENTER) \
            .key_up(Keys.SHIFT) \
            .key_up(Keys.ENTER) \
            .send_keys("TOTAL DECEASED:  " + wordList[5]) \
            .key_down(Keys.SHIFT) \
            .key_down(Keys.ENTER) \
            .key_up(Keys.SHIFT) \
            .key_up(Keys.ENTER) \
            .send_keys("DAILY DECEASED:  " + wordList[6]) \
            .perform()
        inputWin.send_keys(Keys.ENTER)
    elif n==3:
        ActionChains(browse) \
            .send_keys("script: " + wordList[0]) \
            .key_down(Keys.SHIFT) \
            .key_down(Keys.ENTER) \
            .key_up(Keys.SHIFT) \
            .key_up(Keys.ENTER) \
            .send_keys("proxy: " +wordList[1]) \
            .perform()
        inputWin.send_keys(Keys.ENTER)
    else:
        inputWin.send_keys(link)
        inputWin.send_keys(Keys.ENTER)

while SCANNED:
    chatMessages = browser.find_elements_by_css_selector("._1VzZY.selectable-text.invisible-space.copyable-text")
    messages = []
    try:
        #reading the latest message in the target chat window
        ##and the codeblock get tiggerred upon keywords(youtube,meaning,Translate and Covid Status)
        x = chatMessages[-1].text
        if "youtube" in x.lower() and "?v=" not in x.lower():
            x = x.lower().replace("youtube ", "")
            print(x)
            inputLink = youtubesearch(browser, x)
            whatsappmessage(browser, inputLink)
        elif "translate" in x.lower():
            inputLink = "Sorry!"
            inputLink= googletranslate(browser,x)
            whatsappmessage(browser, link=x,wordList=inputLink,n=3)
        elif "meaning of" in x.lower():
            words = meaningofWord(browser,x)
            whatsappmessage(browser,link=x,wordList=words,n=1)
        elif "covid status" in x.lower():
            count = covidstatus(browser)
            whatsappmessage(browser,link=x,wordList=count,n=2)
    except NoSuchElementException:
        pass
    sleep(2)

