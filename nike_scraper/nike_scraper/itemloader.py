from itemloaders.processors import TakeFirst, MapCompose
from scrapy.loader import ItemLoader

class NikeItemLoader(ItemLoader):
    default_output_processor = TakeFirst()

    product_url_in = MapCompose(lambda x: "https://www.nike.com/id/" + x)
    