# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import openpyxl


class AddToXlsxPipeline:
    def __init__(self):
        self.workbook = None
        self.worksheet = None
        self.current_row_index = 0

    def process_item(self, item, spider):

        values = list(item.values())
        header = list(item.keys())

        if self.current_row_index == 0:
            self.worksheet.append(header)
            self.worksheet.append(values)
        else:
            self.worksheet.append(values)
        
        self.current_row_index += 1

        return item

    
    def open_spider(self, spider):
        self.workbook = openpyxl.Workbook()
        self.worksheet = self.workbook.active
    
    def close_spider(self, spider):
        excel_file = '20231107_airmax.xlsx'
        self.workbook.save(excel_file)
