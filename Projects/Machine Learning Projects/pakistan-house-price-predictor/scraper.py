import requests as REQS
from bs4 import BeautifulSoup as BSOUP
import pandas as PD

def parse_house_price(price: str) -> float:
    PRICE = price
    if PRICE.endswith('Crore'):
        return round(float(PRICE[:-5]) * 10000000)
    elif PRICE.endswith('Lakh'):
        return round(float(PRICE[:-4]) * 100000)
    elif PRICE.endswith('Million'):
        return round(float(PRICE[:-7]) * 1000000)
    elif PRICE.endswith('Arab'):
        return round(float(PRICE[:-4]) * 1000000000)
    elif PRICE.endswith('Thousand'):
        return round(float(PRICE[:-8]) * 1000)
    else:
        return round(float(PRICE))

def parse_house_size(size: str) -> float:
    SIZE = size
    if SIZE.endswith('Marla'):
        return round(float(SIZE[:-5].replace(',', '')) * 225)
    elif SIZE.endswith('Kanal'):
        return round(float(SIZE[:-5].replace(',', '')) * 4500)
    elif SIZE.endswith('Sq. Yd.'):
        return round(float(SIZE[:-7].replace(',', '')) * 9)
    else:
        return round(float(SIZE))

def get_text_from_tag(tag, data_type = 'str'):
    TAG = tag
    DATA_TYPE = data_type
    if TAG is None and DATA_TYPE == 'num':
        return 0
    if DATA_TYPE == 'num':
        try:
            return int(TAG.text.strip())
        except ValueError:
            return 0
        
    if TAG is None and DATA_TYPE == 'str':
        return ''
    if DATA_TYPE == 'str':
        return TAG.text.strip()
    
    if TAG is None and DATA_TYPE == 'price':
        return 0.0
    if DATA_TYPE == 'price':
        return parse_house_price(TAG.text.strip())
    
    if TAG is None and DATA_TYPE == 'size':
        return 0.0
    if DATA_TYPE =='size':
        return parse_house_size(TAG.text.strip())

def scrape(city: str, num_pages: int):
    CITY = city
    NUM_PAGES = num_pages
    HOUSES_INFORMATION = []
    
    for PAGE_NUM in range(1, NUM_PAGES + 1):
        URL = f'https://www.zameen.com/Homes/{CITY}-{PAGE_NUM}.html'
        print(f'\n\tRequested URL: <{URL}>')
        RESPONSE = REQS.get(URL)
        SOUP = BSOUP(RESPONSE.text, 'html.parser')
        HOUSES_LIST = SOUP.select('main > div > div > div > div > ul > li')
        PREVIOUS_HOUSES_INFORMATION_LENGTH = len(HOUSES_INFORMATION)
        
        for HOUSE in HOUSES_LIST:
            BATHROOMS = HOUSE.select_one("span[aria-label='Baths']")
            BEDROOMS = HOUSE.select_one("span[aria-label='Beds']")
            LOCATION = HOUSE.select_one("div[aria-label='Location']")
            PRICE = HOUSE.select_one("span[aria-label='Price']")
            SIZE = HOUSE.select_one("div[title] > div > div > span:nth-child(1)")
            
            if PRICE:
                if SIZE is None:
                    SIZE = LOCATION.parent.select_one(
                        "div:nth-child(2) > div > span:nth-child(3)"
                    )
                HOUSES_INFORMATION.append({
                    'location': get_text_from_tag(LOCATION),
                    'price': get_text_from_tag(tag = PRICE, data_type = 'price'),
                    'bedrooms': get_text_from_tag(tag = BEDROOMS, data_type = 'num'),
                    'bathrooms': get_text_from_tag(tag = BATHROOMS, data_type = 'num'),
                    'size': get_text_from_tag(tag = SIZE, data_type = 'size')
                })
        if len(HOUSES_INFORMATION) == PREVIOUS_HOUSES_INFORMATION_LENGTH:
            break
    return HOUSES_INFORMATION

def main(max_pages: int = 25):
    print('\n<scraper.py>\n')
    
    HOUSES_INFORMATION = []
    
    CITIES = [
        {'id': 1, 'name': 'Lahore'},
        {'id': 2, 'name': 'Karachi'},
        {'id': 3, 'name': 'Islamabad'},
        {'id': 15, 'name': 'Multan'},
        {'id': 16, 'name': 'Faisalabad'},
        {'id': 17, 'name': 'Peshawar'},
        {'id': 18, 'name': 'Quetta'},
        {'id': 41, 'name': 'Rawalpindi'},
        {'id': 36, 'name': 'Murree'},
        {'id': 327, 'name': 'Gujranwala'},
        {'id': 1233, 'name': 'Attock'},
        {'id': 3234, 'name': '2_FECHS'}
    ]
    
    for CITY in CITIES:
        HOUSES_INFORMATION.append({
            'city': CITY.get('name'),
            'info': scrape(f"{CITY.get('name')}-{CITY.get('id')}", max_pages)
        })
        
    with open('data.csv', 'w') as FILE:
        FILE.write('city|location|price|bedrooms|baths|size\n')
        for HOUSE in HOUSES_INFORMATION:
            for INFO in HOUSE.get('info'):
                FILE.write(f"{HOUSE.get('city')}|{INFO.get('location')}|{INFO.get('price')}|{INFO.get('bedrooms')}|{INFO.get('bathrooms')}|{INFO.get('size')}\n")

if __name__ == '__main__':
    MAX_PAGES = 100
    main(max_pages = MAX_PAGES)