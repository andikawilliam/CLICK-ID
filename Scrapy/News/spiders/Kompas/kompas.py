import scrapy

class KompasSpider(scrapy.Spider): 
	name = "Kompas"	# name of spider

	# Dates of the news pages to scrap
	start_urls = [
	'https://indeks.kompas.com/?site=all&date=2019-09-%s' % i for i in range(10,21)
	# range of dates start from date 01 - 09
	]

	# Parse for each date page
	def parse(self, response):

		# extract all page links of news
		news_urls = response.css('a.article__link::attr(href)').extract() 
		
		# for each  newslink in a page
		for url in news_urls:
			# a request is made, with the parse_details being called
			if url:	
				yield scrapy.Request(url=url, callback=self.parse_details)
		
		# There is a change of css selector starting in page number 4, where there are 2 paging_link--next
		# To circumvate we need to check whether it is actually 'Next' or not
		next_page = response.css('a.paging__link.paging__link--next::text')[0].extract()
		
		# Retrieve the next URL
		if (next_page != 'Next'):
			next_page_url = response.css('a.paging__link.paging__link--next::attr(href)')[1].extract()
		else: 
			next_page_url = response.css('a.paging__link.paging__link--next::attr(href)')[0].extract()
		

		if next_page_url is not None: #if next page doesnt exist stop
			yield scrapy.Request(url=next_page_url, callback=self.parse)


	# Function to get the information of the news link opened
	def parse_details(self, response):
		
		# Retrieves source and date time
		# results in -> 'Kompas.com - 05/10/2019, 21:15 WIB'
		src_date = response.css('div.read__time::text').extract_first()

		category = response.css('li.breadcrumb__item > a > span::text')[1].extract()
		sub_category = response.css('li.breadcrumb__item > a > span::text')[2].extract()

		yield {
			'title': response.css('h1.read__title::text').extract_first(),
			# 'source': src_date[:10],
			'source': 'Kompas.com',
			'date': src_date[13:-11],
			'time': src_date[-9:],
			'category': category,
			'sub-category': sub_category,
			'content': response.css('div.read__content > p::text').extract(),
			'url': response.request.url
		}