from selenium import webdriver
from bs4 import BeautifulSoup
query = ["birds"]
def main():
    driver = webdriver.Chrome()
    driver.get('https://www.youtube.com/results?search_query={}'.format(query[0]))
    content = driver.page_source.encode('utf-8').strip()
    soup =BeautifulSoup(content, 'lxml')
    titles = soup.find_all('a', id = 'video-title')
    descriptions = soup.find_all('div', class_='metadata-snippet-container style-scope ytd-video-renderer style-scope ytd-video-renderer')
    
main()
