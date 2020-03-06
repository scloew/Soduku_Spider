import scrapy
from ..items import SodukuSpiderItem


# class Puzzle(scrapy.Item) :
#   difficulty = scrapy.Field()
#   solution = scrapy.Field()
#   mask = scrapy.Field()

class PuzzleSpider(scrapy.Spider):
  name = 'puzzles'
  start_urls = [
    f'https://nine.websudoku.com/?level={lvl}&set_id={puz_num}'
    for lvl in range(1, 5) for puz_num in range(0, 50)
  ]

  def parse(self, response):
    difficulties = {'Easy', 'Medium', 'Hard', 'Evil', 'unknown'}
    category = response.css('p font a[title="Copy link for this puzzle"]::text').extract()[0]
    difficulty = difficulties.intersection(set(category.split(' ')))
    solution = response.css('[name="cheat"]').xpath('@value').extract()[0]
    mask = response.css('[id="editmask"]').xpath('@value').extract()[0]
    puzzle = SodukuSpiderItem()
    puzzle['difficulty'] = difficulty.pop()
    puzzle['solution'] = solution
    puzzle['mask'] = mask
    yield puzzle

