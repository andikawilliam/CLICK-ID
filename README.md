# CLICK-ID
This repository contains the files of the CLICK-ID Dataset that was constructed during the author's Undergraduate Thesis; Clickbait Detection for Bahasa Indonesia using Bi-LSTM. 
It is mainly divided into 2 parts, the dataset files and the Scraper code.


### Dataset
The dataset files mainly covers 3 folders;
- raw_articles : the raw data that was scraped from each of the selected publishers
- sample_articles : comprised of the 15,000 sample of article data, with only its title, category, sub-category, and label 
- clickbait_annotated : comprised of the 15,000 sample selected from the article data along with the labels of all 3 annotators
- clickbait_dataset : comprised of the 15,000 sample, only with the labels


### Scraper
The Scrapy Project code for scraping articles from online news publishers. Each publisher has a specific spider code, located in the /Scrapy/News/spider/ directory.
I designed each scraper to collect articles data:
* headline (title)
* publisher (source)
* date published (date)
* time published (time)
* article category (category)
* article sub category (sub-category)
* content

#### Notes on Article Data
1. Not all articles have date, time, and sub-categories, In this cases it is left as "-".
2. Since every publisher has a different website structure, scraping the content of the article has proven to be the most difficult task out of all. Mostly, content is divided into different <p> tags. However, I've found cases where a publisher implements a different structure for each category. For instance, one category uses <p> tags and the other <div> tags. Furthermore, some websites divides their content into several pages. This means we have to add another redirect method in order to get the next page's content. Because of this, the some content may be missing from the article data.

