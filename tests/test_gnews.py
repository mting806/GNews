import unittest
from gnews import GNews
from time import time
from gnews.utils import utils

class TestGNews(unittest.TestCase):
    def setUp(self):
        # Create a GNews instance with default parameters for testing
        self.gnews = GNews()

    def test_get_news(self):
        # Test that get_news returns a non-empty list of news articles
        key = "Google"
        news_articles = self.gnews.get_news(key)
        self.assertTrue(isinstance(news_articles, list))
        self.assertTrue(len(news_articles) > 0)

    def test_get_top_news(self):
        # Test that get_top_news returns a non-empty list of news articles
        top_news_articles = self.gnews.get_top_news()
        self.assertTrue(isinstance(top_news_articles, list))
        self.assertTrue(len(top_news_articles) > 0)

    def test_get_news_by_topic(self):
        # Test that get_news_by_topic returns a non-empty list of news articles for a valid topic
        topic = "business"
        news_articles = self.gnews.get_news_by_topic(topic)
        self.assertTrue(isinstance(news_articles, list))
        self.assertTrue(len(news_articles) > 0)

    def test_get_news_by_location(self):
        # Test that get_news_by_location returns a non-empty list of news articles for a valid location
        location = "India"
        news_articles = self.gnews.get_news_by_location(location)
        self.assertTrue(isinstance(news_articles, list))
        self.assertTrue(len(news_articles) > 0)

    def test_get_news_by_site_valid(self):
        site = "cnn.com"
        news_articles = self.gnews.get_news_by_site(site)
        self.assertTrue(isinstance(news_articles, list))
        self.assertTrue(len(news_articles) > 0)

    def test_get_news_by_site_invalid(self):
        # Test that get_news_by_site returns an empty list for an invalid site domain
        site = "invalidsite123.com"
        news_articles = self.gnews.get_news_by_site(site)
        self.assertEqual(news_articles, [])

    def test_get_full_article(self):
        pass
        # Test that get_full_article returns a valid article object for a valid URL
        # url = "https://www.bbc.com/news/live/world-us-canada-66248859"
        # article = self.gnews.get_full_article(url)
        # self.assertIsNotNone(article)
        # self.assertTrue(hasattr(article, 'title'))
        # self.assertTrue(hasattr(article, 'text'))

    def test_get_final_url(self):
        # Test that get_final_url returns a valid URL for a valid URL
        topic = "business"
        news_articles = self.gnews.get_news_by_topic(topic)
        t = time()
        self.gnews.get_news(news_articles[1]['url'])
        t0 = time() - t
        
        t = time()
        final_url = utils._get_final_url(news_articles[1]['url'])  # should this be included in time?
        self.gnews.get_news(final_url)
        t1 = time() - t
        self.assertTrue(t1>t0)
        
        t = time()
        self.gnews.get_news_final(news_articles[1]['url'])
        t2 = time() - t
        self.assertTrue(t2<t0)

if __name__ == '__main__':
    unittest.main()
