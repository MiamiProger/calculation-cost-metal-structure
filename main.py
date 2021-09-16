from bs4 import BeautifulSoup
import requests
import re


HEADERS = {
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
	'accept': '*/*'
}


def get_html(url):

	session = requests.Session()
	response = session.get(url, headers=HEADERS)

	return response.content


def parser_broomstick(url, type_metal, brand, depth):

	soup = BeautifulSoup(get_html(url), 'html.parser')

	table_cost = soup.find_all("table")

	array_cost = []

	for item in table_cost:
		if item.find("th").get_text().lower() == type_metal.lower():
			for i in item.find_all("td"):
				if i.get_text().strip() == brand:
					item_cost = i.findNext().get_text().strip()
					if item_cost == depth:
						array_cost.append(int(i.findNext().findNext().findNext().get_text()))
					elif re.search(depth, item_cost):
						array_cost.append(int(i.findNext().findNext().findNext().get_text()))
			continue

	cost_metal = 0

	for j in array_cost:
		if j > cost_metal:
			cost_metal = j
		elif cost_metal > j:
			continue

	return cost_metal


def main():

	number_type_metal = input('''Выберите: 1- Арматура, 2- Квадрат, 3- Круг/пруток, 4- Лента, 5- Лист/плита, 6- Труба круглая, 7- Труба профильная, 
	8- Уголок, 9- Швеллер\n''')

	if number_type_metal == '1':
		url = 'https://mc.ru/prices/sortovojprokat.htm'
		type_metal = 'АРМАТУРА'
		brand = 'кл А1 Ст3'
		depth = '10'
	elif number_type_metal == '2':
		url = 'https://mc.ru/prices/sortovojprokat.htm'
		type_metal = 'КВАДРАТ Г/К'
		brand = 'Ст3'
		depth = '14'
	elif number_type_metal == '3':
		url = 'https://mc.ru/prices/sortovojprokat.htm'
		type_metal = 'КРУГ Г/К'
		brand = 'Ст3'
		depth = '65'
	elif number_type_metal == '4':
		url = 'https://mc.ru/prices/sortovojprokat.htm'
		type_metal = 'ПОЛОСА Г/К'
		brand = 'Ст3        30'
		depth = '6'
	elif number_type_metal == '5':
		url = 'https://mc.ru/prices/listovojprokat.htm'
		type_metal = 'СТАЛЬ ЛИСТОВАЯ Г/К ОБЫЧ КАЧЕСТВА'
		brand = 'Ст3    н/обр'
		depth = '10'
	elif number_type_metal == '6':
		url = 'https://mc.ru/prices/truby.htm'
		type_metal = 'ТРУБЫ ЭЛЕКТРОСВАРНЫЕ'
		brand = '22'
		depth = '1,5'
	elif number_type_metal == '7':
		url = 'https://mc.ru/prices/truby.htm'
		type_metal = 'ТРУБЫ ЭЛЕКТРОСВАРНЫЕ ПРЯМОУГ'
		brand = '80x60'
		depth = '3'
	elif number_type_metal == '8':
		url = 'https://mc.ru/prices/sortovojprokat.htm'
		type_metal = 'УГОЛОК'
		brand = '40x40'
		depth = '4'
	elif number_type_metal == '9':
		url = 'https://mc.ru/prices/sortovojprokat.htm'
		type_metal = 'ШВЕЛЛЕР'
		brand = '10'
		depth = ''

	result = parser_broomstick(url, type_metal, brand, depth)

	print('Стоимость тонны - '+type_metal+': '+str(result))


if __name__ == '__main__':
	main()