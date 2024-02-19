import requests    
from bs4 import BeautifulSoup



HOST='https://www.olx.ua/'
URL='https://www.olx.ua/uk/list/q-%D0%B3%D0%BE%D0%B4%D0%B8%D0%BD%D0%BD%D0%B8%D0%BA/'



HEADERS = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

def get_html(url,params=''):
    response=requests.get(url,headers=HEADERS,params=params)
    return response

# print(get_html(URL))

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='css-qfzx1y')
    users_data = []

    

    for item in items:
        link_elem = item.find_next('a', class_='css-rc5s2u')
        link = link_elem.get('href') if link_elem else None
        

        if link:
           link = HOST + link
            

        title_item=item.find_next('h6',class_='css-16v5mdi er34gjf0')
        title=title_item.get_text() if title_item else 'No title'

        price_item=item.find_next('p',class_='css-10b0gli er34gjf0')
        price= price_item.get_text() if price_item else 'No price'

        
        users_data.append({
            'title':title,
            'price':price,
            'link':link
            
            
    })
    return users_data

def save_to_file_olx(data, filename='output.txt'):
    with open(filename, 'w', encoding='utf-8') as file:
        for item in data:
            file.write(f"Title: {item['title']}\n")
            file.write(f"Price: {item['price']}\n")
            file.write(f"Link: {item['link']}\n\n")


html_content = get_html(URL).text
data = get_content(html_content)
save_to_file_olx(data, filename='olx_data.txt')



