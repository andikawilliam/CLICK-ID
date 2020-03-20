import scrapy

class FimelaSpider(scrapy.Spider): 
	name = "FimelaSpider"	# name of spider

	# Dates of the news pages to scrap
	start_urls = [
	# 'https://www.fimela.com/lifestyle-relationship/indeks/2019/09/%s' % i for i in range(10,21)
	# 'https://www.fimela.com/beauty-health/indeks/2019/09/%s' % i for i in range(10,21)
	# 'https://www.fimela.com/news-entertainment/indeks/2019/09/%s' % i for i in range(10,21)
	'https://www.fimela.com/parenting/indeks/2019/09/%s' % i for i in range(10,21)

	]

	# Parse for each date page
	def parse(self, response):

		# extract all page links of news
		news_urls = response.css('a.ui--a.fimela--articles--snippet__title::attr(href)').extract()

		# for each  newslink in a page
		for url in news_urls:
			# a request is made, with the parse_details being called
			if url:	
				yield scrapy.Request(url=url, callback=self.parse_details)
		
		# Retrieve next URL
		next_page_url = response.css('#next::attr(href)').extract_first()

		if next_page_url is not None: #if next page doesnt exist stop
			yield scrapy.Request(url=next_page_url, callback=self.parse)


	# Function to get the information of the news link opened
	def parse_details(self, response):

		date_time = response.css('time::text').extract_first()

		yield {
			'title': response.css('header.read-page--header > h1::text').extract_first(),
			# 'source': src_date[:10],
			'source': 'fimela.com',
			'date': date_time.rsplit(', ', 1)[0],
			'time': date_time.rsplit(', ', 1)[1],
			'category': response.css('p.read-page--header--subtitle::text').extract_first(),
			'sub-category': '-',
			'content': response.css('div.article-content-body__item-content > p::text').extract(),
			'url': response.request.url
		}