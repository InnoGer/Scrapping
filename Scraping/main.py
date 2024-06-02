import re
from typing import List
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

# BASE_URL = "https://books.toscrape.com/index.html"


# def main(threshold: int = 5):
#     with requests.Session() as session:
#         response = session.get(BASE_URL)

#         soup = BeautifulSoup(response.text, 'html.parser')
#         categories = soup.find('ul', class_="nav nav-list").find_all('a')

#         # Alternative
#         categories = soup.select('ul.nav.nav-list a')
#         categories_urls = [category['href'] for category in categories]

#         # Go to all categories page
#         for category_url in categories_urls:
#             full_url = urljoin(BASE_URL, category_url)
#             response = session.get(full_url)
#             soup = BeautifulSoup(response.text, 'html.parser')

#             books = soup.find_all('article', class_="product_pod")
#             books = soup.select('article.product_pod')
#             category_title = soup.find("h1").text
#             number_of_books = len(books)
#             if number_of_books <= threshold:
#                 print(f"La catégorie '{category_title}' ne contient pas assez de livres ({number_of_books})")


############################################################
####  Exercice Récupérer les livre à ne seule étoile #######
############################################################

# BASE_URL = "https://books.toscrape.com/index.html"

# def main():
#     response = get_url()
#     hrefs = analyser_test(response)
#     get_bookID(hrefs)

# def get_url ():  
#     try:
#         response = requests.get(BASE_URL)
#         response.raise_for_status()
#     except requests.exceptions.RequestException as e:
#             print(f"Il y a une erreur lors de l'acces au site : {e}")
#             raise requests.exceptions.RequestException from e
#     return response

# def analyser_test(response):
#     soup = BeautifulSoup(response.text, "html.parser")
#     star_one_book = soup.select("p.One")
#     href = []
#     for book in star_one_book:
#         try:
#             href.append(book.find_next("h3").find("a")['href'])
#         except AttributeError as e:
#             print('Impossible de trouver la balise <h3>')
#             raise AttributeError from e
#         except TypeError as e:
#             print('Impossible de trouver la balise <a>')
#             raise TypeError from e
#         except KeyError as e:
#             print("Impossible de trouver la balise 'href'  ")
#             raise KeyError from e
#     return href

# def get_bookID(hrefs):
#     #Régular expression
#     book_ID = []
#     for href in hrefs:
#         try:
#             ID = re.findall(r"_\d{1,4}", href)[0][1:]
#         except IndexError as e:
#             print("Impossible de trouver l'Id du livre")
#             raise IndexError from e
#         else:
#             book_ID.append(ID)
#     print(book_ID)


############################################################
####  Exercice Récupérer les livre à ne seule étoile #######
############################################################

"""
## Fonctions à coder

Fonction pour récupérer l'URL de la page suivante
    - Récupérérer à partir du HTML directement ou de l'URL ?
Fonction qui à partir de l'uRL d'un livre, va calculerr le prix
Fonction pour récupérer le prix à partir du HTML
Fonction pour récupérer la quantité disponible à partir du HTML
Fonction pour récuérer les URLs de tous les livres de la bibliothèque
Fonction pour récupérer les URLs sur une page spécifique

"""

import sys
from typing import List

from selectolax.parser import HTMLParser
from loguru import logger

logger.remove()

logger.add(f"books.log", 
           level='WARNING', 
           rotation='500kb')

logger.add(sys.stderr, 
           level='INFO')

def get_all_books_urls(url: str) -> List[str]:
    """
    Retourne tous l'url de tous les livres de la bibliothèthe à partir d'un url de départ

    Arguments:
        url {str} -- l'URL de départ
    Returns:
        List[str] -- Tous les urls de toutes les pages
    """
    pass

def get_allbooks_urls_on_page(tree: HTMLParser) -> List[str]:
    """ Trouve l'URL de tous les livres présent sur la page

    Arguments:
        url {str} -- l'objet HTML parser

    Returns:
        List[str] -- La liste des URL de tous les livres sur une page
    """

    pass

def get_next_page_url(tree: HTMLParser) -> str:
    """ Trouver l'URL de la page suivante à partir d'un objet HTMLparser

    Arguments:
        tree {HTMLParser} -- l'Objet HTMLParser de la page

    Returns:
        str -- l'URL de la page suivante
    """

    pass

def get_books_price(url: str) -> float:

    """Calcule la valeur d'un livre à partir de l'url

    Arguments:
        url {str} -- l'URL de la page du livre

    Returns:
        float -- le coût de livre ( prix multiplié par le quantité)
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        tree = HTMLParser(response.text)
        price = get_book_price_from_page(tree=tree)
        quantity = get_book_quantity_from_page(tree=tree)
        return price * quantity
    except requests.exceptions.RequestException as e:
        logger.error(f"Erreur lors de la requete HTML {e}")
        return 0.0

def get_book_price_from_page(tree: HTMLParser) -> float:
    """ trouve le prix d'un livre à partir d'un objet HTML

    Arguments:
        tree {HTMLParser} -- Objet HTML de la page du livre

    Returns:
        float -- le prix du livre
    """
    price_noeud = tree.css_first("p.price_color")
    if price_noeud:
        price_string = price_noeud.text()
    else:
        logger.error(f"Aucun noeud de prix trouver sur la page")
        return 0.0
    try:
        price = re.findall(r"[0-9.]+", "affsdfgsd")[0]
    except IndexError as e:
        logger.error(f'Impossible de trouver le prix du livree {e}')
        return 0.0
    else:
        return float(price)
    

def get_book_quantity_from_page(tree: HTMLParser) -> int:

    """ trouve la quantité d'un livre à partir d'un objet HTML

    Arguments:
        tree {HTMLParser} -- Objet HTML de la page du livre

    Returns:
        float -- la quantité du livre
    """
    quantity_noeud = tree.css_first("p.price_color")
    if price_noeud:
        price_string = price_noeud.text()
    else:
        logger.error(f"Aucun noeud de prix trouver sur la page")
        return 0.0
    try:
        price = re.findall(r"[0-9.]+", "affsdfgsd")[0]
    except IndexError as e:
        logger.error(f'Impossible de trouver le prix du livree {e}')
        return 0.0
    else:
        return float(price)

def main():

    base_url = "https://books.toscrape.com/index.html"

    get_books_price("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")

    # all_books_urls = get_all_books_urls(base_url)
    # total_price = []
    # for url in all_books_urls:
    #     price = get_books_price(url)
    #     total_price.append(price)

    # return sum(total_price)



if __name__ == '__main__':
    main()
