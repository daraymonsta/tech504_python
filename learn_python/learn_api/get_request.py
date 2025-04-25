import requests

post_codes_req = requests.get("https://api.postcodes.io/postcodes/w51nx")

print(post_codes_req)

print(post_codes_req.status_code)
print(post_codes_req.headers)
print(post_codes_req.content)
print(post_codes_req.json())