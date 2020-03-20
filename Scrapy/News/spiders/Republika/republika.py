import scrapy
from w3lib.html import remove_tags

class SindonewsSpider(scrapy.Spider): 
	name = "SindoNews"	# name of spider

	# Dates of the news pages to scrap
	start_urls = [
	'https://www.republika.co.id/index/2019/09/%s' % i for i in range(10,21)
	# range of dates start from date 01 - 08
	]

	# Parse for each date page
	def parse(self, response):

		# extract all page links of news
		news_urls = response.css('div.set_subkanal > div.txt_subkanal.txt_index > h2 > a::attr(href)').extract()
		
		# for each  newslink in a page
		for url in news_urls:
			# a request is made, with the parse_details being called
			if url:	
				yield scrapy.Request(url=url, callback=self.parse_details)
		
		# Retrieve next URL
		next_links = response.css('nav[role="navigation"] > a::text').extract()
		length = len(next_links)

		# Search for the link, iterate for length of link list
		for i in range(0, length):
			if next_links[i] == "Next":
				index = i
				
				# if next_paxe_url is not None: #if next page doesnt exist stop	
				next_page_url = response.css('nav[role="navigation"] > a::attr(href)')[index].extract()

				yield scrapy.Request(url=next_page_url, callback=self.parse)

				break


	# Function to get the information of the news link opened
	def parse_details(self, response):
		title_with_tags = response.css('div.wrap_detail_set > h1').extract_first()
		title = remove_tags(title_with_tags)

		category = response.css('div.breadcome > ul > li > a::text')[1].extract()
		sub_category = response.css('div.breadcome > ul > li > a::text')[2].extract()


		src_date = response.css('div.date_detail > p::text').extract_first()
		date_time = src_date.rsplit(' ', 1)[1]

		yield {
			'title': title,
			# 'source': src_date[:10],
			'source': 'republika.co.id',
			'date': src_date.rsplit('  ',2)[1], # Category and subcategory contains -> /n so we need to strip it first
			'time': src_date.rsplit('  ',2)[2],
			'category': category.strip(),
			'sub-category': sub_category.strip(),
			'content': response.css('div.artikel > p::text').extract(),
			'url': response.request.url
		}