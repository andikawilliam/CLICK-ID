import scrapy

class OkezoneSpider(scrapy.Spider): 
	name = "Okezone"	# name of spider

	# Dates of the news pages to scrap
	start_urls = [
	'https://index.okezone.com/bydate/index/2019/09/%d/' % i for i in range(10,21)
	# range of dates start from date 01 - 08
	]

	# Parse for each date page
	def parse(self, response):

		# extract all page links of news
		news_urls = response.css('h4.f17 > a::attr(href)').extract()
		
		# for each  newslink in a page
		for url in news_urls:
			# a request is made, with the parse_details being called
			if url:	
				yield scrapy.Request(url=url, callback=self.parse_details)
		
		# Retrieve next URL
		next_links = response.css('div.pagination-indexs > div > a::text').extract()
		length = len(next_links)

		# Search for the link, iterate for length of link list
		for i in range(0, length):
			if next_links[i] == "Next>":
				index = i
				print('YES')
				
				# if next_paxe_url is not None: #if next page doesnt exist stop				
				next_page_url = response.css('div.pagination-indexs > div > a::attr(href)')[index].extract()
				yield scrapy.Request(url=next_page_url, callback=self.parse)

				break


	# Function to get the information of the news link opened
	def parse_details(self, response):

		""" DATE """
		src_date = response.css('div.namerep > b::text').extract_first()

		date = src_date[:-10] # Minggu 01 September 2019
		date = date.split(' ', 1)[1]

		""" STRIP CONTENT """
		content = response.css('#contentx > p::text').extract()
		content = [text.strip() for text in content]

		yield {
			'title': response.css('div.title > h1::text').extract(),
			# 'source': src_date[:10],
			'source': 'okezone.com',
			'date': date,
			'time': src_date.rsplit(' ', 2)[1], 
			'category': response.css('div.breadcrumb > ul > li > a::text')[1].extract(),
			'sub-category':response.css('div.breadcrumb > ul > li > a::text')[2].extract(),
			'content': content,
			'url': response.request.url
		}