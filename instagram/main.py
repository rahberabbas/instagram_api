from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

options = Options()
#options.headless = True`
options.add_argument("--window-size=1920,1080")
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--headless")
# options.add_argument("--disable-gpu")


main_url = 'https://www.instagram.com/tv/CKtHy7RhPh4/?__a=1'
driver = webdriver.Chrome(options=options)
driver.get(main_url)
print(driver.find_element_by_xpath("/html/body").text)
# json_text = driver.find_element_by_css_selector('pre').get_attribute('innerText')
# if json_text:
#     r = json.loads(json_text)
#     video_url = r['graphql']['shortcode_media']['video_url']
#     name = r['graphql']['shortcode_media']['owner']['username']
#     print(video_url)