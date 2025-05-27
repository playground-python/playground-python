import httpx
r = httpx.get('https://www.example.org/')
print(r.status_code)
