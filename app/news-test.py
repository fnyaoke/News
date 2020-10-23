import unittest
from .models import Articles, Sources

class ArticlesTest(unittest.TestCase):
    '''
    Test class to test the behavior of the class
    '''

    def setUp(self):
        '''
        setUp method that will run before every test
        '''
        self.new_article = Articles("techcrunch","techcrunch","Walter Thompson","Podcast advertising has a business intelligence gap","Widespread misinformation and misconceptions are delaying ad revenue growth for podcast creators, publishers and networks.","http://techcrunch.com/2020/10/08/podcast-advertising-has-a-business-intelligence-gap/","https://techcrunch.com/wp-content/uploads/2020/10/GettyImages-691121157.jpg?w=502","2020-10-08T18:46:00Z","There are sizable, meaningful gaps in the knowledge collection and publication of podcast listening and engagement statistics.")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))


    def test_init(self):
        self.assertEqual(self.new_article.id,"techcrunch")
        self.assertEqual(self.new_article.name,"techcrunch")
        self.assertEqual(self.new_article.author,"Walter Thompson")
        self.assertEqual(self.new_article.title,"Podcast advertising has a business intelligence gap")
        self.assertEqual(self.new_article.description,"Widespread misinformation and misconceptions are delaying ad revenue growth for podcast creators, publishers and networks.")
        self.assertEqual(self.new_article.url,"http://techcrunch.com/2020/10/08/podcast-advertising-has-a-business-intelligence-gap/")
        self.assertEqual(self.new_article.urlToImage,"https://techcrunch.com/wp-content/uploads/2020/10/GettyImages-691121157.jpg?w=502")
        self.assertEqual(self.new_article.publishedAt,"2020-10-08T18:46:00Z")
        self.assertEqual(self.new_article.content,"There are sizable, meaningful gaps in the knowledge collection and publication of podcast listening and engagement statistics.")
if __name__ == '__main__':
    unittest.main()

class SourcesTest(unittest.TestCase):
    '''
    Test class Sources to test the behavior of the class
    '''

    def setUp(self):
        '''
        setUp method that will run before every test
        '''
        self.new_source = Sources ('sports','name','description','http://www.someurldomain.com','sports','english')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Sources))


    def test_init(self):
        self.assertEqual(self.new_source.id,"sports")
        self.assertEqual(self.new_source.name,"name")
        self.assertEqual(self.new_source.description,"Description")
        self.assertEqual(self.new_source.url,"http://www.someurldomain.com")
        self.assertEqual(self.new_source.category,"sports")
        self.assertEqual(self.new_source.language,"English")

if __name__ == '__main__':
    unittest.main()