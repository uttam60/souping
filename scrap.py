from lib.functions import read_url, souping


url = 'https://www.dealabs.com/groupe/playstation-5'
agent = 'Chrome'
page = read_url(url, agent)
print(page)


has_ps5 = souping(page)
print(has_ps5)