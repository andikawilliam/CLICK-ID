import scrapy

class SindonewsSpider(scrapy.Spider): 
	name = "SindoNews"	# name of spider


	news = ['https://www.liputan6.com/news/indeks/2019/09/%s' % i for i in range(10,21)]
	bisnis = ['https://www.liputan6.com/bisnis/indeks/2019/09/%s' % i for i in range(10,21)]
	showbiz = ['https://www.liputan6.com/showbiz/indeks/2019/09/%s' % i for i in range(10,21)]
	bola = ['https://www.liputan6.com/bola/indeks/2019/09/%s' % i for i in range(10,21)]
	# photo = ['https://www.liputan6.com/photo/indeks/2019/09/%s' % i for i in range(10,11)]
	tekno = ['https://www.liputan6.com/tekno/indeks/2019/09/%s' % i for i in range(10,21)]
	# cek_fakta = ['https://www.liputan6.com/cek_fakta/indeks/2019/09/%s' % i for i in range(10,11)]
	hot = ['https://www.liputan6.com/hot/indeks/2019/09/%s' % i for i in range(10,21)]
	disabilitas = ['https://www.liputan6.com/video/indeks/2019/09/%s' % i for i in range(10,21)]
	global_news = ['https://www.liputan6.com/global/indeks/2019/09/%s' % i for i in range(10,21)]
	otomotif = ['https://www.liputan6.com/otomotif/indeks/2019/09/%s' % i for i in range(10,21)]
	regional = ['https://www.liputan6.com/regional/indeks/2019/09/%s' % i for i in range(10,21)]
	lifestyle = ['https://www.liputan6.com/lifestyle/indeks/2019/09/%s' % i for i in range(10,21)]
	properti = ['https://www.liputan6.com/properti/indeks/2019/09/%s' % i for i in range(10,21)]
	health = ['https://www.liputan6.com/health/indeks/2019/09/%s' % i for i in range(10,21)]
	# citizen6 = ['https://www.liputan6.com/citizen6/indeks/2019/09/%s' % i for i in range(10,11)]
	# tv = ['https://www.liputan6.com/tekno/tv/2019/09/%s' % i for i in range(10,11)]

	# Dates of the news pages to scrap
	start_urls = news + bisnis + showbiz + bola + tekno + hot + disabilitas + global_news + otomotif + regional + lifestyle + properti + health
	


	# range of dates start from date 01 - 08
	

	# Parse for each date page
	def parse(self, response):

		# extract all page links of news
		news_urls = response.css('header.articles--rows--item__header > h4 > a::attr(href)').extract()
		
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

		src_date = response.css('time.read-page--header--author__datetime::attr(datetime)').extract_first()
		time = src_date.rsplit(' ', 1)[1]

		yield {
			'title': response.css('header.read-page--header > h1::text').extract_first(),
			'source': 'liputan6.com',
			'date': src_date.rsplit(' ', 1)[0],
			'time': time[:5], # getting rid of the seconds
			'category': response.css('ul.read-page--breadcrumb > li > a > span::text')[1].extract(),
			'sub-category': response.css('ul.read-page--breadcrumb > li > a > span::text')[2].extract(),
			'content': response.css('div.article-content-body__item-content > p::text').extract(),
			'url': response.request.url
		}