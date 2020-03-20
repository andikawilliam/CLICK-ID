import scrapy

class DetikSportSpider(scrapy.Spider): 
	name = "DetikSport"	# name of spider

	# Dates of the news pages to scrap
	start_urls = [
	# 'https://news.detik.com/indeks/all/1?date=09/%s/2019' % i for i in range(10,11)
	# 'https://finance.detik.com/indeks?date=09/%s/2019' % i for i in range(10,11)
	# 'https://hot.detik.com/indeks/all/1?date=09/0%s/2019' % i for i in range(10,11)

	'https://sport.detik.com/indeks?date=09/%s/2019' % i for i in range(10,30)
	]

	# Parse for each date page
	def parse(self, response):

		# extract all page links of news
		news_urls = response.css('li > article > div.desc_idx.ml10 > a::attr(href)').extract()

		# for each  newslink in a page
		for url in news_urls:
			# a request is made, with the parse_details being called
			if url:	
				yield scrapy.Request(url=url, callback=self.parse_details)
		
		# The next page in detik.com is denoted by '>>' text
		# It doesnt have an identifier of an ID or a Class
		# However, it is always placed at the end of the links 
		# The command below returns an array of the links -> so we use [-1]
		next_page_url = response.css('div.paging2 > a::attr(href)')[-1].extract()

		if next_page_url: #if next page doesnt exist stop
			yield scrapy.Request(url=next_page_url, callback=self.parse)


	# Function to get the information of the news link opened
	def parse_details(self, response):
		

		""" DATE & TIME """
		# Retrieves source and date time
		# results in -> '2019/09/01 23:49:43 WIB'
		src_date = response.css('div.jdl > div.date::text').extract_first()

		if(src_date[4] == '/'):
			date = src_date[:10]
			time =  src_date[11:-7]
		else:
			src_date = src_date.rsplit(', ', 1)[1] 
			src_date = src_date[:-4]

			date = src_date.rsplit(' ', 1)[1] # split into '20:27 WIB'
			time = src_date.rsplit(' ', 1)[0] 	   # retrieves only '20:27'
		
		""" CONTENT """
		div = response.xpath('//div[@class="detail_wrap"]')[0]
		# content = div.xpath('normalize-space(.//div[@class="detail_text"])').extract_first()

		content = div.xpath('normalize-space(.//div[contains(concat(" ", normalize-space(@class), " "), " detail_text ")])').extract_first()
		


		yield {
			'title': response.css('div.jdl > h1::text').extract_first(),
			# 'source': src_date[:10],
			'source': 'detik.com',
			'date': date,
			'time': time,	# detik also lists seconds, but we dont need that
			'category': response.css('div.breadcrumb > a::text')[0].extract(),
			'sub-category': response.css('div.breadcrumb > a::text')[1].extract(),
			# 'content': '-',
			'content': content,
			'url': response.request.url
		}