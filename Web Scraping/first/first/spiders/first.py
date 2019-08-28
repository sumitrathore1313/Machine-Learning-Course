
# -*- coding: utf-8 -*-
import scrapy

class BoxSpider(scrapy.Spider):
    name = 'first'

    def start_requests(self):
        url = "https://www.ambitionbox.com/reviews/apple-reviews"
        
        yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        title = response.css('.h1::text').extract_first()
        print(title)
        try:
            all_reviews = response.css('article')
        except:
            pass
        print(len(all_reviews))
        json_data = []
        for review in all_reviews:
            print(len(review.css('div.review_text_wrap_wrap div.review_text_wrap p.review_text::text').extract()))
            temp = {
                'like': review.css('div.review_text_wrap_wrap div.review_text_wrap p.review_text::text').extract()[0],
                'dislike': review.css('div.review_text_wrap_wrap div.review_text_wrap p.review_text::text').extract()[1]
            }
            json_data.append(temp)

        import json
        with open(title+ '.json',
                  'w') as outfile:
            json.dump(json_data, outfile)
