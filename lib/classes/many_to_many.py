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
    def title(self, new_title):
        if isinstance(new_title, str) and 5 <= len(new_title) <= 50 and not hasattr(self, "_title"):
            self._title = new_title

    def author(self):
        if isinstance(self.author, Author):
            return self.author
    
    def magazine(self):
        if isinstance(self.magazine, Magazine):
            return self.magazine

    def __repr__(self):
        return f'<Article {self.magazine.name}, {self.title}, {self.author.name}>'
        
class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 0 and not hasattr(self, "_name"):
            self._name = new_name
        # else:
        #     raise TypeError

    def articles(self):
        result = []
        for article in Article.all:
            # print(article.author)
            if article.author is self and isinstance(article, Article):
                result.append(article)
        return result

    def magazines(self):
        result = set()
        for article in self.articles():
            result.add(article.magazine)
        return result

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        result = set()
        for magazine in self.magazines():
            result.add(magazine.category)
        if result == set():
            return None
        else:
            return list(result)

    def __repr__(self):
        return f'<Author {self.name}>'

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 2 <= len(new_name) <= 16:
            self._name = new_name

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str) and len(new_category) > 0:
            self._category = new_category

    def articles(self):
        result = []
        for article in Article.all:
            if article.magazine is self:
                result.append(article)
        return result

    def contributors(self):
        result = set()
        for article in self.articles():
            if isinstance(article.author, Author):
                result.add(article.author)
        return result

    def article_titles(self):
        result = []
        for article in self.articles():
            result.append(article.title)
        if result == []:
            return None
        else:
            return result

    def contributing_authors(self):
        result = []
        auth_dict = {}
        for article in self.articles():
            if article.author not in auth_dict:
                auth_dict[article.author] = 1
            else:
                auth_dict[article.author] += 1 
        print(auth_dict[article.author])
        # adding whole dictionary to result, need to remove authors with less than 2 contributions
        if auth_dict[article.author] >= 2:
            result.append(auth_dict)
        return result

    def __repr__(self):
        return f'<Magazine {self.name} {self.category}>'

a1 = Author("Roberto")
a2 = Author("James Joyce")
a3 = Author("Mary Gaitskill")
a4 = Author("Bob")

m1 = Magazine("Thrasher", "Skate")
m2 = Magazine("Economist", "Money")
m3 = Magazine("NY POST", "Trash")
m4 = Magazine("HAI", "Stuff")

art1 = Article(a1, m1, "Jabronis")
art2 = Article(a2, m2, "How to get rich")
art3 = Article(a3, m3, "Subway bad")
art4 = Article(a2, m2, "Stocks")
art5 = Article(a1, m3, "City Bad")
art6 = Article(a2, m1, "Cool stuff")

# print(art1.magazine)

a1.add_article(m1, "spahgetti")

print(m1.contributing_authors())