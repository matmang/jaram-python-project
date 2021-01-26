from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome(executable_path = r'C:\Users\jysko\python programming\chromedriver\chromedriver.exe')
url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%BD%94%EB%A1%9C%EB%82%98+%ED%98%84%ED%99%A9&oquery=%EC%BD%94%EB%A1%9C%EB%82%98+%ED%98%84%ED%99%A9&tqi=hs9wBwprvOsssMu%2BeOVssssstmh-256212'
driver.get(url)

src = driver.page_source
soup = BeautifulSoup(src, "html.parser")

confirm_num = soup.select_one('em.info_variation')
print(confirm_num.get_text())