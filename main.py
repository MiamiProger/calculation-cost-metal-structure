from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from rich.console import Console
import re
import os


HEADERS = {
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
	'accept': '*/*'
}


def get_html(url):

	session = requests.Session()
	response = session.get(url, headers=HEADERS)

	return response.content


def parser_broomstick(url, type_metal):

	soup = BeautifulSoup(get_html(url), 'html.parser')
	
	table_cost = soup.find_all("table")

	array_cost = []

	for item in table_cost:
		for item_array in type_metal:
			if item.find("th").get_text() == item_array:
				for i in item.find_all("tr"):
					k = 1
					brand = 0
					depth = 0
					array_element = []
					if i.find("th"):
						continue
					else:
						for j in i.find_all("td"):
							if k == 1:
								array_element.append(j.get_text().strip())
								k+=1
								continue
							elif k == 2:
								array_element.append(j.get_text().strip())
								k+=1
								continue
							elif k == 3: 
								k+=1
								continue
							elif k == 4:
								array_element.append(int(j.get_text()))
								k+=1
								continue
						if array_cost != []:
							last_element = array_cost[-1]
							if last_element[0] == array_element[0] and last_element[1] == array_element[1]:
								array_cost.remove(last_element)
								array_cost.append(array_element)
							else:
								array_cost.append(array_element)
						else:
							array_cost.append(array_element)
				continue

	return array_cost


def loading_driver():
	options = Options()
	options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36')
	options.add_argument('--disable-blink-features=AutomationControlled')
	options.headless = True
	driver = webdriver.Chrome(options=options)

	return driver


def weight_calculation_corner(width, height, thickness, length):
	result_weight = ''

	url = 'https://metal-calculator.ru/page/app?&m=1&s=10&mode=partner&partner_key=4HKJKR9922&p=????%203'
	driver = loading_driver()
	try:
		driver.get(url=url)
		thickness_input = driver.find_element_by_name('t') 
		thickness_input.clear()
		thickness_input.send_keys(thickness)
		width_input = driver.find_element_by_name('a') 
		width_input.clear()
		width_input.send_keys(width)
		length_input = driver.find_element_by_name('l') 
		length_input.clear()
		length_input.send_keys(length)
		height_input = driver.find_element_by_name('b') 
		height_input.clear()
		height_input.send_keys(height)

		button_cal = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/form/div/a').click()
		result_weight = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div/div/div[3]/div/div[2]/div[2]/ul/li[2]/div/span[2]').text
		result_weight = result_weight.replace(' ????.', '')
		result_weight = result_weight.replace(',', '.')
		result_weight = result_weight.replace(' ', '')

	except Exception as ex:
		print(ex)
	finally:
		driver.close()
		driver.quit()

	return result_weight


def weight_calculation_square(side, length):
	result_weight = ''

	url = 'https://metal-calculator.ru/page/app?&m=1&s=3&mode=partner&partner_key=4HKJKR9922&p=????%203'
	driver = loading_driver()
	try:
		driver.get(url=url)
		side_input = driver.find_element_by_name('a') 
		side_input.clear()
		side_input.send_keys(side)
		length_input = driver.find_element_by_name('l') 
		length_input.clear()
		length_input.send_keys(length)

		button_cal = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/form/div/a').click()
		result_weight = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div/div/div[3]/div/div[2]/div[2]/ul/li[2]/div/span[2]').text
		result_weight = result_weight.replace(' ????.', '')
		result_weight = result_weight.replace(',', '.')
		result_weight = result_weight.replace(' ', '')

	except Exception as ex:
		print(ex)
	finally:
		driver.close()
		driver.quit()

	return result_weight


def weight_calculation_circle(side, length):
	result_weight = ''

	url = 'https://metal-calculator.ru/page/app?&m=1&s=4&mode=partner&partner_key=4HKJKR9922&p=????%203'
	driver = loading_driver()
	try:
		driver.get(url=url)
		side_input = driver.find_element_by_name('d') 
		side_input.clear()
		side_input.send_keys(side)
		length_input = driver.find_element_by_name('l') 
		length_input.clear()
		length_input.send_keys(length)

		button_cal = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/form/div/a').click()
		result_weight = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div/div/div[3]/div/div[2]/div[2]/ul/li[2]/div/span[2]').text
		result_weight = result_weight.replace(' ????.', '')
		result_weight = result_weight.replace(',', '.')
		result_weight = result_weight.replace(' ', '')

	except Exception as ex:
		print(ex)
	finally:
		driver.close()
		driver.quit()

	return result_weight


