import scrapy
from scrapy.exceptions import CloseSpider

class SearchItemSpider(scrapy.Spider):
    name = 'searchitem'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter = 1  # 2. Define a self.counter property


    def start_requests(self):
        while True:
            number = self.counter * 24
            keyword = 'air max'
            item = keyword.strip().replace(" ", "%2B")
            url = f'https://api.nike.com/cic/browse/v2?queryid=products&anonymousId=1DBE8664E320C53A536DE7BDABEC68ED&country=id&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(ID)%26filter%3Dlanguage(en-GB)%26filter%3DemployeePrice(true)%26searchTerms%3D{item}%26anchor%3D{number}%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D24&language=en-GB&localizedRangeStr=%7BlowestPrice%7D%E2%80%94%7BhighestPrice%7D'
            yield scrapy.Request(url)
            self.counter += 1

    def parse(self, response):
        print('this is response', response)
        res = response.json()
        products = res["data"]["products"]["products"]

        if not products:
            raise CloseSpider("There are no products to scrape")

        for product in products:
            yield {
                "title": product["title"],
                "subtitle": product["subtitle"],
                "product_url": f"https://www.nike.com/id/{product['url'][14:]}",
                "image_url": product["images"]["portraitURL"],
                "current_price": product["price"]["currentPrice"],
                "full_price": product["price"]["fullPrice"],
                "discounted" : product["price"]["discounted"]
            }
