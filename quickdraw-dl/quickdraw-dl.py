#!/usr/bin/python

import sys
import requests
import json
import ast
import os

def quickdraw(word):
    url = 'https://quickdraw.withgoogle.com/api'

    headers = {}
    headers["Host"] = "quickdraw.withgoogle.com"
    headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"
    headers["Accept"] = "application/json, text/javascript, */*; q=0.01"
    headers["Accept-Language"] = "en-US,en;q=0.5"
    headers["Accept-Encoding"] = "gzip, deflate, br"
    headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
    headers["X-Requested-With"] = "XMLHttpRequest"
    headers["Referer"] = "https://quickdraw.withgoogle.com/"
    headers["Content-Length"] = "27"
    headers["Connection"] = "keep-alive"

    data = {'method': 'gallery', 'word': word}

    r = requests.post(url, headers=headers, data=data)
    
    if r.status_code != 200:
        print("Failed")
        
    os.makedirs("./images", exist_ok=True)
    
    os.makedirs("./images/" + word, exist_ok=True)

    data = json.loads(r.text)

    i = 0

    for trace in data["images"]:
        trace = json.loads('{"trace":'+trace["image"]+'}')["trace"]
        
        target = open("./images/" + word + '/' + str(i) + '.svg', 'w')
        target.truncate()
        target.write('<svg xmlns="http://www.w3.org/2000/svg">\n')

        for stroke in trace:
            d = ' '.join(['%s%d %d' % (['M', 'L'][i>0], x, y) for i, (x, y) in enumerate(zip(stroke[0],stroke[1]))])
            target.write('<path fill="none" stroke-linecap="round" stroke-width="3" stroke="rgba(0,0,0,1.00)" d="'+d+'"/>\n')
            
        target.write('</svg>\n')
        target.close()
        
        i += 1
        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Run as: quickdraw.py [word]")
        exit()
        
    quickdraw(sys.argv[1])
