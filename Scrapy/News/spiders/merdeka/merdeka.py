import scrapy

class MerdekaSpider(scrapy.Spider): 
	name = "Merdeka"	# name of spider

	# Dates of the news pages to scrap
	start_urls = [
	'https://www.merdeka.com/indeks-berita/2019/10/%s/index2.html' % i for i in range(10,20)

	# range of dates start from date 01 - 08
	]

	page = 1 
	# Parse for each date page
	def parse(self, response):

		# extract all page links of news
		news_urls = response.css('ul.mdk-idn-nd-centlist > li > a::attr(href)').extract()

		# for each  newslink in a page
		for url in news_urls:
			# a request is made, with the parse_details being called
			if url:	
				url = "https://www.merdeka.com%s" % url
				yield scrapy.Request(url=url, callback=self.parse_details)
		
		# # Retrieve next URL
		# # self.page = self.page + 1
		# next_page = 'index%s.html' % (self.page)
		# next_page_url = ''

		# if next_page_url is not None: #if next page doesnt exist stop
		# 	yield scrapy.Request(url=next_page_url, callback=self.parse(self.page))


	# Function to get the information of the news link opened
	def parse_details(self, response):

		src_date = response.css('div.col-dt-left > span.date-post::text').extract_first()
		date_time = src_date.rsplit(', ', 1)[1]

		yield {
			'title': response.css('div.mdk-body-detail > div.mdk-dt-headline > h1::text').extract_first(),
			# 'source': src_date[:10],
			'source': 'merdeka.com',
			'date': date_time.rsplit(' ', 1)[0],
			'time': date_time.rsplit(' ', 1)[1],
			'category': response.css('div.mdk-breadcrumb > a::text')[1].extract(),
			'sub-category': '-',
			'content': response.css('div.mdk-body-paragraph > p::text').extract(),
			'url': response.request.url
		}