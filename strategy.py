import abc

class Blog:
    def __init__(self, name):
        self.name = name
        self.link = "example.com/blog"
    
    def share_link(self, strategy):
        strategy.share(self.link)

class ShareStrategy(abc.ABC):
    @abc.abstractmethod
    def share(self, link):
        pass

class StrategyEx1(ShareStrategy):
    def share(self, link):
        print(f"example 1: {link}")

class StrategyEx2(ShareStrategy):
    def share(self, link):
        print(f"example 2: {link}")

class StrategyEx3(ShareStrategy):
    def share(self, link):
        print(f"example 3: {link}")

def strategy():
    ex1 = StrategyEx1()
    ex2 = StrategyEx2()
    ex3 = StrategyEx3()

    blog = Blog("new blog")

    blog.share_link(ex1)
    blog.share_link(ex2)
    blog.share_link(ex3)

strategy()
