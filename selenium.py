import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
chrome_prefs = {}
options.experimental_options["prefs"] = chrome_prefs
chrome_prefs["profile.default_content_settings"] = {"images": 2}
chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}

options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)
browser.get('https://events.interpark.com/exhibition?exhibitionCode=220120031')
print('로그인후 바로구매후 아무 키나 누르십시오....')

while True:
    input()
    browser.find_element_by_xpath('//*[@id="payMethodNoBankbook"]').click()
    browser.find_element_by_xpath('//*[@id="frmOnlinePayment"]/div/div/table/tbody/tr[3]/td/input').send_keys('QUAN CHUNLAN')
    browser.find_element_by_xpath('//*[@id="bankSelbox"]/option[9]').click()
    browser.find_element_by_xpath('//*[@id="frmReceipt"]/div[1]/div/input[2]').click()
    browser.find_element_by_xpath('//*[@id="agree_check"]').click()
    browser.find_element_by_xpath('//*[@id="order"]/ul/li[1]/a/img').click()
    break

print('구매완료')