from matchers import *


class Base:
    def matches(self, player):
        return True


class QueryBuilder:
    def __init__(self, stack=Base()):
        self._stack = stack

    def build(self):
        return self._stack

    def playsIn(self, team):
        return QueryBuilder(stack=And(PlaysIn(team), self._stack))

    def hasAtLeast(self, n, type):
        return QueryBuilder(stack=And(HasAtLeast(n, type), self._stack))

    def hasFewerThan(self, n, type):
        return QueryBuilder(stack=And(HasFewerThan(n, type), self._stack))

    def oneOf(self, one, two):
        return QueryBuilder(stack=Or(one, two))

