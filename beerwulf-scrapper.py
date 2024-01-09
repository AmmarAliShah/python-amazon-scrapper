from requests_html import HTMLSession

url = "https://www.target.com/p/400-thread-count-printed-performance-sheet-set-threshold-153/-/A-14220754"
s = HTMLSession()
r = s.get(url)
r.html.render(sleep=1)


dpci = r.html.find('div[data-test="item-details-specifications"]')
for d in dpci:
    print(d.text)

#print(r.status_code)