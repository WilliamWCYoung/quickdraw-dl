#!/usr/bin/python

import sys
import requests
import json
import ast
import os
import hashlib

def quickdraw(word):
    url = 'https://quickdraw.withgoogle.com/api'

    headers = {}
    headers["Host"] = "quickdraw.withgoogle.com"
    headers["Accept"] = "application/json, text/javascript, */*; q=0.01"
    headers["Accept-Language"] = "en-US,en;q=0.5"
    headers["Accept-Encoding"] = "gzip, deflate, br"
    headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
    headers["X-Requested-With"] = "XMLHttpRequest"
    headers["Referer"] = "https://quickdraw.withgoogle.com/"
    headers["Connection"] = "keep-alive"

    data = {'method': 'gallery', 'word': word}

    r = requests.post(url, headers=headers, data=data)
    
    if r.status_code != 200:
        print("Failed")
        
    os.makedirs("./images", exist_ok=True)
    
    os.makedirs("./images/" + word, exist_ok=True)

    data = json.loads(r.text)
    
    m = hashlib.md5()
    m.update(r.text.encode('utf-8'))
    
    target = open("./images/" + word + "/" + m.hexdigest()[:5]+'.txt', 'w')
    target.truncate()
    target.write(r.text)
    target.close()


    for trace in data["images"]:
        trace = json.loads('{"trace":'+trace["image"]+'}')["trace"]
        
        min_x = trace[0][0][0]
        min_y = trace[0][1][0]
        
        for stroke in trace:
            for value in stroke[0]:
                if value < min_x:
                    min_x = value
                    
            for value in stroke[1]:
                if value < min_y:
                    min_y = value
        
        
        for i in range(len(trace)):
            for f in range(len(trace[i][0])):
                trace[i][0][f] = trace[i][0][f] - min_x
                trace[i][1][f] = trace[i][1][f] - min_y

        max_x = trace[0][0][0]
        max_y = trace[0][1][0]
        
        for stroke in trace:
            for value in stroke[0]:
                if value > max_x:
                    max_x = value
                    
            for value in stroke[1]:
                if value > max_y:
                    max_y = value
                    
        scale_factor = 600/max_x
        
        for i in range(len(trace)):
            for f in range(len(trace[i][0])):
                trace[i][0][f] = (trace[i][0][f] * scale_factor) + 50
                trace[i][1][f] = (trace[i][1][f] * scale_factor) + 50
        
        width = (max_x*scale_factor)+100
        height = (max_y*scale_factor)+100
        
        file_contents = ""
        
        file_contents += '<svg width="'+str(width)+'" height="'+str(height)+'" viewBox="0 0 '+str(width)+' '+str(height)+'" xmlns="http://www.w3.org/2000/svg">\n'

        for stroke in trace:
            d = ' '.join(['%s%d %d' % (['M', 'L'][i>0], x, y) for i, (x, y) in enumerate(zip(stroke[0],stroke[1]))])
            file_contents += '<path fill="none" stroke-linecap="round" stroke-width="3" stroke="rgba(0,0,0,1.00)" d="'+d+'"/>\n'
            
        file_contents += '</svg>\n'
            
        m.update(file_contents.encode('utf-8'))
        
        target = open("./images/" + word + '/' + m.hexdigest()[:5] + '.svg', 'w')
        target.truncate()
        target.write(file_contents)
        target.close()
        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Run as: quickdraw.py [word]")
        exit()
        
    quickdraw(sys.argv[1])
