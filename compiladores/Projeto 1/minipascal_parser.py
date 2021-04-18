from minipascal_ast import Compound_statement, Variable_decl_part, Variable_declaration
from rply import ParserGenerator
import warnings
from ast import *
from lexer import *

warnings.filterwarnings("ignore")


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


@pg.production('program : PROGRAM IDENTIFIER SEMICOLON block DOT')
def program(p):
    return Program(p[1], p[3])


@pg.production('block : variable_declaration_part subroutine_declaration_part statement_part')
def block(p):
    return Block(p[0], p[1], p[2])


@pg.production('variable_declaration_part : VAR variable_declaration SEMICOLON variable_declaration_list')
@pg.production('variable_declaration_list : variable_declaration SEMICOLON')
@pg.production('variable_declaration_list : variable_declaration variable_declaration_list')
@pg.production('variable_declaration_list : ')
@pg.production('variable_declaration_part : ')
def variable_declaration_part(p):
    if len(p) == 0:
      return None
    elif len(p) < 3:
        return Variable_decl_part(p[1], None)
    return Variable_decl_part(p[1], p[3])


@pg.production('variable_declaration : IDENTIFIER COLON type')
@pg.production('variable_declaration : IDENTIFIER COMMA variable_declaration')
def variable_declaration(p):
    return Variable_declaration(p[0], p[2])

@pg.production('dtype : simple_type')
@pg.production('dtype : array_type')
def dtype(p):
    return Type(p[0])


@pg.production('array_type : ARRAY OPEN_BRACKET index_range CLOSE_BRACKET OF simple_type')
def array_type(p):
    return Array_type(p[2], p[5])


@pg.production('index_range : INT_CONST INDEX_RANGE INT_CONST')
def index_range(p):
    return Index_range(p[0], p[2])


@pg.production('simple_type : CHARACTER')
@pg.production('simple_type : INTEGER')
@pg.production('simple_type : BOOLEAN')
def simple_type(p):
    return Simple_type(p[0])


@pg.production('type_identifier : IDENTIFIER')
def type_identifier(p):
    return Type_identifier(p[0])


@pg.production('subroutine_declaration_part : procedure_declaration')
@pg.production('subroutine_declaration_part : function_declaration')
def subroutine_declaration_part(p):
    return Subroutine_decl_part(p[0])


@pg.production('procedure_declaration : PROCEDURE IDENTIFIER formal_parameters SEMICOLON block')
@pg.production('procedure_declaration : ')
def procedure_declaration(p):
    if len(p) == 0:
      return None
    return Procedure_decl(p[1], p[2], p[4])


@pg.production('function_declaration : FUNCTION IDENTIFIER formal_parameters COLON type SEMICOLON block')
def function_declaration(p):
    return Function_decl(p[1], p[2], p[4], p[6])


@pg.production('formal_parameters : OPEN_PARENS param_section CLOSE_PARENS')
def formal_parameters(p):
    return Formal_parameters(p[1])


@pg.production('param_section : variable_declaration')
@pg.production('param_section : SEMICOLON param_section SEMICOLON param_section')
def param_section(p):
    return Param_section(p[0])


@pg.production('statement_part : compound_statement')
def statement_part(p):
    return Statement_part(p[0])

#compound_statement ::= begin statement {;statement} end
@pg.production('compound_statement : BEGIN statement statement_list END')
@pg.production('statement_list : ')
@pg.production('statement_list : SEMICOLON statement statement_list')
def compound_statement(p):
    if len(p) == 0:
      return None
    if len(p) > 2:
        return Compound_statement(p[1], p[2])
    return Compound_statement(p[1], None)


@pg.production('statement : simple_statement')
@pg.production('statement : structured_statement')
def statement(p):
    return Statement(p[0])


@pg.production('simple_statement : assignment_statement')
@pg.production('simple_statement : function_procedure_statement')
@pg.production('simple_statement : read_statement')
@pg.production('simple_statement : write_statement')
def simple_statement(p):
    return Simple_statement(p[0])


@pg.production('assignment_statement : variable ATTRIBUTION expression')
def assignment_statement(p):
    return Assignment_statement(p[0], p[2])


@pg.production('function_procedure_statement : function_procedure_identifier')
def function_procedure_statement(p):
    return Function_procedure_statement(p[0])


