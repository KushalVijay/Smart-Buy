from bs4 import BeautifulSoup
import re
import requests
import time


def flipkartparser(url):
    time.sleep(2)
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
    response = requests.get(url, headers=headers)
    output = []
    htmltext = response.text
    soup = BeautifulSoup(htmltext, 'html.parser')
    brand = soup.find('span', {'class': "_2J4LW6"})
    name = soup.find('span', {'class': "_35KyD6"})
    price = soup.find('div', {'class': "_1vC4OE _3qQ9m1"})
    rating = soup.find('div', {'class': "hGSR34 bqXGTW"})
    try:
        photo = soup.findAll('div', {'class': "_2_AcLJ"})[0].get('style')[21:-1]
    except:
        photo = None
    link = url
    if brand:
        output.append(brand.text)
    else:
        output.append('N/A')
    if name:
        output.append(name.text)
    else:
        output.append('N/A')
    if price:
        output.append(price.text)
    else:
        output.append('N/A')
    if rating:
        output.append(rating.text)
    else:
        output.append('N/A')
    if photo:
        output.append(photo)
    else:
        output.append("images/NA.jpg")
    output.append(link)
    return output


def getproductid(query):
    url = "https://www.flipkart.com/search?q=" + query.lower()
    print("Searching your product at...", url, sep=" ")
    htmltext = requests.get(url).text
    time.sleep(2)
    pattern = re.compile(r"/[/ 0-9 a-z -]+/p/[0-9a-z]{16,16}")  # flipkart product id
    List = re.findall(pattern, htmltext)

    List = list(set(List))

    return List


def ReadAsinflip(query):
    Id = getproductid(query)
    extracted_data = []
    ctr = 0
    for i in Id:
        ctr += 1

        url = "https://www.flipkart.com" + i
        print("Processing: " + url)
        extracted_data.append(flipkartparser(url))
        time.sleep(1)
        if (ctr == 5):
            break

    return extracted_data



