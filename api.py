import requests
import config

sess = requests.Session()
sess.headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.132 YaBrowser/22.3.1.892 Yowser/2.5 Safari/537.36',
    'origin': 'https://www.flightradar24.com',
    'referer': 'https://www.flightradar24.com/',
}

def foundFlightByICAO(icao):
    try:
        fid = sess.get(
            'https://www.flightradar24.com/v1/search/web/find',
            params = {
                'limit': 111,
                'query': icao
            }
        ).json()['results'][0]['id']
    
        sid = [a for a in sess.get(
            'https://www.flightradar24.com/v1/search/web/find',
            params = {
                'limit': 111,
                'query': fid
            }
        ).json()['results'] if a['type'] == 'live'][0]['id']
    
        flight = sess.get(
            'http://data-live.flightradar24.com/clickhandler',
            params = {
                'version': '1.5',
                'flight': sid
            }
        ).json()
    
        try:
            image = flight['aircraft']['images']['large'][0]['src']
        except:
            image = 'N/A'
        return {
            'callsign': flight['identification']['callsign'] if flight['identification']['callsign'] else 'N/A',
            'number': flight['identification']['number']['default'] if flight['identification']['number']['default'] else 'N/A',
            'pos': flight['trail'][0] if flight['trail'] else 'N/A',
            'model': flight['aircraft']['model']['text'] if flight['aircraft']['model']['text'] else 'N/A',
            'reg': flight['aircraft']['registration'] if flight['aircraft']['registration'] else 'N/A',
            'origin': '{} ({})'.format(flight['airport']['origin']['position']['region']['city'], flight['airport']['origin']['code']['iata']) if flight['airport']['origin'] else 'N/A',
            'destination': '{} ({})'.format(flight['airport']['destination']['position']['region']['city'] if flight['airport']['destination']['position']['region']['city'] else 'N/A', flight['airport']['destination']['code']['iata'] if flight['airport']['destination']['code']['iata'] else 'N/A') if flight['airport']['destination'] else 'N/A',
            'airline': flight['airline']['short'] if 'short' in flight['airline'] else 'N/A',
            'image': image
        }
    except (KeyError, IndexError, requests.RequestException) as e:
        print(f'[ERROR] Failed to fetch flight {icao}: {e}')
        return None

def prepareResponse(tr = None):
    tracked = requests.get(config.FLIGHTS_URL).json() if not tr else tr
    ret = []

    for flight in tracked:
        fl = foundFlightByICAO(flight)
        ret.append(fl if fl else tracked[flight])

    return ret