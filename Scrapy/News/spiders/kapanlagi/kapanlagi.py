import scrapy

class KapanlagiSpider(scrapy.Spider): 
	name = "Kapanlagi"	# name of spider

	# Dates of the news pages to scrap
	start_urls = [
	'https://www.kapanlagi.com/index%s.html' % i for i in range(2,25)
	# Kapalangi has no date based index
	# Hence, it is scraped by using a range of index
	]

	# Parse for each date page
	def parse(self, response):

		# extract all page links of news
		news_urls = response.css('li > div.clearfix.link-trigger > a::attr(href)').extract()

		# for each  newslink in a page
		for url in news_urls:
			url = "https://www.kapanlagi.com%s" % url
			# a request is made, with the parse_details being called
			if url:	
				yield scrapy.Request(url=url, callback=self.parse_details)
		
	# Function to get the information of the news link opened
	def parse_details(self, response):

		title = title = response.css('div.headline-detail > h1::text').extract_first()
		title = title.strip()

		src_date = response.css(
			'div.col-dt-headline.clearfix > div > span.date-post.updated::text'
			).extract_first()

		date_time = src_date.rsplit(', ', 1)[1]

		first_content = response.css('div.body-paragraph.clearfix > p::text').extract()
		first_content = [text.strip() for text in first_content]

		second_content = response.css('div.body-paragraph.pagging_on::text').extract()
		second_content = [text.strip() for text in second_content]

		content = first_content	+ second_content

		yield {
			'title': title,
			# 'source': src_date[:10],
			'source': 'kapanlagi.com',
			'date': date_time.rsplit(' ', 1)[0],
			'time': date_time.rsplit(' ', 1)[1],
			'category': response.css('#v5-navigation > a::text')[1].extract(),
			'sub-category': '-',
			'content': content,
			'url': response.request.url
		}