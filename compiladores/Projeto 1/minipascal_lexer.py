from rply import LexerGenerator

lg = LexerGenerator()

# program ::= 'program' identifier;block
# variable_declaration_part ::= 'var' empty | variable_declaration; \{variable_declaration;\}
# array_type ::= 'array' '\['index_range'\]' 'of' simple_type

lg.add('PROGRAM', r'program')
lg.add('VAR', r'var')
lg.add('COMMA', r'\,')
lg.add('ARRAY', r'array')
lg.add('OPEN_BRACKET', r'\[')
lg.add('CLOSE_BRACKET', r'\]')
lg.add('OF', r'of')

# index_range ::= integer_const..integer_const
lg.add('INDEX_RANGE', r'\.\.')

# simple_type ::= char | integer | boolean
lg.add('INTEGER', r'integer')
lg.add('CHARACTER', r'char')
lg.add('BOOLEAN', r'boolean')

# procedure_declaration ::= 'procedure' identifier formal_parameters ';' block
# function declaration ::= 'function' identifier formal_parameters ':'
# type ';' block
lg.add('PROCEDURE', r'procedure')
lg.add('FUNCTION', r'function')

# formal_parameters ::= '('param_section')'
# param_section ::= variable_declaration {';' variable_declaration ';'}
lg.add('OPEN_PARENS', r'\(')
lg.add('CLOSE_PARENS', r'\)')
lg.add('SEMICOLON', r'\;')

# compound_statement ::= 'begin' statement {';'statement} 'end'
lg.add('BEGIN', r'begin')
lg.add('END', r'end')

# read_statement ::= 'read' '('variable {',' variable} ')'
# write_statement ::= 'write' '(' variable {',' variable} ')'
lg.add('READ', r'read')
lg.add('WRITE', r'write')

# if_statement ::= 'if' expression 'then' statement | 'if' expression
# 'then' statement 'else' statement
lg.add('IF', r'if')
lg.add('THEN', r'then')
lg.add('ELSE', r'else')

# while_statement ::= 'while' expression 'do' statement
lg.add('WHILE', r'while')
lg.add('DO', r'do')

# factor ::= variable | constant | '('expression')' | 'not' factor
lg.add('NOT', r'not')

# relational_operator ::= '=' | '<>' | '<' | '<=' | '>=' | '>' | 'or' | 'and'
lg.add('EQUALS', r'=')
lg.add('NOT_EQUAL', r'<>')
lg.add('LESSER_THAN', r'\<')
lg.add('LESSER_OR_EQUALS', r'\<\=')
lg.add('GREATER_THAN', r'\>')
lg.add('GREATER_OR_EQUALS', r'\>\=')
lg.add('OR', r'or')
lg.add('AND', r'and')

lg.add('ATTRIBUTION', r':=')
lg.add('DOT', r'\.')
lg.add('COLON', r'\:')

# integer_const ::= digit { digit }
# sign ::= '+' | '-' | empty
lg.add('INT_CONST', r'[+-]?\d+')

# adding_operator ::= '+' | '-'
lg.add('PLUS', r'\+')
lg.add('MINUS', r'-')

# multiplying_operator ::= '*' | 'div'
lg.add('MUL', r'\*')
lg.add('DIV', r'/')

# character_const ::= `'`letter_or_digit`'` | `"`letter_or_digit
# {letter_or_digit}`"`
lg.add('CHAR_CONST', r'(\'[a-zA-Z0-9]\')|(\"[a-zA-Z0-9][a-zA-Z0-9]*\")')

# identifier ::= letter { letter_or_digit }
lg.add('IDENTIFIER', r'[a-zA-z][a-zA-Z0-9]*')

lg.ignore(r'\s+')
lexer = lg.build()
for token in lexer.lex(
        'var numero2, numeroB, soma : integer;begin write(A); read(a); write(Banana); read("numeroB"); soma := (numeroA + numeroB); write(Soma = , soma:5:-2 ); end'):
    print(token)