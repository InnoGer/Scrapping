import requests
from bs4 import BeautifulSoup
from pprint import pprint
from urllib.parse import urljoin

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


###############################################
#######    Ma proposition de correction #######
###############################################

# url = 'https://books.toscrape.com/'

# categories_dict = {}

# with requests.Session() as session:
#     response = session.get(url)
#     soup = BeautifulSoup(response.text, "html.parser")
#     categories_name = soup.find('aside').find('ul').find('li').find('ul')
#     list_cat_name = [chield.text.strip() for chield in categories_name.children if chield.name]
#     hrefs = categories_name.find_all('a')
#     list_cat_href = [urljoin(url, chield['href']) for chield in hrefs]
#     categories_href = {key: value for key, value in zip(list_cat_name, list_cat_href)}
#     Seuil_de_livre = int(input("Afficher les catégories dans un seuil de : "))

#     for key, href in categories_href.items():
#         response_url = session.get(href)
#         soup_url = BeautifulSoup(response_url.text, 'html.parser')
#         liste_livre = soup_url.find('section').find('ol', class_='row')
#         nombre_livre = len([li for li in liste_livre.children])
#         if nombre_livre < Seuil_de_livre:
#             print(f"La catégories '{key}' ne contient que ({nombre_livre}) livres")
#         else:
#             print(f"La catégories '{key}' contient assez de livre ({nombre_livre})")


###############################################
############ # Solution Docstring #############
###############################################

BASE_URL = "https://books.toscrape.com/index.html"


def main(threshold: int = 5):
    with requests.Session() as session:
        response = session.get(BASE_URL)

        soup = BeautifulSoup(response.text, 'html.parser')
        categories = soup.find('ul', class_="nav nav-list").find_all('a')

        # Alternative
        categories = soup.select('ul.nav.nav-list a')
        categories_urls = [category['href'] for category in categories]

        # Go to all categories page
        for category_url in categories_urls:
            full_url = urljoin(BASE_URL, category_url)
            response = session.get(full_url)
            soup = BeautifulSoup(response.text, 'html.parser')

            books = soup.find_all('article', class_="product_pod")
            books = soup.select('article.product_pod')
            category_title = soup.find("h1").text
            number_of_books = len(books)
            if number_of_books <= threshold:
                print(f"La catégorie '{category_title}' ne contient pas assez de livres ({number_of_books})")


if __name__ == '__main__':
    main(threshold=5)



