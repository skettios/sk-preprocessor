import pygments
import pygments.lexers
from pygments.filter import Filter
from pygments.token import Token


class UnwantedFilter(Filter):
    def __init__(self, **options):
        Filter.__init__(self, **options)

    def filter(self, lexer, stream):
        for ttype, value in stream:
            if ttype is Token.Text and (' ' in value or '\n' in value or '\r' in value or '\t' in value):
                continue
            elif ttype is Token.Punctuation:
                continue
            elif ttype.parent is Token.Comment:
                continue
            yield ttype, value


class CPPTokenizer:
    def __init__(self, source):
        lexer = pygments.lexers.get_lexer_by_name('cpp')
        lexer.add_filter(UnwantedFilter())
        self._current = None
        self._previous = None
        self._tokens = iter(pygments.lex(source, lexer))

    def next(self):
        try:
            self._previous = self._current
            self._current = next(self._tokens)
            return self._current[0], self._current[1]
        except StopIteration:
            return None, None

    def prev(self):
        return self._current[0], self._current[1]
