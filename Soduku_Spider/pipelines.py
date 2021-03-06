# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pyodbc


class SodukuSpiderPipeline(object):

    def __init__(self):
        self.conn = pyodbc.connect(
            "Driver={SQL Server};"
            "Server=LAPTOP-B3HSU0AK\LOEWSQL;"
            "Database=SodukuPuzzles;"
            "Trusted_Connection=yes"
        )

    def _insert(self, item):
        print('inserting item')
        cursor = self.conn.cursor()
        cursor.execute(
            'INSERT into Puzzles(difficulty, solution, mask) values(?,?,?);',
            (
                item['difficulty'],
                item['solution'],
                item['mask']
            )
        )
        self.conn.commit()

    def process_item(self, item, spider):
        self._insert(item)
        return item
