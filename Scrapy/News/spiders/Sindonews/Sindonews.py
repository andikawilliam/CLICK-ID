import scrapy

class SindonewsSpider(scrapy.Spider): 
	name = "SindoNews"	# name of spider

	# Dates of the news pages to scrap
	start_urls = [
	'https://index.sindonews.com/index/0?t=2019-09-%s' % i for i in range(10,21)
	# range of dates start from date 01 - 08
	]

	# Parse for each date page
	def parse(self, response):

		# extract all page links of news
		news_urls = response.css('div.indeks-title > a::attr(href)').extract()
		
		# for each  newslink in a page
		for url in news_urls:
			# a request is made, with the parse_details being called
			if url:	
				yield scrapy.Request(url=url, callback=self.parse_details)
		
		# Retrieve next URL
		next_page_url = response.css('div.pagination > ul > li > a[rel="next"]::attr(href)').extract_first()

		if next_page_url is not None: #if next page doesnt exist stop
			yield scrapy.Request(url=next_page_url, callback=self.parse)


	# Function to get the information of the news link opened
	def parse_details(self, response):

		src_date = response.css('div.article > time::text').extract_first()
		date_time = src_date.rsplit(', ', 1)[1]

		yield {
			'title': response.css('div.article > h1::text').extract_first(),
			# 'source': src_date[:10],
			'source': 'sindonews.com',
			'date': date_time[:-12],
			'time': date_time[-9:],
			'category': response.css('ul.menu > li.active > a::text').extract_first(),
			'sub-category': response.css('ul.breadcrumb > li > a::text')[1].extract(),
			'content': response.css('#content::text').extract(),
			'url': response.request.url
		}