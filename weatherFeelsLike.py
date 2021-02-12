import bs4 as bs
import urllib.request
import time
import fourletterphat as flp

loop = True

while loop:
    site = urllib.request.urlopen('https://www.klart.se/se/sk%C3%A5ne-l%C3%A4n/v%C3%A4der-malm%C3%B6/timmar/')
    soup = bs.BeautifulSoup(site, 'lxml')

    # find id 'hour-1_1'
    first_hour = soup.find_all(id="hour-1_1")


    # find all 'col -feelsLike's
    for i in first_hour:
        temp_list = i.find(class_='col -feelsLike')


    # try to set degrees, otherwise continue and restart loop
    try:
        degrees = str(temp_list.text.strip()) + 'C'
    except:
        print('Something went wrong')
        continue

    # fourletterphat-code
    flp.clear()
    flp.print_str(degrees)    # degree sign not available in flp
    flp.show()
    
    print(degrees)    # print to console, because why not
    time.sleep(60)
