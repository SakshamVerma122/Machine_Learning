import scrapy

# This is a Spider
class QuotesSpider(scrapy.Spider):
    
    # Name of the spider not necessarily the file name
    name = "quotes_spider"

    # Aloows you to make get or post request to a particular URL
    def start_request():
        
        # List of URL we are going to scarpe data
        URLS =[ 'https://quotes.toscrape.com/page/1/',
            'https://quotes.toscrape.com/page/2/'
             'https://quotes.toscrape.com/page/3/']
        
        # Generator Function
        for url in URLS:
            yield 