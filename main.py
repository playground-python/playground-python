import httpx
# Make a request
r = httpx.get('https://www.example.org/')
print(r.status_code)
