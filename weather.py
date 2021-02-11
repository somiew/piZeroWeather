import bs4 as bs
import urllib.request
import time
import fourletterphat as flp

loop = True

while loop:
    site = urllib.request.urlopen('https://xn--vder24-bua.se/malm%C3%B6/')
    soup = bs.BeautifulSoup(site, 'lxml')

    first_day = soup.find_all(class_="row main-display")

    # create empty list
    temp = []

    # find all top temps and append to list
    for i in first_day:
        temp_list = i.find(class_='top_temp')
        temp.append(temp_list.text)

    # try to set degrees, otherwise continue and restart loop
    try:
        degrees = temp[0] + ' C'
    except:
        print('Something went wrong')
        continue

    # fourletterphat-code
    flp.clear()
    flp.print_str(degrees)    # degree sign not available in flp
    flp.show()
    
    print(degrees)    # print to console, because why not
    time.sleep(60)
