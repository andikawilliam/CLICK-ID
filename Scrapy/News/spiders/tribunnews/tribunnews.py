# -*- coding: utf-8 -*-
import scrapy


class TribunnewsSpider(scrapy.Spider):
	name = 'tribunnews'
	# allowed_domains = ['https://www.tribunnews.com']
	
	start_urls = [
	'https://www.tribunnews.com/index-news?date=2019-9-%s' % i for i in range(10,21)
    ]

	def parse(self, response):
		# extract all page links of news
		news_urls = response.css('li.ptb15 > h3.f16.fbo > a::attr(href)').extract()
		
		# for each  newslink in a page
		for url in news_urls:
			# a request is made, with the parse_details being called
			if url:	
				yield scrapy.Request(url=url, callback=self.parse_details)
		
		# Retrieve next URL
		next_links = response.css('div.paging > a::text').extract()
		length = len(next_links)

		# Search for the link, iterate for length of link list
		for i in range(0, length):
			# if next_page_url is not None: #if next page doesnt exist stop
			if next_links[i] == "Next": 
				index = i
				# print('YES')

				next_page_url = response.css('div.paging > a::attr(href)')[index-1].extract()
				# index is -1 because the first link a does not have a link 
				yield scrapy.Request(url=next_page_url, callback=self.parse)
				break

	def parse_details(self,response):
		""" DATE """
		src_date = response.css('div.mt10 > time.grey::text').extract_first()

		# Minggu, 01 September 2019
		date = src_date.split(' ', 1)[1]

		yield {
			'title': response.css('#article > h1::text').extract_first(),
			# 'source': src_date[:10],
			'source': 'tribunnews.com',
			'date': date[:-10],
			'time': src_date.rsplit(' ', 2)[1], 
			'category': response.css('ul > li > h4 > a > span::text')[1].extract(),
			'sub-category':response.css('ul > li > h4 > a > span::text')[1].extract(),
			'content': response.css('div.side-article.txt-article > p::text').extract(),
			'url': response.request.url
		}