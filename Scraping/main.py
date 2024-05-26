import requests
from bs4 import BeautifulSoup
from pprint import pprint

url1 = "https://www.google.com"

#try:
    #url = 'https://www.cetteurlnexistepas'
    #response = requests.get(url)
    #response.raise_for_status()
#except requests.exceptions.HTTPError as errh:
    #print('Http Error : ', errh)
#except requests.exceptions.ConnectionError as errc:
    #print('Error Connecting : ', errc)

#response = requests.get(url)

#with open('Scraping/index.html', 'w') as f:
   # f.write(response.text)


# url2 = "https://books.toscrape.com/"
# response = requests.get(url2)
# soup = BeautifulSoup(response.text, 'html.parser')
# image = soup.find_all('img', alt_="The Black Maria")
# aside = soup.find('div', class_="side_categories")
# categories_div = aside.find("ul").find("li").find("ul")
# categories = [chield.text.strip() for chield in categories_div if chield.name ]

# print(categories)


#for categorie in categories.children:
  #  if categorie.name:
  #          print(categorie.text.strip())


#print(aside.children)

# url2 = "https://books.toscrape.com/"

# response = requests.get(url2)

# soup = BeautifulSoup(response.text, 'html.parser')

# images = soup.find('section').find_all('img')

# for image in images:
#     print(image['src'])

# url = 'https://books.toscrape.com/'

# response = requests.get(url)

# with open('Scraping/index.html', 'w') as f:
#     f.write(response.text)

# with open('Scraping/index.html', 'r') as f:
#     html = f.read()

# soup = BeautifulSoup(html, 'html.parser')

# images = soup.find('section').find_all('img')

# for image in images:
#     print(image.get('src'))


# url2 = "https://books.toscrape.com/"

# response = requests.get(url2)

# soup = BeautifulSoup(response.text, 'html.parser')
# articles = soup.find_all('article', class_='product_pod')

# for image in articles:
#     links = image.find_all('a')
#     if len(links) >= 2:
#         link = links[1]
#         print(link.get('title'))

url = 'https://books.toscrape.com/'

categories_dict = {}

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

categories_name = soup.find('aside').find('ul').find('li').find('ul')

list_cat_name = [chield.text.strip() for chield in categories_name.children if chield.name]

hrefs = categories_name.find_all('a')

list_cat_href = [url + chield['href'] for chield in hrefs]

categories_href = {key: value for key, value in zip(list_cat_name, list_cat_href)}

Seuil_de_livre = int(input("Afficher les catégories qui contiennent moins de : "))

for key, href in categories_href.items():

    response_url = requests.get(href)

    soup_url = BeautifulSoup(response_url.text, 'html.parser')

    liste_livre = soup_url.find('section').find('ol', class_='row')

    nombre_livre = len([li for li in liste_livre.children])

    if nombre_livre < Seuil_de_livre:
        print(key, nombre_livre)






