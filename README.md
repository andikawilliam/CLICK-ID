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
The Scrapy Project code. Each publisher has a specific spider code, located in the /Scrapy/News/spider/ directory
