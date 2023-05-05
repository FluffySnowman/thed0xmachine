import urllib.parse
import http.client


dorks = [
    "intitle:{0}",
    "intext:{0}",
]


query = input("Enter a search query: ")


for dork in dorks:
    search_url = "/search?q=" + urllib.parse.quote(dork.format(query))
    
    conn = http.client.HTTPSConnection("www.google.com")
    conn.request("GET", search_url)
    response = conn.getresponse()
    html = response.read()
    
    start = 0
    while True:
        start_link = html.find(b'<a href="/url?q=', start)
        if start_link == -1:
            break
        end_link = html.find(b'&', start_link + 16)
        link = html[start_link + 16:end_link].decode('utf-8')
        if link.startswith("http"):
            print(link)
        start = end_link
    
    print()  



