from rply import ParserGenerator
from rply.token import BaseBox, TokenToken
from objects import *

pg = ParserGenerator(['PROGRAM',
                      'VAR',
                      'COMMA',
                      'ARRAY',
                      'OPEN_BRACKET',
                      'CLOSE_BRACKET',
                      'OF',
                      'INDEX_RANGE',
                      'INTEGER',
                      'CHARACTER',
                      'BOOLEAN',
                      'PROCEDURE',
                      'FUNCTION',
                      'OPEN_PARENS',
                      'CLOSE_PARENS',
                      'SEMICOLON',
                      'BEGIN',
                      'END',
                      'READ',
                      'WRITE',
                      'IF',
                      'THEN',
                      'ELSE',
                      'WHILE',
                      'DO',
                      'NOT',
                      'EQUALS',
                      'NOT_EQUAL',
                      'LESSER_THAN',
                      'LESSER_OR_EQUALS',
                      'GREATER_THAN',
                      'GREATER_OR_EQUALS',
                      'OR',
                      'AND',
                      'ATTRIBUTION',
                      'DOT',
                      'COLON',
                      'PLUS',
                      'MINUS',
                      'MUL',
                      'DIV',
                      'INT_CONST',
                      'CHAR_CONST',
                      'IDENTIFIER'],
                     precedence=[('left',
                                  ['ELSE',
                                   'THEN']), ('left',
                                              ['EQUALS',
                                               'NOT_EQUAL',
                                               'LESSER_THAN',
                                               'LESSER_OR_EQUALS',
                                               'GREATER_THAN',
                                               'GREATER_OR_EQUALS']), ('left',
                                                                       ['PLUS',
                                                                        'MINUS',
                                                                        'OR']),
                                 ('left',
                                  ['MUL',
                                   'DIV',
                                   'AND']),
                                 ('left', 'NOT')])

@pg.production('program : PROGRAM identifier SEMICOLON block')
def program(p):
    return Program(p[1], p[3])

@pg.production('block : variable_declaration_part subroutine_declaration_part statement_part')
def block(p):
    return Block(p[0], p[1], p[2])

@pg.production('variable_declaration_part : VAR empty ')

@pg.production('atrib : ID EQUALS expression')
def attrib(p):
    return Attrib(p[0].getstr(), p[2])


@pg.production('expression : NUMBER')
def expression_integer(p):
    # p is a list of the pieces matched by the right hand side of the
    # rule
    return Number(int(p[0].getstr()))



@pg.production('expression : OPEN_PARENS expression CLOSE_PARENS')
def expression_parens(p):
    return p[1]

@pg.production('read_statement : READ OPEN_PARENS variable ')

@pg.production('write_statement : WRITE OPEN_PARENS variable COMMA variable_list CLOSE_PARENS')

@pg.production('structured_statement : compound_statement')

@pg.production('structured_statement : if_statement')

@pg.production('structured_statement : while_statement')

@pg.production('if_statement : IF expression THEN statement')
def if_then(p):
    return If_statement(p[1], p[3])
@pg.production(' if_statement : IF expression THEN statement ELSE statement')
def if_else(p):
    return If_else_statement(p[1], p[3], p[5])
@pg.production('while_statement : WHILE expression DO statement')
def while_statement(p):
    return While_statement(p[1], p[3])


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


@pg.production('expression : expression != expression')
@pg.production('expression : expression == expression')
@pg.production('expression : expression >= expression')
@pg.production('expression : expression <= expression')
@pg.production('expression : expression > expression')
@pg.production('expression : expression < expression')
@pg.production('expression : expression AND expression')
@pg.production('expression : expression OR expression')

def expression_logical_binop(p):
    left = p[0]
    right = p[2]
    check = p[1]
    
    if check.gettokentype() == '==':
        return Equals(left, right)
    elif check.gettokentype() == '!=':
        return Not_equal(left, right)
    elif check.gettokentype() == '>=':
        return Greater_or_equals(left, right)
    elif check.gettokentype() == '<=':
        return Less_or_equals(left, right)
    elif check.gettokentype() == '>':
        return Greater_than(left, right)
    elif check.gettokentype() == '<':
        return Less_than(left, right)
    elif check.gettokentype() == 'AND':
        return And(left, right)
    elif check.gettokentype() == 'OR':
        return Or(left, right)
    else:
        raise AssertionError("Oops, this shouldn't be possible")

parser = pg.build()