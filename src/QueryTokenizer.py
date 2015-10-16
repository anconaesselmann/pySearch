"""
@author Axel Ancona Esselmann
"""
import re
from QueryTerm import QueryTerm;
from ProximityQueryTerm import ProximityQueryTerm;

class QueryTokenizer():
    def tokenize(self, string):
        tokens = [];
        compiledExpression = re.compile(r"""
            (?P<proximityTokens>
                (\d\(.*?\))
            )
            """, re.X|re.S) # Verbose and multi-line flags
        proximityTokens = re.findall(compiledExpression, string)
        for pToken in proximityTokens:
            compiledExpressionPTokens = re.compile(r"""
                (?P<distance>
                    (\d)
                )
                (\()
                (?P<token1>([^\s]+))
                (\s*)
                (?P<token2>([^\)]+))
                """, re.X|re.S) # Verbose and multi-line flags
            parts = re.match(compiledExpressionPTokens, pToken[0]);
            tokens.append(ProximityQueryTerm(parts.group('token1'), parts.group('token2'), parts.group('distance')))
        regularTokens = compiledExpression.sub('', string).split();
        for rToken in regularTokens:
            tokens.append(QueryTerm(rToken));
        return tokens;