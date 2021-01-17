from abc import ABCMeta, abstractmethod
# haha
# second time change it


# Main add a comment

class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def excute(self, data):
        pass


class FastStrategy(Strategy):
    def excute(self, data):
        print('using fast method%s' % data)


class SlowStrategy(Strategy):
    def excute(self, data):
        print('using slow method%s' % data)


class Context:
    def __init__(self, strategy, data):
        self.strategy = strategy
        self.data = data

    def set_strategy(self, strategy, data):
        self.strategy = strategy
        self.data = data

    def Do_strategy(self):
        self.strategy.excute(self.data)


s1 = FastStrategy()
s2 = SlowStrategy()
c1 = Context(s1, 'hahaha')
c1.Do_strategy()
c1.set_strategy(s2, 'hehehe')
c1.Do_strategy()
