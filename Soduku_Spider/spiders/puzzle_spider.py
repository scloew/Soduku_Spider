import scrapy

class PuzzleSpider(scrapy.Spider):

    name = 'puzzle_spider'
    start_urls = [f'https://nine.websudoku.com/?level={lvl}&set_id={puz_num}' \
                  for lvl in range(1, 5) for puz_num in range(75, 77)]
    #TODO currently only points to one puzzle; need it to point to others

    def parse(self, response):
      difficulties = {'Easy', 'Medium', 'Hard', 'Evil'}
      with open('out.txt', 'a') as f:
        f.write('hello puzzle\n')
        solution = response.css('[name="cheat"]').xpath('@value').extract()[0]
        mask = response.css('[id="editmask"]').xpath('@value').extract()[0]
        category = response.css('p font a[title="Copy link for this puzzle"]::text').extract()[0]
        difficulty = difficulties.intersection(set(category.split(' ')))
        f.write(f'{solution}\n')
        f.write(f'{mask}\n')
        f.write(f'{difficulty.pop()}\n\n')
      yield None
#﻿body table[id="puzzle_grid"] td
#TODO this is the chrome dev  tools css.... but doesn't seem to work here