def weight_calculation_strip(width, thickness, length):
	result_weight = ''

	url = 'https://metal-calculator.ru/page/app?&m=1&s=5&mode=partner&partner_key=4HKJKR9922&p=????%203'
	driver = loading_driver()
	try:
		driver.get(url=url)
		thickness_input = driver.find_element_by_name('t') 
		thickness_input.clear()
		thickness_input.send_keys(thickness)
		width_input = driver.find_element_by_name('a') 
		width_input.clear()
		width_input.send_keys(width)
		length_input = driver.find_element_by_name('b') 
		length_input.clear()
		length_input.send_keys(length)

		button_cal = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/form/div/a').click()
		result_weight = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div/div/div[3]/div/div[2]/div[2]/ul/li[2]/div/span[2]').text
		result_weight = result_weight.replace(' ????.', '')
		result_weight = result_weight.replace(',', '.')
		result_weight = result_weight.replace(' ', '')

	except Exception as ex:
		print(ex)
	finally:
		driver.close()
		driver.quit()

	return result_weight


def weight_calculation_sheet(width, thickness, length, amount):
	url = 'https://metal-calculator.ru/page/app?&m=1&s=6&mode=partner&partner_key=4HKJKR9922&p=????%203'
	result_weight = ''

	driver = loading_driver()
	try:
		driver.get(url=url)
		thickness_input = driver.find_element_by_name('t') 
		thickness_input.clear()
		thickness_input.send_keys(thickness)
		width_input = driver.find_element_by_name('a') 
		width_input.clear()
		width_input.send_keys(width)
		length_input = driver.find_element_by_name('b') 
		length_input.clear()
		length_input.send_keys(length)
		amount_input = driver.find_element_by_name('n') 
		amount_input.clear()
		amount_input.send_keys(amount)

		button_cal = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/form/div/a').click()
		result_weight = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div/div/div[3]/div/div[2]/div[2]/ul/li[2]/div/span[2]').text
		result_weight = result_weight.replace(' ????.', '')
		result_weight = result_weight.replace(',', '.')
		result_weight = result_weight.replace(' ', '')

	except Exception as ex:
		print(ex)
	finally:
		driver.close()
		driver.quit()

	return result_weight


def weight_calculation_fittings(length):
	result_weight = ''

	url = 'https://metal-calculator.ru/page/app?&m=1&s=1&mode=partner&partner_key=4HKJKR9922'
	driver = loading_driver()
	try:
		driver.get(url=url)
		length_input = driver.find_element_by_name('l') 
		length_input.clear()
		length_input.send_keys(length)

		button_cal = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/form/div/a').click()
		result_weight = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div/div/div[3]/div/div[2]/div[2]/ul/li[2]/div/span[2]').text
		result_weight = result_weight.replace(' ????.', '')
		result_weight = result_weight.replace(',', '.')
		result_weight = result_weight.replace(' ', '')

	except Exception as ex:
		print(ex)
	finally:
		driver.close()
		driver.quit()

	return result_weight


def weight_calculation_channel(length):
	result_weight = ''

	url = 'https://metal-calculator.ru/page/app?&m=1&s=12&mode=partner&partner_key=4HKJKR9922'
	driver = loading_driver()
	try:
		driver.get(url=url)
		length_input = driver.find_element_by_name('l') 
		length_input.clear()
		length_input.send_keys(length)

		button_cal = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/form/div/a').click()
		result_weight = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div/div/div[3]/div/div[2]/div[2]/ul/li[2]/div/span[2]').text
		result_weight = result_weight.replace(' ????.', '')
		result_weight = result_weight.replace(',', '.')
		result_weight = result_weight.replace(' ', '')

	except Exception as ex:
		print(ex)
	finally:
		driver.close()
		driver.quit()

	return result_weight


