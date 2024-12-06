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
        if type(value) != Author:
            return
        self._author = value
      
        
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
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category


    @property
    def name(self):
        return self._name
    

    @name.setter
    def name(self, value):
        if type(value) != str:
            return
        if len(value) < 2 or len(value) > 16 :
            return
        
        self._name = value

    @property
    def category(self):
        return self._category
    

    @category.setter
    def category(self, value):
        if type(value) != str:
            return
        if len(value) == 0 :
            return
        
        self._category = value





    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass