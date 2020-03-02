import scrapy
from collections import namedtuple


class Puzzle(scrapy.Item) :
  difficulty = scrapy.Field()
  solution = scrapy.Field()
  mask = scrapy.Field()

class PuzzleSpider(scrapy.Spider):
  name = 'puzzles'
  start_urls = [
    f'https://nine.websudoku.com/?level={lvl}&set_id={puz_num}'
    for lvl in range(1, 2) for puz_num in range(75, 77)
  ]

  def parse(self, response):
    difficulties = {'Easy', 'Medium', 'Hard', 'Evil', 'unknown'}
    category = response.css('p font a[title="Copy link for this puzzle"]::text').extract()[0]
    difficulty = difficulties.intersection(set(category.split(' ')))
    solution = response.css('[name="cheat"]').xpath('@value').extract()[0]
    mask = response.css('[id="editmask"]').xpath('@value').extract()[0]
    puzzle = Puzzle()
    puzzle['difficulty'] = 'easy'
    puzzle['solution'] = solution
    puzzle['mask'] = mask
    with open('out.txt', 'a') as f:
      category = response.css('p font a[title="Copy link for this puzzle"]::text').extract()[0]
      difficulty = difficulties.intersection(set(category.split(' ')))
      solution = response.css('[name="cheat"]').xpath('@value').extract()[0]
      mask = response.css('[id="editmask"]').xpath('@value').extract()[0]
      f.write(f'{difficulty.pop()}\n')
      f.write(f'{solution}\n')
      f.write(f'{mask}\n\n')
    yield puzzle
