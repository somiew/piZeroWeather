import bs4 as bs
import urllib.request
import time
import fourletterphat as flp

loop = True

while loop:
    site = urllib.request.urlopen('https://xn--vder24-bua.se/malm%C3%B6/')
    soup = bs.BeautifulSoup(site, 'lxml')

    first_day = soup.find_all(class_="row main-display")

    # create list, find all top temps and append to list
    for i in first_day:
        temp = []
        temp_list = i.find(class_='top_temp')
        temp.append(temp_list.text)

    # fourletterphat-code
    flp.clear()
    flp.print_sting(temp[0] + '°C')
    flp.show()
    
    #print(temp[0] + '°C')
    time.sleep(60)
