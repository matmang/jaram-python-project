from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import time


def today_confirmTotal():
    driver = webdriver.Chrome(executable_path=r'.\chromedriver.exe')
    url = 'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun='
    driver.get(url)

    src = driver.page_source
    soup = BeautifulSoup(src, "html.parser")

    confirm_num = soup.select_one('p.inner_value')
    return confirm_num.get_text()


def today_confirmNational():
    driver = webdriver.Chrome(executable_path=r'.\chromedriver.exe')
    url = 'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun='
    driver.get(url)

    src = driver.page_source
    soup = BeautifulSoup(src, "html.parser")

    confirm_num = soup.select('p[class*="_"]')[2]
    res = ''
    for i in confirm_num :
        res += i
    return res


def today_confirmOversea():
    driver = webdriver.Chrome(executable_path=r'.\chromedriver.exe')
    url = 'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun='
    driver.get(url)

    src = driver.page_source
    soup = BeautifulSoup(src, "html.parser")

    confirm_num = soup.select('p[class*="_"]')[3]
    res = ''
    for i in confirm_num :
        res += i
    return res


def today_release():
    driver = webdriver.Chrome(executable_path=r'.\chromedriver.exe')
    url = 'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun='
    driver.get(url)

    src = driver.page_source
    soup = BeautifulSoup(src, "html.parser")

    checkup_num = soup.select('span[class*="_"]')[1]
    res = ''
    for i in checkup_num:
        res += i
    return res

def today_quarantine():
    driver = webdriver.Chrome(executable_path=r'.\chromedriver.exe')
    url = 'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun='
    driver.get(url)

    src = driver.page_source
    soup = BeautifulSoup(src, "html.parser")

    quarantine = soup.select('span[class*="_"]')[2]
    res = ''
    for i in quarantine :
        res += i
    return res


def today_dead():
    driver = webdriver.Chrome(executable_path=r'.\chromedriver.exe')
    url = 'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun='
    driver.get(url)

    src = driver.page_source
    soup = BeautifulSoup(src, "html.parser")

    dead = soup.select('span[class*="_"]')[3]
    res = ''
    for i in dead :
        res += i
    return res