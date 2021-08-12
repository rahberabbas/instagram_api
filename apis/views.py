from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt
import json

headers = {
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
        }

@csrf_exempt
def index(request):
    if request.method == "POST":
        url = request.POST.get("url")
        main = "/".join(url.split("/")[:-1])
        main_url = f"{main}/?__a=1"
        response = requests.get(main_url, headers=headers)
        if response.ok:
            r = response.json()
            pic_url = r['graphql']['user']['profile_pic_url_hd']
            name = r['graphql']['shortcode_media']['owner']['username']
            print(pic_url)
        return JsonResponse({'url': pic_url, 'username': name})
    return JsonResponse({"HELLO": "SIR"})

@csrf_exempt
def posts(request):
    if request.method == "POST":
        url = request.POST.get("url")
        main = "/".join(url.split("/")[:-1])
        main_url = f"{main}/?__a=1"
        response = requests.get(main_url, headers=headers)
        try:
            if response.ok:
                r = response.json()
                pic_url = r['graphql']['shortcode_media']['edge_sidecar_to_children']['edges']
                name = r['graphql']['shortcode_media']['owner']['username']
                jsonstr = json.dumps(pic_url)
                lst = []
                for i in pic_url:
                    urls = i['node']['display_resources']
                    for j in urls:
                        lst.append(j['src'])
                pic_urls = lst
            return JsonResponse({'urls': pic_urls, 'username': name})
        except:
            if response.ok:
                r = response.json()
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
        try:
            main = "/".join(url.split("/")[:-1])
            main_url = f"{main}/?__a=1"
            response = requests.get(main_url, headers=headers)
            if response.ok:
                r = response.json()
                video_url = r['graphql']['shortcode_media']['video_url']
                name = r['graphql']['shortcode_media']['owner']['username']
                print(video_url)
            return JsonResponse({'url': video_url, 'username': name})
        except:
            main_url = f"{main}?__a=1"
            response = requests.get(main_url, headers=headers)
            if response.ok:
                r = response.json()
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
        response = requests.get(main_url, headers=headers)
        if response.ok:
            r = response.json()
            video_url = r['graphql']['shortcode_media']['video_url']
            name = r['graphql']['shortcode_media']['owner']['username']
            print(video_url)
        return JsonResponse({'url': video_url, 'username': name})
    return JsonResponse({"HELLO": "SIR"})

@csrf_exempt
def status(request):
    if request.method == "POST":
        url = request.POST.get("url")
        main = "/".join(url.split("/")[:-1])
        main_url = f"{main}/?__a=1"
        response = requests.get(main_url, headers=headers)
        if response.ok:
            r = response.json()
            video_url = r['user']['id']
            print(video_url)
        second_url = f'https://www.instagram.com/graphql/query/?query_hash=45246d3fe16ccc6577e0bd297a5db1ab&variables={"highlight_reel_ids":[],"reel_ids":[{video_url}],"location_ids":[],"precomposed_overlay":false}'
        response = requests.get(second_url, headers=headers)
        if response.ok:
            r = response.json()
            video_url = r['data']['reels_media']['display_resources']
            print(video_url)
        return JsonResponse({'url': video_url})
    return JsonResponse({"HELLO": "SIR"})

