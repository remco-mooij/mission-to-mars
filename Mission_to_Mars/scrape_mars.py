# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import requests

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()

    # 1. Find news title and paragraph
    news_url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(news_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    # title and paragraph strings:
    news_title = soup.find_all('div', class_="content_title")[0].text.strip()
    news_p = soup.find_all('div', class_="rollover_description_inner")[0].text.strip()
    
    # 2. Find featured image url
    jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jpl_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    img_data_url = soup.footer.a["data-link"]
    base_url = 'https://www.jpl.nasa.gov'
    browser.visit(base_url + img_data_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    result = soup.find_all('figure', class_='lede')[0]
    img_url = result.a['href']
    
    # featured_img_url string:
    featured_image_url = base_url + img_url
    
#     # 3. Find weather tweet
#     twitter_url = "https://twitter.com/marswxreport?lang=en"
#     # browser.visit(twitter_url)
#     # Function to convert a list to a string,
#     # url: https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/
#     def listToString(list):  
#         str1 = " " 
#         return (str1.join(list)) 
    
#     tweet_list = browser.find_by_css('div > div > div > span')
#     list_of_lists = []
#     for i in tweet_list:
#         twitter_data = i.text
#         data_converted = twitter_data.split('·')
#         list_of_lists.append(data_converted)
#     tweet_data = [''.join(x) for x in list_of_lists]
#     tweet_data = listToString(tweet_data)
#     tweet_list = tweet_data.split("@MarsWxReport")
    
#     # tweet string:
#     mars_weather = tweet_list[2].strip().replace('\n', " ")
    
    # 4. Find Mars facts
    facts_url = "https://space-facts.com/mars/"
    browser.visit(facts_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    # html table:
    html_table = soup.find("table", id="tablepress-p-mars-no-2")
    
    # 5. Find hemispheres image urls
    hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemi_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find_all('a', class_="itemLink product-item")
    links = []
    for i in results:
        try:
            link = i.find_all('h3')
            links.append(link)
        except AttributeError as e:
            print(e)

    link1 = links[1][0].text.strip()
    link2 = links[3][0].text.strip()
    link3 = links[5][0].text.strip()
    link4 = links[7][0].text.strip()

    browser.find_by_text(link1).click()
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    img_url1 = soup.li.a['href']
    browser.visit(hemi_url)

    browser.find_by_text(link2).click()
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    img_url2 = soup.li.a['href']
    browser.visit(hemi_url)

    browser.find_by_text(link3).click()
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    img_url3 = soup.li.a['href']
    browser.visit(hemi_url)

    browser.find_by_text(link4).click()
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    img_url4 = soup.li.a['href']
    browser.visit(hemi_url)
    
    title1 = link1.replace(" Enhanced", "")
    title2 = link2.replace(" Enhanced", "")
    title3 = link3.replace(" Enhanced", "")
    title4 = link4.replace(" Enhanced", "")

    # dictionary with hemisphere titles and urls:
    hemisphere_image_urls = [
        {"title": title1, "img_url": img_url1},
        {"title": title2, "img_url": img_url2},
        {"title": title3, "img_url": img_url3},
        {"title": title4, "img_url": img_url4}
    ]

    dictionary = {
        'featured_image_url': featured_image_url,
#         'mars_weather': mars_weather,
        'mars_facts': html_table,
        'mars_hemispheres': hemisphere_image_urls
    }
    
    browser.quit()

    return dictionary

