import requests

class UpsDataProcurer:
    def __init__(self, unraidUrlBase:str):
        self.unraidUrlBase = unraidUrlBase

    def procure(self, sessionCookie:str):
        url = self.unraidUrlBase + '/sub/apcups'
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Cookie': sessionCookie,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        }
        response = requests.get(url, headers=headers)

        # parse the response        
        try:
            print(response.status_code)
            print(response.content)
            print(response.json())
        except Exception as e:
            print(e)