def weight_calculation_profile_pipe(width, height, thickness, length):
	result_weight = ''

	url = 'https://metal-calculator.ru/page/app?&m=1&s=9&mode=partner&partner_key=4HKJKR9922&p=????%203'
	driver = loading_driver()
	try:
		driver.get(url=url)
		thickness_input = driver.find_element_by_name('t') 
		thickness_input.clear()
		thickness_input.send_keys(thickness)
		width_input = driver.find_element_by_name('a') 
		width_input.clear()
		width_input.send_keys(width)
		length_input = driver.find_element_by_name('l') 
		length_input.clear()
		length_input.send_keys(length)
		height_input = driver.find_element_by_name('b') 
		height_input.clear()
		height_input.send_keys(height)

		button_cal = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/form/div/a').click()
		result_weight = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div/div/div[3]/div/div[2]/div[2]/ul/li[2]/div/span[2]').text
		result_weight = result_weight.replace(' ????.', '')
		result_weight = result_weight.replace(',', '.')
		result_weight = result_weight.replace(' ', '')

	except Exception as ex:
		print(ex)
	finally:
		driver.close()
		driver.quit()

	return result_weight


def weight_calculation_round_pipe( width, thickness, length):
	result_weight = ''

	url = 'https://metal-calculator.ru/page/app?&m=1&s=8&mode=partner&partner_key=4HKJKR9922&p=????%203'
	driver = loading_driver()
	try:
		driver.get(url=url)
		thickness_input = driver.find_element_by_name('t') 
		thickness_input.clear()
		thickness_input.send_keys(thickness)
		width_input = driver.find_element_by_name('d') 
		width_input.clear()
		width_input.send_keys(width)
		length_input = driver.find_element_by_name('l') 
		length_input.clear()
		length_input.send_keys(length)

		button_cal = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/form/div/a').click()
		result_weight = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div/div/div[3]/div/div[2]/div[2]/ul/li[2]/div/span[2]').text
		result_weight = result_weight.replace(' ????.', '')
		result_weight = result_weight.replace(',', '.')
		result_weight = result_weight.replace(' ', '')

	except Exception as ex:
		print(ex)
	finally:
		driver.close()
		driver.quit()

	return result_weight


