from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 이미지 차단(로딩속도 단축)
options = webdriver.ChromeOptions()
chrome_prefs = {}
options.experimental_options["prefs"] = chrome_prefs
chrome_prefs["profile.default_content_settings"] = {"images": 2}
chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}

options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)
browser.get('https://www.interpark.com') # 인터파크 주소

print('로그인후 상품페이지에 들어가서 아무 키나 누르십시오....')

while True:
    input()
    browser.find_element_by_xpath('//*[@id="payMethodNoBankbook"]').click() # 무통장입금
    browser.find_element_by_xpath('//*[@id="bankSelbox"]/option[9]').click() # 입금하실은행(신한은행)
    browser.find_element_by_xpath('//*[@id="frmOnlinePayment"]/div/div/table/tbody/tr[3]/td/input').send_keys('입금자명') # 입금자명
    browser.find_element_by_xpath('//*[@id="frmReceipt"]/div[1]/div/input[2]').click() # 현금영수증 신청안함
    browser.find_element_by_xpath('//*[@id="agree_check"]').click() # 결제진행 동의
    browser.find_element_by_xpath('//*[@id="order"]/ul/li[1]/a/img').click() #결제하기
    break

print('구매완료')