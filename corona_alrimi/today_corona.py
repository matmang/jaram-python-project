from selenium import webdriver
import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import time


def today_confirm():
    driver = webdriver.Chrome(executable_path=r'.\chromedriver.exe')
    url = 'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun='
    driver.get(url)

    src = driver.page_source
    soup = BeautifulSoup(src, "html.parser")

    confirm_num = soup.select_one('p.inner_value')
    return confirm_num.get_text()


def today_release():
    driver = webdriver.Chrome(executable_path=r'.\chromedriver.exe')
    url = 'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun='
    driver.get(url)

    src = driver.page_source
    soup = BeautifulSoup(src, "html.parser")

    checkup_num = soup.select_one('span.txt_ntc')
    return checkup_num.get_text()


print(today_release())