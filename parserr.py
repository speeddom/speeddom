from rply import ParserGenerator
from ast import VAR, SUM, Sub


pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN',
             'SEMI_COLON', 'SUM', 'SUB','VAR', 'LAMBDA'],
            precedence=[
                ('left', ['PLUS', 'MINUS']),
                ('left', ['MUL', 'DIV'])
            ]
        )

@pg.production('expression : NUMBER')
def expression_number(p):
        # p is a list of the pieces matched by the right hand side of the
        # rule
        return Number(int(p[0].getstr()))
   
@pg.production('expression : VAR')
def expression_number(p):
        # p is a list of the pieces matched by the right hand side of the
        # rule
        return Number(int(p[0].getstr()))
    
@pg.production('expression : LAMBDA')
def expression_number(p):
        # p is a list of the pieces matched by the right hand side of the
        # rule
        return p[1]
@pg.production('expression : DOT')
def expression_number(p):
        # p is a list of the pieces matched by the right hand side of the
        # rule
        return p[1]
@pg.production('expression : OPEN_PARENS expression CLOSE_PARENS')
def expression_parens(p):
        return p[1]


    
@pg.production('expression : OPEN_PARENS expression CLOSE_PARENS')
def expression_parens(p):
        return p[1]



    
@pg.production('expression : expression PLUS expression')
@pg.production('expression : expression MINUS expression')
@pg.production('expression : expression MUL expression')
@pg.production('expression : expression DIV expression')
def expression_binop(p):
        left = p[0]
        right = p[2]
        if p[1].gettokentype() == 'PLUS':
            return Add(left, right)
        elif p[1].gettokentype() == 'MINUS':
            return Sub(left, right)
        elif p[1].gettokentype() == 'MUL':
            return Mul(left, right)
        elif p[1].gettokentype() == 'DIV':
            return Div(left, right)
        else:
            raise AssertionError('Oops, this should not be possible!')

parser = pg.build()