@pg.production('function_procedure_statement_var : variable ATTRIBUTION function_procedure_identifier')
def function_procedure_statement_var(p):
    return Function_procedure_statement_var(p[0], p[2])


@pg.production('function_procedure_identifier : IDENTIFIER')
def function_procedure_identifier(p):
    return Function_procedure_identifier(p[0])


@pg.production('var_list : ')
@pg.production('var_list : COMMA variable var_list')

@pg.production('read_statement : READ OPEN_PARENS variable var_list CLOSE_PARENS')
def read_statement(p):
  if len(p) == 0:
      return None
  return Read_statement(p[2], p[3])


@pg.production('write_statement : WRITE OPEN_PARENS variable var_list CLOSE_PARENS')
def write_statement(p):
  if len(p) == 0:
      return None
  return Write_statement(p[2], p[3])



@pg.production('structured_statement : compound_statement')
@pg.production('structured_statement : if_statement')
@pg.production('structured_statement : if_else_statement')
@pg.production('structured_statement : while_statement')
def structured_statement(p):
    return Structured_statement(p[0])


@pg.production('if_statement : IF expression THEN statement')
def if_statement(p):
    return If_statement(p[1], p[3])


@pg.production('if_else_statement : IF expression THEN statement ELSE statement')
def if_else_statement(p):
    return If_else_statement(p[1], p[3], p[5])


@pg.production('while_statement : WHILE expression DO statement')
def while_statement(p):
    return While_statement(p[1], p[3])


@pg.production('expression : expression EQUALS expression')
@pg.production('expression : expression NOT_EQUAL expression')
@pg.production('expression : expression LESSER_THAN expression')
@pg.production('expression : expression LESSER_OR_EQUALS expression')
@pg.production('expression : expression GREATER_THAN expression')
@pg.production('expression : expression GREATER_OR_EQUALS expression')
@pg.production('expression : expression OR expression')
@pg.production('expression : expression AND expression')
def expression_logical_binop(p):
    left = p[0]
    right = p[2]
    check = p[1]

    if check.gettokentype() == 'EQUALS':
        return Equals(left, right)
    elif check.gettokentype() == 'NOT_EQUAL':
        return Not_equal(left, right)
    elif check.gettokentype() == 'GREATER_OR_EQUALS':
        return Greater_or_equals(left, right)
    elif check.gettokentype() == 'LESSER_OR_EQUALS':
        return Lesser_or_equals(left, right)
    elif check.gettokentype() == 'GREATER_THAN':
        return Greater_than(left, right)
    elif check.gettokentype() == 'LESSER_THAN':
        return Lesser_than(left, right)
    elif check.gettokentype() == 'AND':
        return And(left, right)
    elif check.gettokentype() == 'OR':
        return Or(left, right)
    else:
        raise AssertionError("Oops, this shouldn't be possible")


@pg.production('expression : sign term')
def expression_simple(p):
    return Simple_expression(p[0], p[1])


@pg.production('sign : PLUS')
@pg.production('sign : MINUS')
@pg.production('sign : ')
def sign(p):
    if len(p) == 0:
      return None
    return Sign(p[0])


@pg.production('term : factor')
def term(p):
    return Term(p[0])


@pg.production('factor : VAR')
@pg.production('factor : INT_CONST')
@pg.production('factor : CHAR_CONST')
@pg.production('factor : IDENTIFIER')
@pg.production('factor : OPEN_PARENS expression CLOSE_PARENS')
@pg.production('factor : NOT factor')
def factor(p):
    if p[0].gettokentype() == 'OPEN_PARENS' or p[0].gettokentype() == 'NOT':
        return Factor(p[1])
    else:
        return Factor(p[0])


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


@pg.production('variable : entire_variable')
@pg.production('variable : indexed_variable')
def variable(p):
    return Variable(p[0])


@pg.production('indexed_variable : array_variable OPEN_BRACKET expression CLOSE_BRACKET')
def indexed_variable(p):
    return Indexed_variable(p[0], p[2])


@pg.production('array_variable : entire_variable')
def array_variable(p):
    return Array_variable(p[0])


@pg.production('entire_variable : variable_identifier')
def entire_variable(p):
    return Entire_variable(p[0])


@pg.production('variable_identifier : IDENTIFIER')
def variable_identifier(p):
    return Variable_identifier(p[0])

@pg.error
def error_handler(token):
    raise ValueError("Ran into a %s where it wasn't expected" % token.gettokentype())

parser = pg.build()