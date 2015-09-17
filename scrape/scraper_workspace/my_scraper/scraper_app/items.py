from scrapy.item import Item, Field

class LivingSocialDeal(Item):
    """Living social container for scraped data
       This assumes we know some information about fields
       we will be scraping in advanced
    """
    title = Field()
    link = Field()
    location = Field()
    original_price = Field()
    price = Field()
    end_date = Field()
