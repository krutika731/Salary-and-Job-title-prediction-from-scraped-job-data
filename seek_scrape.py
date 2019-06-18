## Generating a crawler to scrape the data from Ineed for bsiness analyst,data scientist,business intelligence, data analyst and data engineer in ausralia
import scrapy


class seek_job_data(scrapy.Spider):
    name = 'seek_spider'
    start_urls = ['https://www.seek.com.au/data-analyst-scientist-jobs']
    start_urls = ['https://www.seek.com.au/data-jobs-in-information-communication-technology/in-All-Australia?subclassification=6283%2C6286%2C6290']
    def parse(self, response):
       
        job_divs = '//*/article'
        for each_job in response.xpath(job_divs):

            #Getting job title,location,salary and company name from the main page and getting the link for job decription page
            job_title = './/h1/a/text()'
            job_desc_link = './/h1/a/@href'
            link = each_job.xpath(job_desc_link).extract_first()
            location = './/span[@class="_3FrNV7v _3PZrylH E6m4BZb"]//strong[@class="lwHBT6d"]//a[@data-automation="jobLocation"]/text()'
            salary =  './/span[@class="lwHBT6d"]/text()'
            company = './/span[@class="_3FrNV7v _3PZrylH E6m4BZb"]/span/a/text()'
            job_info = {}
            job_info['job_title'] = each_job.xpath(job_title).extract_first()
            job_info['location']= each_job.xpath(location).extract_first()
            job_info['salary'] = each_job.xpath(salary).extract_first()
            job_info['company'] = each_job.xpath(company).extract_first()
            
            #yielding the request to job description page and passing scraped job information to next function
            yield scrapy.Request('https://www.seek.com.au' + link, callback=self.parse_page2, meta={'job_info':job_info})

        
        #getting the link for next page and yeilding a request to next page to get more job data    
        next_page = response.xpath('//*/a[@class="bHpQ-bp"]/@href').extract_first()
  
        if next_page:
            yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse
                )
            
    #function to get job description        
    def parse_page2(self, response):
        print('you are here')
        job_info = response.meta['job_info']
        job_desc = response.xpath('//*/div[@class="tempmargin"]').extract()
        job_info['job_desc'] = job_desc

        #getting the job descriptopn and  combining it with other job information(title,location etc..) and finally yielding this information            
        yield job_info