def cost_metal_structures():
	console = Console()

	type_metal = input('''????????????????: 1- ????????????????, 2- ??????????????, 3- ????????/????????????, 4- ??????????, 5- ????????/??????????, 6- ?????????? ??????????????, 7- ?????????? ????????????????????, 8- ????????????, 9- ??????????????\n''')
	array_type_metal = []
	if type_metal == '1':
		diameter = input("?????????????????????? ??????????????: ")
		length = input("??????????: ")
		array_type_metal.append('????????????????')
		result_cost = parser_broomstick('https://mc.ru/prices/sortovojprokat.htm', array_type_metal)
		weight_corner = weight_calculation_fittings(diameter, length)
		for item in result_cost:
			if re.search(diameter, item[1]):
				cost_corner = item[2]
				print("???????? ???? 1??: ", cost_corner)
		result = (float(weight_corner) * int(cost_corner))/1000
	elif type_metal == '2':
		side = input("?????????????? ????????????????: ")
		length = input("??????????: ")
		array_type_metal.append('?????????????? ??/??')
		result_cost = parser_broomstick('https://mc.ru/prices/sortovojprokat.htm', array_type_metal)
		weight_corner = weight_calculation_square(side, length)
		for item in result_cost:
			if re.search(side, item[1]):
				cost_corner = item[2]
				print("???????? ???? 1??: ", cost_corner)
		result = (float(weight_corner) * int(cost_corner))/1000
	elif type_metal == '3':
		side = input("?????????????? ??????????: ")
		length = input("??????????: ")
		array_type_metal.append('???????? ??/??')
		result_cost = parser_broomstick('https://mc.ru/prices/sortovojprokat.htm', array_type_metal)
		weight_corner = weight_calculation_circle(side, length)
		for item in result_cost:
			if re.search(side, item[1]):
				cost_corner = item[2]
				print("???????? ???? 1??: ", cost_corner)
				break
		result = (float(weight_corner) * int(cost_corner))/1000
	elif type_metal == '4':
		thickness = input("?????????????? ??????????: ")
		thickness = thickness.replace(',', '.')
		width = input("???????????? ??????????: ")
		length = input("??????????: ")
		array_type_metal.append('???????????? ??/??')
		result_cost = parser_broomstick('https://mc.ru/prices/sortovojprokat.htm', array_type_metal)
		weight_corner = weight_calculation_strip(width, thickness, length)
		for item in result_cost:
			if re.search(width, item[0]) and re.search(thickness, item[1]):
				cost_corner = item[2]
				print("???????? ???? 1??: ", cost_corner)
				break
		result = (float(weight_corner) * int(cost_corner))/1000
	elif type_metal == '5':
		thickness = input("?????????????? ??????????: ")
		thickness = thickness.replace(',', '.')
		width = input("???????????? ??????????: ")
		length = input("?????????? ??????????: ")
		amount = input("????????????????????: ")
		mark = '????3    ??/??????'
		array_type_metal.append('?????????? ???????????????? ??/?? ???????? ????????????????')
		result_cost = parser_broomstick('https://mc.ru/prices/listovojprokat.htm', array_type_metal)
		weight_corner = weight_calculation_sheet(width, thickness, length, amount)
		for item in result_cost:
			if mark == item[0] and item[1] == thickness:
				cost_corner = item[2]
				print("???????? ???? 1??: ", cost_corner)
				break
		result = (float(weight_corner) * int(cost_corner))/1000
	elif type_metal == '6':
		thickness = input("?????????????? ????????????: ")
		thickness = thickness.replace(',', '.')
		width = input("?????????????? ?????????????? ??????????: ")
		length = input("??????????: ")
		array_type_metal.append('?????????? ????????????????????????????')
		result_cost = parser_broomstick('https://mc.ru/prices/truby.htm', array_type_metal)
		weight_corner = weight_calculation_round_pipe( width, thickness, length)
		for item in result_cost:
			if re.search(width, item[0]) and item[1] == thickness:
				cost_corner = item[2]
				print("???????? ???? 1??: ", cost_corner)
				break
		result = (float(weight_corner) * int(cost_corner))/1000
	elif type_metal == '7':
		thickness = input("?????????????? ????????????: ")
		thickness = thickness.replace(',', '.')
		width = input("???????????? ??????????: ")
		height = input("???????????? ??????????: ")
		length = input("??????????: ")
		if width == height:
			array_type_metal.append('?????????? ???????????????????????????? ??????????????')
			size = width
		else:
			array_type_metal.append('?????????? ???????????????????????????? ??????????????')
			size = width+'x'+height

		result_cost = parser_broomstick('https://mc.ru/prices/truby.htm', array_type_metal)
		weight_corner = weight_calculation_profile_pipe(width, height, thickness, length)
		for item in result_cost:
			if item[0] == size and item[1] == thickness:
				cost_corner = item[2]
				print("???????? ???? 1??: ", cost_corner)
				break
		result = (float(weight_corner) * int(cost_corner))/1000
	elif type_metal == '8':
		thickness = input("?????????????? ??????????: ")
		thickness = thickness.replace(',', '.')
		width = input("???????????? ????????????: ")
		height = input("???????????? ????????????: ")
		length = input("??????????: ")
		array_type_metal.append('????????????')
		result_cost = parser_broomstick('https://mc.ru/prices/sortovojprokat.htm', array_type_metal)
		weight_corner = weight_calculation_corner(width, height, thickness, length)
		for item in result_cost:
			if item[0] == width+'x'+height and item[1] == thickness:
				cost_corner = item[2]
				print("???????? ???? 1??: ", cost_corner)
		result = (float(weight_corner) * int(cost_corner))/1000
	elif type_metal == '9':
		diameter = input("?????????? ????????????????: ")
		length = input("??????????: ")
		array_type_metal.append('??????????????')
		result_cost = parser_broomstick('https://mc.ru/prices/sortovojprokat.htm', array_type_metal)
		weight_corner = weight_calculation_channel(length)
		for item in result_cost:
			if re.search(diameter, item[1]):
				cost_corner = item[2]
				print("???????? ???? 1??: ", cost_corner)
		result = (float(weight_corner) * int(cost_corner))/1000

	return result, weight_corner


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def main():
	console = Console()
	print("?????????????????????? ?????????????? ?????????????????? ????????????????????????????????????")
	type_detail = 0

	while True:
		result = 0
		if type_detail == 'q':
			break
		type_detail = input("???????????????????? ?????????????????? ?????? ?????????? ????????????????????????????????????? (y-????, n-??????)\n?????? ???????????? ???? ?????????????????? - q\n")

		if type_detail == 'y':
			col_detail = input("?????????????? ???????????????????? ??????????????: ")
			for item in range(int(col_detail)):
				item_result, weight_corner = cost_metal_structures()
				result += int(item_result)
			console.print("???????? ????????????: ", result, style="bold red")
		elif type_detail == 'n':
			result, weight_corner = cost_metal_structures()
			cls()
			console.print("?????? ????????????: ", weight_corner, style="bold red")
			console.print("???????? ????????????: ", result, style="bold red")


if __name__ == '__main__':
	main()