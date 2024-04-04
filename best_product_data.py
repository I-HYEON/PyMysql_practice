from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdrivermanager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

# chrome webDriver를 설치 및 로드
driver = webdriver.Chrome()

# 특가 탭 열기
driver.get("https://m.ssg.com/page/ranking.ssg")

# 셀렉터 지정

for i in range(4, 6):  # 이미지가 반복되는 숫자 범위를 지정
    image_selector =  f'#__next > div > main > div.css-vooagt > div:nth-child(2) > div:nth-child({i}) > div > div.css-kdwx3d > a > div > div > img'
    name_selector = f'#__next > div > main > div.css-vooagt > div:nth-child(2) > div:nth-child({i}) > div > a > p'
    try:
        # 해당 요소가 로드될 때까지 대기
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, image_selector))
        )
        print("상품 이미지", element.get_attribute('src'))
    except Exception:
        print("상품 이미지를 찾을 수 없습니다.")

driver.quit()


