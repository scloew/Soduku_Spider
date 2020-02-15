import scrapy

class PuzzleSpider(scrapy.Spider):

    name = 'puzzle_spider'
    start_urls = [f'https://nine.websudoku.com/?level=4&set_id={i}' for i in range(75, 77)]
    #TODO currently only points to one puzzle; need it to point to others

    def parse(self, response):
        with open('out.txt', 'a') as f:
          f.write('hello puzzle\n')
          solution = response.css('[name="cheat"]').xpath('@value').extract()[0]
          mask = response.css('[id="editmask"]').xpath('@value').extract()[0]
          f.write(f'{solution}\n')
          f.write(f'{mask}\n')
        yield None
#﻿body table[id="puzzle_grid"] td
#TODO this is the chrome dev  tools css.... but doesn't seem to work here
