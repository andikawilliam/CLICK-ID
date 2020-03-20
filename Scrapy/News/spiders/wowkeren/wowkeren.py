import scrapy

class WowkerenSpider(scrapy.Spider): 
	name = "Wowkeren"	# name of spider

	# Dates of the news pages to scrap
	start_urls = [
	'https://www.wowkeren.com/berita/page/%s/#' % i for i in range(250,401)
	# wowkeren does not keep their news index based on dates
	# rather they are page based, here august 1 news are kept at 401 at 20 october 2019
	# subject to change as the dates changes
	# page 338 is up to 9th september
	]

	# Parse for each date page
	def parse(self, response):

		# extract all page links of news
		news_urls = response.css('div.col-xl-12 > div > div > h3.title-semibold-dark > a::attr(href)').extract()

		# for each  newslink in a page
		for url in news_urls:
			url = response.urljoin(url)
			# -> wowkeren gives a relative url '/berita/tampil/00271031.html'


			# a request is made, with the parse_details being called
			if url:	
				yield scrapy.Request(url=url, callback=self.parse_details)


		"""
		wowkeren per page system index, hence there is no next page
		instead it will be iterated from the start url
		"""

		# Retrieve next URL
		# next_page_url = response.css('div.pagination > ul > li > a[rel="next"]::attr(href)').extract_first()

		# if next_page_url is not None: #if next page doesnt exist stop
		# 	yield scrapy.Request(url=next_page_url, callback=self.parse)


	# Function to get the information of the news link opened
	def parse_details(self, response):

		content = response.css('div.news-details-layout1 > p::text').extract()
		content = [text.strip() for text in content]

		yield {
			'title': response.css('div.breadcrumbs-content > h1::text').extract_first(),

			# 'title': response.css('div.news-details-layout1 > h2::text').extract_first(),
			# 'source': src_date[:10],
			'source': 'wowkeren.com',
			'date': response.css('ul.post-info-dark > li::text')[2].extract(),
			'time': '-',
			'category': response.css('div.topic-box-sm::text').extract_first(),
			'sub-category': '-',
			'content': content,
			'url': response.request.url
		}