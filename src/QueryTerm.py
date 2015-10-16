"""
@author Axel Ancona Esselmann
"""
class QueryTerm():
    def __init__(self, term):
        self.term = term;
    def __str__(self):
        return "QueryTerm: " + self.term;