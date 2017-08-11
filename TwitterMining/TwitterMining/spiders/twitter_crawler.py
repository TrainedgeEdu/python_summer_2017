import scrapy
# from scrapy.crawler import CrawlerProcess
# from scrapy.utils.project import get_project_settings
#
#
# process = CrawlerProcess(get_project_settings())
#

class TwitterCrawlerSpider(scrapy.Spider):
    name = "twitter_crawler"
    allowed_domains = ["https://twitter.com/","https://twitter.com/SrBachchan"]
    start_urls = ['https://twitter.com/SrBachchan']

    def parse(self, response):
        name=response.css('.ProfileHeaderCard h1 a::text').extract_first()
        user=response.css('.ProfileHeaderCard h2 a span b::text').extract_first()
        status=response.css('.ProfileHeaderCard p::text').extract_first()
        location=response.css('.ProfileHeaderCard-locationText::text').extract_first().strip()
        join=response.css('.ProfileHeaderCard-joinDateText::text').extract_first()
        media=response.css('.PhotoRail-headingText a::text').extract_first().strip()

        print('Name:'+name)
        print('User:'+user)
        print('Status:'+status)
        print('Location:'+location)
        print('Join date:'+join)
        print('Media:'+media)

        i=1
        tweets=response.css('.ProfileTimeline div .stream ol li')
        for items in tweets:
            y=items.css('.tweet .content')
            t_date=y.css('.stream-item-header .time a::attr(title)').extract_first()
            t_lang=y.css('.js-tweet-text-container p::attr(lang)').extract_first()
            if t_lang=="en":
                t_lang="English"
            if t_lang=="hi":
                t_lang="Hindi"

            t_footer=y.css('.stream-item-footer .ProfileTweet-actionList.js-actions')
            t_reply = t_footer.css('.ProfileTweet-action.ProfileTweet-action--reply > button > span > span::text').extract_first()
            #t_retweets=t_footer.css('.ProfileTweet-action.ProfileTweet-action--retweet button span span::text').extract_first()
            #t_likes=t_footer.css('.ProfileTweet-action.ProfileTweet-action--favorite button span span::text').extract_first()

            z=items.css('.tweet .context')
            t_type=z.css('div .js-retweet-text::text').extract_first()
            rt_user=""
            t_at=[]
            if(t_type==None):
                t_type="Tweet"
            else:
                t_type="Retweet"
                rt_user = z.css('div .js-retweet-text a b::text').extract_first()

            if t_type=="Tweet":
                t_at = y.css('.js-tweet-text-container p .twitter-atreply b::text').extract()


            if t_date!=None:
                print("\n{}".format(i))
                i=int(i+1)
                print("Date: {}".format(t_date))
                print("Text Language: {}".format(t_lang))
                print("Replies: {}".format(t_reply))
                # print("Retweets: {}".format(t_retweets))
                # print("Likes: {}".format(t_likes))
                print("Tweet type: {}".format(t_type))
                if t_type=="Retweet":
                    print("Reweet user: {}".format(rt_user))
                print("@mentions: {}".format(t_at))

# process = CrawlerProcess({
#     'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
# })
#
# process.crawl(TwitterCrawlerSpider)
# process.start()