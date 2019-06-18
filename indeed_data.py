## Generating a crawler to scrape the data from Ineed for bsiness analyst,data scientist,business intelligence, data analyst in ausralia

import scrapy
from bs4 import BeautifulSoup 
import requests


class job_data(scrapy.Spider):
    name = 'jobdata_spider'
    start_urls = ['https://au.indeed.com/jobs?q=data+analyst%2C+data+scientist%2C+business+analyst%2C+business+intelligence%2F&l=australia']
   
    def parse(self, response):
        HTML_response_each_news_link = response.text
        soup = BeautifulSoup(HTML_response_each_news_link,'lxml')
        job_divs = '//*/div[contains(@class, "jobsearch-SerpJobCard unifiedRow")]'
        for each_job in response.xpath(job_divs):

            #Getting job title,location,salary and company name from the main page and getting the link for job decription page
            job_title = './/div[@class="title"]/a/@title'
            job_desc_link = './/div[@class="title"]/a/@href'
            link = each_job.xpath(job_desc_link).extract_first()
            location = './/div[@class="recJobLoc"]/@data-rc-loc'
            salary =  './/span[@class="salary no-wrap"]/text()'

            company = each_job.xpath('.//span[@class="company"]/text()').extract_first().replace('\n','').strip()
            if len(company) == 0:
                company = each_job.xpath('.//span[@class="company"]/a/text()').extract_first().replace('\n','').strip()

            job_info['job_title'] = each_job.xpath(job_title).extract_first()
            job_info['location']= each_job.xpath(location).extract_first()
            job_info['salary'] = str(each_job.xpath(salary).extract_first()).replace('\n    ','').strip()
            job_info['company'] = company
            
            #yielding the request to job description page and passing scraped job information to next function
            yield scrapy.Request(response.urljoin(link), callback=self.parse_page2, meta={'job_info':job_info})
            

        #getting the link for next page and yeilding a request to next page to get more job data    
        HTML_response_each_news_link = response.text
        soup = BeautifulSoup(HTML_response_each_news_link,'lxml')
            
        all_links = soup.find('div',{'class':'pagination'}).find_all('a')
        next_page = all_links[-1].get('href')
  
        if next_page:
            yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse
               )
            
    #function to get job description        
    def parse_page2(self, response):
        
        job_info = response.meta['job_info']
        job_desc = response.xpath('//*/div[@id="jobDescriptionText"]/text()').extract()
        if job_desc == []:
            #print('in if')
            job_info['job_desc'] = response.xpath('//*/div[@id="jobDescriptionText"]').extract()
        else:
            #print('in else')
            job_info['job_desc'] = job_desc

        #getting the job descriptopn and  combining it with other job information(title,location etc..) and finally yielding this information
        yield job_info

            
       
