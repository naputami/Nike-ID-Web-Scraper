import scrapy
from scrapy.exceptions import CloseSpider


class NewwomenshoesSpider(scrapy.Spider):
    name = 'newwomenshoes'

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter = 0  # Define a self.counter property


    def start_requests(self):
        while True:
            number = self.counter * 24
            url = f'https://api.nike.com/cic/browse/v2?queryid=products&anonymousId=1DBE8664E320C53A536DE7BDABEC68ED&country=id&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(ID)%26filter%3Dlanguage(en-GB)%26filter%3DemployeePrice(true)%26filter%3DattributeIds(16633190-45e5-4830-a068-232ac7aea82c%2C7baf216c-acc6-4452-9e07-39c2ca77ba32%2C53e430ba-a5de-4881-8015-68eb1cff459f)%26anchor%3D{number}%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D24&language=en-GB&localizedRangeStr=%7BlowestPrice%7D%E2%80%94%7BhighestPrice%7D'
            yield scrapy.Request(url)
            self.counter += 1
    
    def parse(self, response):
        print('this is response', response)
        res = response.json()
        products = res["data"]["products"]["products"]

        if not products:
            raise CloseSpider(f'There is no product to be displayed')

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

    