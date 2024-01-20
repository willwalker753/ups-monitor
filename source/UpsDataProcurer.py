import websocket
import re
from datetime import datetime, timezone

class UpsDataProcurer:
    def __init__(self, unraidIp:str):
        self.unraidIp = unraidIp

    '''
    @param  (string)  sessionCookie  

    @return  (dict)  
    '''
    def procure(self, sessionCookie):
        url = f'ws://{self.unraidIp}/sub/apcups'
        result = {}

        try:
            ws = websocket.WebSocket()
            
            # Include the session cookie in the WebSocket headers
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Cookie': sessionCookie,
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            }
            ws.connect(url, header=headers)

            # Assume you receive data as a string from the WebSocket
            data_str = ws.recv()

            pattern = r'(\d+ W \(\d+ %\))'
            watts_match = re.search(pattern, data_str)

            if watts_match:
                watts = int(watts_match.group(1).split(' ')[0])
                result = {
                    'watts': watts,
                    'measured_dt': datetime.utcnow().replace(tzinfo=timezone.utc).isoformat()
                }
            else:
                raise Exception('Power information not found in the WebSocket data.')

        except Exception as e:
            print(f'Error in procure method: {e}')
            result = {
                'is_error': True,
                'error': str(e),
                'error_dt': datetime.utcnow().replace(tzinfo=timezone.utc).isoformat(),
            }

        finally:
            ws.close()

        return result
