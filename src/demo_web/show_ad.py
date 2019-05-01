# selenium 설치
# pip install selenium

# 브라우처 driver 설치
# - 크롬 드라이브 설치: https://sites.google.com/a/chromium.org/chromedriver/downloads

from selenium import webdriver
import re

# Chorme driver가 설치되어 있는 path
path = './chromedriver.exe'

# Chrome 창 띄우기
driver = webdriver.Chrome(path)
# 사용자의 아이디가 지정되어 있는 url로 접속
driver.get('https://xtvznzjl15.execute-api.us-west-2.amazonaws.com/show?user=23')


##### element가 img src인 경우
# images = driver.find_elements_by_tag_name('img')
# 이미지가 여러개인 경우
# for image in images:
#     img_content = (image.get_attribute('src'))
    # print(image.get_attribute('src'))
# 이미지가 한개인 경우
# img_content = images.get_attribute('src')

##### element가 pre인 경우
images = driver.find_elements_by_tag_name("pre")
# image url 불러오기
img_content = (images[0].text)
# img_content의 양 끝에 "가 있기 때문에 제거
img_content = re.sub('"', '', img_content)
print(img_content)

# 새창 띄워서 이미지 url로 접속하기
driver2 = webdriver.Chrome(path)
driver2.get(img_content)
