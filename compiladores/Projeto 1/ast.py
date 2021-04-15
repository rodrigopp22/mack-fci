from rply.token import BaseBox
from rply import ParserGenerator
import lexer


class BinaryOp(BaseBox):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Integer_const(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value


class Program(BaseBox):
    def __init__(self, identifier, block):
        self.identifier = identifier
        self.block = block

    def print(self):
        self.identifier.print()
        self.block.print()


class Block(BaseBox):
    def __init__(self, var_decl_part, subroutine_decl_part, statement_part):
        self.var_decl_part = var_decl_part
        self.subroutine_decl_part = subroutine_decl_part
        self.statement_part = statement_part

    def print(self):
        self.var_decl_part.print()
        self.subroutine_decl_part.print()
        self.statement_part.print()


class Variable_decl_part(BaseBox):
    def __init__(self, variable_declaration, variable_declaration_list):
        self.variable_declaration = variable_declaration
        self.variable_declaration_list = variable_declaration_list

    def print(self):
        self.variable_declaration.print()
        for var in self.variable_declaration_list:
            var.print()


class Variable_declaration(BaseBox):
    def __init__(self, identifier, identifier_list, dtype):
        self.identifier = identifier
        self.identifier_list = identifier_list
        self.dtype = dtype

    def print(self):
        self.identifier.print()
        self.dtype.print()
        for id_list in self.identifier_list:
            id_list.print()


class Index_range(BaseBox):
    def __init__(self, beginning, ending):
        self.beginning = beginning
        self.ending = ending

    def print(self):
        self.beginning.print()
        self.ending.print()


class Procedure_decl(BaseBox):
    def __init__(self, identifier, formal_parameters, block):
        self.identifier = identifier
        self.formal_parameters = formal_parameters
        self.block = block

    def print(self):
        self.identifier.print()
        self.formal_parameters.print()
        self.block.print()


class Function_decl(BaseBox):
    def __init__(self, identifier, formal_parameters, dtype, block):
        self.identifier = identifier
        self.formal_parameters = formal_parameters
        self.dtype = dtype
        self.block = block

    def print(self):
        self.identifier.print()
        self.formal_parameters.print()
        self.dtype.print()
        self.block.print()


class Formal_parameters(BaseBox):
    def __init__(self, param_section):
        self.param_section = param_section

    def print(self):
        for param in self.param_section:
            param.print()


class Param_section(BaseBox):
    def __init__(self, variable_decl, variable_decl_list):
        self.variable_decl = variable_decl
        self.variable_decl_list = variable_decl_list

    def print(self):
        self.variable_decl.print()
        for var in self.variable_decl_list:
            var.print()


class Statement_part(BaseBox):
    def __init__(self, compound_statement):
        self.compound_statement = compound_statement

    def print(self):
        for statement in self.compound_statement:
            statement.print()


class Compound_statement(BaseBox):
    def __init__(self, statement, statement_list):
        self.statement = statementpython
        self.statement_list = statement_list

    def print(self):
        for stat_list in self.statement_list:
            stat_list.print()


class Assignment_statement(BaseBox):
    def __init__(self, variable, expression):
        self.variable = variable
        self.expression = expression

    def print(self):
        self.variable.print()
        self.expression.print()


class Function_procedure_statement(BaseBox):
    def __init__(self, function_procedure_identifier, variable):
        self.function_procedure_identifier = function_procedure_identifier
        self.variable = variable

    def print(self):
        self.function_procedure_identifier.print()
        self.variable.print()


class Function_procedure_identifier(BaseBox):
    def __init__(self, identifier):
        self.identifier = identifier

    def print(self):
        self.identifier.print()


class Read_statement(BaseBox):
    def __init__(self, variable, variable_list):
        self.variable = variable
        self.variable_list = variable_list

    def print(self):
        self.identifier.print()
        for var_list in variable_list:
            var_list.print()


class Write_statement(BaseBox):
    def __init__(self, variable, variable_list):
        self.variable = variable
        self.variable_list = variable_list

    def print(self):
        self.variable.print()
        for var_list in self.variable_list:
            var_list.print()


class If_statement(BaseBox):
    def __init__(self, expression, statement):
        self.expression = expression
        self.statement = statement

    def print(self):
        self.expression.print()
        self.statement.print()


class If_else_statement(BaseBox):
    def __init__(self, expression, statement, else_statement):
        self.expression = expression
        self.statement = statement
        self.else_statement = else_statement

    def print(self):
        self.expression.print()
        self.statement.print()
        self.else_statement.print()


class While_statement(BaseBox):
    def __init__(self, expression, statement):
        self.expression = expression
        self.statement = statement

    def print(self):
        self.expression.print()
        self.statement.print()


class Simple_expression(BaseBox):
    def __init__(self, sign, term, term_list):
        self.sign = sign
        self.term = term
        self.term_list = term_list

    def print(self):
        self.sign.print()
        self.term.print()
        for term in self.term_list:
            term.print()


class Add(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()


class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()


class Mul(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()


class Div(BinaryOp):
    def eval(self):
        return self.left.eval() / self.right.eval()


class Equals(BinaryOp):
    def eval(self):
        return self.left.eval() == self.right.eval()


class Not_equal(BinaryOp):
    def eval(self):
        return self.left.eval() != self.right.eval()


class Less_than(BinaryOp):
    def eval(self):
        return self.left.eval() < self.right.eval()


class Less_or_equals(BinaryOp):
    def eval(self):
        return self.left.eval() <= self.right.eval()


class Greater_than(BinaryOp):
    def eval(self):
        return self.left.eval() > self.right.eval()


class Greater_or_equals(BinaryOp):
    def eval(self):
        return self.left.eval() >= self.right.eval()


class Or(BinaryOp):
    def eval(self):
        return self.left.eval() or self.right.eval()


class And(BinaryOp):
    def eval(self):
        return self.left.eval() and self.right.eval()



