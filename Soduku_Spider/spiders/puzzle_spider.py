import scrapy
from ..items import SodukuSpiderItem

from time import sleep

class PuzzleSpider(scrapy.Spider):
  name = 'puzzles'
  start_urls = [
    f'https://nine.websudoku.com/?level={lvl}&set_id={puz_num}'
    for lvl in range(1, 4) for puz_num in range(1, 25)
  ]

  def parse(self, response):
    difficulties = {'Easy', 'Medium', 'Hard', 'Evil', 'unknown'}
    category = response.css('p font a[title="Copy link for this puzzle"]::text').extract()[0]
    difficulty = difficulties.intersection(set(category.split(' '))).pop()
    solution = response.css('[name="cheat"]').xpath('@value').extract()[0]
    mask = response.css('[id="editmask"]').xpath('@value').extract()[0]
    puzzle = SodukuSpiderItem(difficulty=difficulty, solution=solution, mask=mask)
    yield puzzle

