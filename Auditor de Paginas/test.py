from pylinkvalidator.api import crawl
crawled_site = crawl("https://agenciamaki.com/")
number_of_crawled_pages = len(crawled_site.pages)
number_of_errors = len(crawled_sites.error_pages)

print ("Number of crawled pages: " + str(number_of_crawled_pages))