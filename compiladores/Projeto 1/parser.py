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

@pg.production('variable_declaration_part : variable_declaration SEMI_COLON, variable_declaration SEMI_COLON')

@pg.production('variable_declaration : identifier, COMMA identifier, COLON type')

@pg.production('type : single_type')
@pg.production('type : array_type')

@pg.production('array_type : ARRAY OPEN_BRACKET index_range CLOSE_BRACKET OF simple_type')

@pg.production('index_range : integer_const INDEX_RANGE integer_const')

@pg.production('simple_type : char')
@pg.production('simple_type : integer')
@pg.production('simple_type : boolean')

@pg.production('type_identifier : identifier')

@pg.production('subroutine_declaration_part : procedure_declaration')
@pg.production('subroutine_declaration_part : function_declaration')

@pg.production('procedure_declaration : PROCEDURE identifier formal_parameters SEMICOLON block')

@pg.production('function_declaration : FUNCTION identifier formal_parameters COLON type SEMICOLON block')

@pg.production('formal_parameters : OPEN_PARENS param_section CLOSE_PARENS')
def expression_parens(p):
    return p[1]

@pg.production('param_section : variable_declaration, SEMICOLON variable_declaration_list SEMICOLON')

@pg.production('statement_part : compound_statement')

@pg.production('compound_statement : BEGIN statement, SEMICOLON statement, END')

@pg.production('statement : simple_statement')
@pg.production('statement : structured_statement')

@pg.production('simple_statement : assignment_statement')
@pg.production('simple_statement : function_procedure_statement')
@pg.production('simple_statement : read_statement')
@pg.production('simple_statement : write_statement')

@pg.production('assignment_statement : variable EQUALS expression')

@pg.production('function_procedure_statement : function_procedure_identifier')

@pg.production('function_procedure_statement : variable EQUALS function_procedure_identifier')

@pg.production('function_procedure_identifier : identifier')

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

@pg.production('variable : entire_variable')
@pg.production('variable : indexed_variable')

@pg.production('indexed_variable : array_variable OPEN_BRACKET expression CLOSE_BRACKET')

@pg.production('array_variable : entire_variable')

@pg.production('entire_variable : variable_identifier')

@pg.production('variable_identifier : identifier')

@pg.production('constant : integer_const')

@pg.production('constant : character_const')

@pg.production('constant : constant_identifier')

@pg.production('constant_identifier : identifier')

@pg.production('identifier : letter, letter_or_digit')

@pg.production('letter_or_digit : letter')
@pg.production('letter_or_digit : digit')

@pg.production('integer_const : digit, digits')

@pg.production('character_const : SINGLE_QUOTE letter_or_digit SINGLE_QUOTE')
@pg.production('character_const : DOUBLE_QUOTE letter_or_digit, letter_or_digit_list DOUBLE_QUOTE')

@pg.production('letter : letter')
@pg.production('digit: digit')


parser = pg.build()