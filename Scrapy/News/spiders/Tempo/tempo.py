import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags

class TempoSpider(scrapy.Spider): 
	name = "Tempo"	# name of spider

	# Dates of the news pages to scrap
	start_urls = [
	'https://www.tempo.co/indeks/2019/09/%s' % i for i in range(10,21)
	# range of dates start from date 01 - 08
	]

	# Parse for each date page
	def parse(self, response):

		# extract all page links of news
		news_urls = response.css('ul.wrapper > li > div > div.wrapper.clearfix > a.col::attr(href)').extract()
		
		# for each  newslink in a page
		for url in news_urls:
			# a request is made, with the parse_details being called
			if url:	
				yield scrapy.Request(url=url, callback=self.parse_details)
		
		# TEMPO.CO DOESNT  HAVE A NEXT PAGE, ALL IN ONE PAGE


	# Function to get the information of the news link opened
	def parse_details(self, response):

		title_in = response.css('div.wrapper > article > h1::text').extract_first()

		# to retrieve the date
		src_date = response.css('#date::text').extract_first()
		date_time = src_date.rsplit(', ', 1)[1] # remove the date 

		yield {
			'title': title_in.strip(), 	# Gets rid of /t /r and /n
			# 'source': src_date[:10],
			'source': 'tempo.co',
			'date': date_time[:-10],
			'time': date_time[-9:],
			'category': response.css('li > a > span::text')[1].extract(),
			'sub-category': '-',
			'content': response.css('#isi > p::text').extract(),
			'url': response.request.url,
		}
