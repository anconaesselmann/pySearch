"""
@author Axel Ancona Esselmann
"""
class ProximityQueryTerm():
    def __init__(self, term1, term2, distance):
        self.term1 = term1;
        self.term2 = term2;
        self.distance = int(distance);
    def __str__(self):
        return "ProximityQueryTerm: (" + self.term1 + ", " + self.term2 + ") distance: " + str(self.distance);
