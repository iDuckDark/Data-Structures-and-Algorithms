"""
https://gist.github.com/ascv/5022712
recursive descent parser
"""
from typing import Generator


class RecursiveDescentParser:
    """A recursive descent parser"""

    def __init__(self, tokens: Generator):
        self.tokens = tokens
        self.curr_tk = next(tokens, "EOF")

    def accept(self, token):
        """return curr_tk if equal to token, else return none"""
        tok = self.curr_tk
        if self.curr_tk != token:
            return None
        self.curr_tk = next(self.tokens, "EOF")
        return tok

    def expect(self, token):
        """return curr_tk if equal to token, else throw error"""
        tok = self.curr_tk
        if not self.accept(token):
            exit(f"expected {token}")
        return tok

    def factor(self):
        """parse factor"""
        if isinstance(self.curr_tk, int):
            result = self.curr_tk
            self.curr_tk = next(self.tokens, "EOF")
        elif self.accept("("):
            result = self.expr()
            self.expect(")")
        else:
            exit("expected number or (")
        return result

    def term(self):
        """parse term"""
        result = self.factor()
        while self.curr_tk in "*/":
            if self.accept("*"):
                result *= self.term()
            elif self.accept("/"):
                result /= self.term()
        return result

    def expr(self):
        """parse expression"""
        result = self.term()
        while self.curr_tk in "+-":
            if self.accept("+"):
                result += self.term()
            elif self.accept("-"):
                result -= self.term()
        return result


def main():
    """test recursive descent parser"""
    tokens = (x for x in [2, "+", 3, "*", 4])
    result = RecursiveDescentParser(tokens).expr()
    print(result)


if __name__ == "__main__":
    main()
