import requests

url = 'https://www.ite.edu.sg/'
r = requests.get(url)
print(r.text)

print("Status code:")
print("\t *", r.status_code)

h = requests.head(url)
print("Header:")
for x in h.headers:
    print("\t ", x, ":", h.headers[x])

headers = {
    'User-Agent':'Mobile'
}
url2 = 'http://httpbin.org/headers'
rh = requests.get(url2, headers=headers)
print(rh.text)
