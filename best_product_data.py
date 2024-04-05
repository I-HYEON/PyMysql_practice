from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.keys import Keys
# import time
import pandas as pd

# chrome webDriver를 설치 및 로드
driver = webdriver.Chrome()

# 특가 탭 열기
driver.get("https://m.ssg.com/page/SpecialPrice.ssg")

# 리스트 생성
bundle_images = []
brand_names = []
bundle_names = []

for i in range(60, 75):  # 이미지가 반복되는 숫자 범위를 지정
    image_selector =  f'#__next > div > main > div.css-vooagt > div:nth-child(2) > div:nth-child({i}) > div > div.css-kdwx3d > a > div > div > img'
    brand_selector = f'#__next > div > main > div.css-vooagt > div:nth-child(2) > div:nth-child({i}) > div > div.css-1jke4yk > a > p > span'
    name_selector = f'#__next > div > main > div.css-vooagt > div:nth-child(2) > div:nth-child({i}) > div > div.css-1jke4yk > a > p'
    try:
        # 해당 요소가 로드될 때까지 대기
        image_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, image_selector))
        )
        try:
            brand_element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, brand_selector))
            )
            brand_text = brand_element.text
        except Exception:
            brand_text = ""  # 빈 문자열 할당

        name_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, name_selector))
        ).text.replace('\n', '')

        # 상품 이름에서 브랜드 문자열의 인덱스 찾기
        brand_index = name_element.find(brand_text)
        # 상품 이름에서 브랜드 문자열 이후의 문자열 가져오기
        if brand_index != -1:  # 브랜드 문자열이 발견되었을 경우에만 처리
            name_text = name_element[:brand_index] + name_element[brand_index + len(brand_text):].strip()
        else:
            name_text = name_element
        image_text = image_element.get_attribute('src')
        print("상품 이미지:", image_text)
        print("상품 브랜드:", brand_text)
        print("상품 이름:", name_text)
        bundle_images.append(image_text)
        brand_names.append(brand_text)
        bundle_names.append(name_text)
    except Exception:
        print("상품을 찾는 중 문제가 발생했습니다")

driver.quit()

data = {'bundle_name': bundle_names, 'bundle_images':bundle_images, 'brand_names':brand_names}

# 데이터프레임 생성
df = pd.DataFrame(data)

# 엑셀 파일로 저장
df.to_excel('특가정보4.xlsx', index=False)



