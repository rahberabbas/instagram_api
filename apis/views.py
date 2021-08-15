from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
#options.headless = True
options.add_argument("--window-size=1920,1080")
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
headers = {
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
        }

@csrf_exempt
def index(request):
    if request.method == "POST":
        url = request.POST.get("url")
        main = "/".join(url.split("/")[:-1])
        main_url = f"{main}/?__a=1"
        driver = webdriver.Chrome(options=options)
        driver.get(main_url)
        json_text = driver.find_element_by_css_selector('pre').get_attribute('innerText')
        r = json.loads(json_text)
        pic_url = r['graphql']['user']['profile_pic_url_hd']
        print(pic_url)
        return JsonResponse({'url': pic_url})
    else:
        return JsonResponse({"HELLO": "SIR"})

@csrf_exempt
def posts(request):
    if request.method == "POST":
        url = request.POST.get("url")
        main = "/".join(url.split("/")[:-1])
        main_url = f"{main}/?__a=1"
        driver = webdriver.Chrome(options=options)
        driver.get(main_url)
        json_text = driver.find_element_by_css_selector('pre').get_attribute('innerText')
        try:
            if json_text:
                r = json.loads(json_text)
                pic_url = r['graphql']['shortcode_media']['edge_sidecar_to_children']['edges']
                name = r['graphql']['shortcode_media']['owner']['username']
                lst = []
                for i in pic_url:
                    urls = i['node']['display_resources']
                    for j in urls:
                        lst.append(j['src'])
                pic_urls = lst
            return JsonResponse({'urls': pic_urls, 'username': name})
        except:
            if json_text:
                r = json.loads(json_text)
                pic_url = r['graphql']['shortcode_media']['display_resources']
                name = r['graphql']['shortcode_media']['owner']['username']
                jsonstr = json.dumps(pic_url)
                lst = []
                for i in pic_url:
                    urls = i['src']
                    lst.append(urls)
                pic_urls = lst
            return JsonResponse({'urls': pic_urls, 'username': name})
    return JsonResponse({"HELLO": "SIR"})
    
@csrf_exempt
def reels(request):
    if request.method == "POST":
        url = request.POST.get("url")
        main = "/".join(url.split("/")[:-1])
        main_url = f"{main}/?__a=1"
        driver = webdriver.Chrome(options=options)
        driver.get(main_url)
        json_text = driver.find_element_by_css_selector('pre').get_attribute('innerText')
        try:
            if json_text:
                r = json.loads(json_text)
                video_url = r['graphql']['shortcode_media']['video_url']
                name = r['graphql']['shortcode_media']['owner']['username']
                print(video_url)
            return JsonResponse({'url': video_url, 'username': name})
        except:
            if json_text:
                r = json.loads(json_text)
                video_url = r['graphql']['shortcode_media']['video_url']
                name = r['graphql']['shortcode_media']['owner']['username']
                print(video_url)
            return JsonResponse({'url': video_url, 'username': name})
    return JsonResponse({"HELLO": "SIR"})

@csrf_exempt
def igtv(request):
    if request.method == "POST":
        url = request.POST.get("url")
        main = "/".join(url.split("/")[:-1])
        main_url = f"{main}/?__a=1"
        driver = webdriver.Chrome(options=options)
        driver.get(main_url)
        json_text = driver.find_element_by_css_selector('pre').get_attribute('innerText')
        if json_text:
            r = json.loads(json_text)
            video_url = r['graphql']['shortcode_media']['video_url']
            name = r['graphql']['shortcode_media']['owner']['username']
            print(video_url)
        return JsonResponse({'url': video_url, 'username': name})
    return JsonResponse({"HELLO": "SIR"})

