class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._title = None
        self._author = None
        self._magazine = None
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if hasattr(self, "_title") and self._title is not None:
            return
        if isinstance(value, str) and 5 <= len(value) <= 50:
            self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
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
        if hasattr(self, "_name"):
            return
        if isinstance(value, str) and len(value) > 0:
            self._name = value

    def articles(self):
        return [a for a in Article.all if a.author is self]

    def magazines(self):
        mags = []
        for a in self.articles():
            if a.magazine not in mags:
                mags.append(a.magazine)
        return mags

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        mags = self.magazines()
        if not mags:
            return None
        areas = []
        for m in mags:
            if m.category not in areas:
                areas.append(m.category)
        return areas


class Magazine:
    all = []

    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        return [a for a in Article.all if a.magazine is self]

    def contributors(self):
        authors = []
        for a in self.articles():
            if a.author not in authors:
                authors.append(a.author)
        return authors

    def article_titles(self):
        arts = self.articles()
        if not arts:
            return None
        return [a.title for a in arts]

    def contributing_authors(self):
        counts = {}
        for a in self.articles():
            counts[a.author] = counts.get(a.author, 0) + 1
        many = [author for author, c in counts.items() if c > 2]
        return many if many else None

    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        by_count = {}
        for a in Article.all:
            by_count[a.magazine] = by_count.get(a.magazine, 0) + 1
        return max(by_count, key=by_count.get) if by_count else None