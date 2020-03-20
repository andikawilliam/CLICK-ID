import scrapy

class PostMetroSpider(scrapy.Spider): 
	name = "PostMetro"	# name of spider
	# pos metro medan doesnt have a proper index page
	# therefore we attempt to brute force it by getting all the pages manually 
	# brute force
	start_urls = [
	'https://www.posmetro-medan.com',
	'https://www.posmetro-medan.com/search?updated-max=2019-10-18T00%3A50%3A00-07%3A00&max-results=6#PageNo=2',
	'https://www.posmetro-medan.com/search?updated-max=2019-10-16T01%3A28%3A00-07%3A00&max-results=6#PageNo=3',
	'https://www.posmetro-medan.com/search?updated-max=2019-10-13T22%3A08%3A00-07%3A00&max-results=6#PageNo=4',
	'https://www.posmetro-medan.com/search?updated-max=2019-10-11T04%3A08%3A00-07%3A00&max-results=6#PageNo=5',
	'https://www.posmetro-medan.com/search?updated-max=2019-10-08T09%3A39%3A00-07%3A00&max-results=6#PageNo=6',
	'https://www.posmetro-medan.com/search?updated-max=2019-10-07T01%3A25%3A00-07%3A00&max-results=6#PageNo=7',
	'https://www.posmetro-medan.com/search?updated-max=2019-10-04T16%3A31%3A00-07%3A00&max-results=6#PageNo=8',
	'https://www.posmetro-medan.com/search?updated-max=2019-10-01T09%3A04%3A00-07%3A00&max-results=6#PageNo=9',
	'https://www.posmetro-medan.com/search?updated-max=2019-09-28T05%3A45%3A00-07%3A00&max-results=6#PageNo=10',
	'https://www.posmetro-medan.com/search?updated-max=2019-09-26T01%3A03%3A00-07%3A00&max-results=6#PageNo=11',
	'https://www.posmetro-medan.com/search?updated-max=2019-09-24T08%3A36%3A00-07%3A00&max-results=6#PageNo=12',
	'https://www.posmetro-medan.com/search?updated-max=2019-09-20T16%3A17%3A00-07%3A00&max-results=6#PageNo=13',
	'https://www.posmetro-medan.com/search?updated-max=2019-09-09T21%3A06%3A00-07%3A00&max-results=6#PageNo=14',
	'https://www.posmetro-medan.com/search?updated-max=2019-09-07T07%3A55%3A00-07%3A00&max-results=6#PageNo=15',
	'https://www.posmetro-medan.com/search?updated-max=2019-09-04T19%3A59%3A00-07%3A00&max-results=6#PageNo=16',
	'https://www.posmetro-medan.com/search?updated-max=2019-09-02T20%3A40%3A00-07%3A00&max-results=6#PageNo=17',
	'https://www.posmetro-medan.com/search?updated-max=2019-08-31T07%3A27%3A00-07%3A00&max-results=6#PageNo=18',
	'https://www.posmetro-medan.com/search?updated-max=2019-08-29T17%3A45%3A00-07%3A00&max-results=6#PageNo=19',
	'https://www.posmetro-medan.com/search?updated-max=2019-08-27T23%3A12%3A00-07%3A00&max-results=6#PageNo=20',
	'https://www.posmetro-medan.com/search?updated-max=2019-08-19T02%3A43%3A00-07%3A00&max-results=6#PageNo=21',
	'https://www.posmetro-medan.com/search?updated-max=2019-08-14T20%3A15%3A00-07%3A00&max-results=6#PageNo=22',
	'https://www.posmetro-medan.com/search?updated-max=2019-08-13T00%3A45%3A00-07%3A00&max-results=6#PageNo=23',
	'https://www.posmetro-medan.com/search?updated-max=2019-08-09T20%3A32%3A00-07%3A00&max-results=6#PageNo=24',
	'https://www.posmetro-medan.com/search?updated-max=2019-08-07T22%3A13%3A00-07%3A00&max-results=6#PageNo=25',
	'https://www.posmetro-medan.com/search?updated-max=2019-08-05T02%3A22%3A00-07%3A00&max-results=6#PageNo=26',
	'https://www.posmetro-medan.com/search?updated-max=2019-08-03T23%3A50%3A00-07%3A00&max-results=6#PageNo=27',
	'https://www.posmetro-medan.com/search?updated-max=2019-08-02T01%3A03%3A00-07%3A00&max-results=6#PageNo=28',
	'https://www.posmetro-medan.com/search?updated-max=2019-07-31T01%3A52%3A00-07%3A00&max-results=6#PageNo=29',
	'https://www.posmetro-medan.com/search?updated-max=2019-07-29T06%3A50%3A00-07%3A00&max-results=6#PageNo=30',
	'https://www.posmetro-medan.com/search?updated-max=2019-07-28T07%3A30%3A00-07%3A00&max-results=6#PageNo=31',
	'https://www.posmetro-medan.com/search?updated-max=2019-07-25T06%3A56%3A00-07%3A00&max-results=6#PageNo=32',
	'https://www.posmetro-medan.com/search?updated-max=2019-07-23T00%3A35%3A00-07%3A00&max-results=6#PageNo=33',
	'https://www.posmetro-medan.com/search?updated-max=2019-07-21T18%3A39%3A00-07%3A00&max-results=6#PageNo=34',
	'https://www.posmetro-medan.com/search?updated-max=2019-07-19T18%3A04%3A00-07%3A00&max-results=6#PageNo=35',
	'https://www.posmetro-medan.com/search?updated-max=2019-07-18T08%3A01%3A00-07%3A00&max-results=6#PageNo=36',
	'https://www.posmetro-medan.com/search?updated-max=2019-07-17T00%3A12%3A00-07%3A00&max-results=6#PageNo=37',
	'https://www.posmetro-medan.com/search?updated-max=2019-07-15T06%3A36%3A00-07%3A00&max-results=6#PageNo=38',
	'https://www.posmetro-medan.com/search?updated-max=2019-07-14T17%3A56%3A00-07%3A00&max-results=6#PageNo=39',
	'https://www.posmetro-medan.com/search?updated-max=2019-07-14T17%3A56%3A00-07%3A00&max-results=6#PageNo=39',
	'https://www.posmetro-medan.com/search?updated-max=2019-07-08T22%3A58%3A00-07%3A00&max-results=6#PageNo=40',
	'https://www.posmetro-medan.com/search?updated-max=2019-07-06T10%3A08%3A00-07%3A00&max-results=6#PageNo=41',
	'https://www.posmetro-medan.com/search?updated-max=2019-07-02T21%3A12%3A00-07%3A00&max-results=6#PageNo=42',
	'https://www.posmetro-medan.com/search?updated-max=2019-06-28T06%3A00%3A00-07%3A00&max-results=6#PageNo=43',
	'https://www.posmetro-medan.com/search?updated-max=2019-06-26T17%3A58%3A00-07%3A00&max-results=6#PageNo=44',
	'https://www.posmetro-medan.com/search?updated-max=2019-06-22T09%3A34%3A00-07%3A00&max-results=6#PageNo=45',
	'https://www.posmetro-medan.com/search?updated-max=2019-06-20T20%3A33%3A00-07%3A00&max-results=6#PageNo=46',
	'https://www.posmetro-medan.com/search?updated-max=2019-06-18T05%3A29%3A00-07%3A00&max-results=6#PageNo=47',
	'https://www.posmetro-medan.com/search?updated-max=2019-06-01T21%3A02%3A00-07%3A00&max-results=6#PageNo=48',
	'https://www.posmetro-medan.com/search?updated-max=2019-05-22T22%3A11%3A00-07%3A00&max-results=6#PageNo=49',
	'https://www.posmetro-medan.com/search?updated-max=2019-05-13T06%3A42%3A00-07%3A00&max-results=6#PageNo=50',
	]

	# Parse for each date page
	def parse(self, response):

		# extract all page links of news
		news_urls = response.css('h2.post-title.entry-title > a::attr(href)').extract()
		
		# for each  newslink in a page
		for url in news_urls:
			# a request is made, with the parse_details being called
			if url:	
				yield scrapy.Request(url=url, callback=self.parse_details)

	# Function to get the information of the news link opened
	def parse_details(self, response):


		title =  response.css('div.post-head > h1.post-title.entry-title::text').extract_first()

		content = response.css('div.post-body.entry-content > div::text').extract()
		content = [text.strip() for text in content]

		yield {
			'title': title.strip(),
			# 'source': src_date[:10],
			'source': 'posmetro-medan.com',
			'date': response.css('abbr.published.timeago::text').extract_first(),
			'time': '-',
			'category': response.css('span.label-head > a::text').extract_first(),
			'sub-category': '-',
			'content': content,
			'url': response.request.url
		}