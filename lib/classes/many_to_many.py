class Article:
    all = [] 
    
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)  

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,value):
        if type(value) != str:
            return
        if len(value) < 5 or len(value) > 50 :
            return
        if hasattr(self,"title"):
            return
        self._title = value

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self,value):
        if isinstance(value, Author):
            self._author = value


    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value
      
        
class Author:
    def __init__(self, name):
        self.name = name
        

    @property
    def name(self):
        return self._name
    

    @name.setter
    def name(self, value):
        if type(value) != str:
            return
        if len(value) == 0 :
            return
        if hasattr(self,"name"):
            return
        self._name = value
        
    
    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        articles = self.articles()
        if not articles:
            return None
        
        categories = [article.magazine.category for article in articles]
        return list(set(categories))

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []

    @property
    def name(self):
        return self._name
    

    @name.setter
    def name(self, value):
        if type(value) != str or len(value) < 2 or len(value) > 16 :
            return
        
        self._name = value

    @property
    def category(self):
        return self._category
    

    @category.setter
    def category(self, value):
        if type(value) != str or len(value) == 0 :
            return
        
        self._category = value





    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass