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
    def __init__(self, variable_declaration_part, procedure_declaration_part, statement_part):
        self.variable_declaration_part = variable_declaration_part
        self.procedure_declaration_part = procedure_declaration_part
        self.statement_part = statement_part

    def print(self):
        self.variable_declaration_part.print()
        self.procedure_declaration_part.print()
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
    def __init__(self, identifier, dtype):
        self.identifier = identifier
        self.dtype = dtype

    def print(self):
        self.identifier.print()
        self.dtype.print()


class Type(BaseBox):
    def __init__(self, simple_or_array_dtype):
        self.simple_or_array_dtype = simple_or_array_dtype

    def print(self):
        self.simple_or_array_dtype.print()


class Array_type(BaseBox):
    def __init__(self, idx_range, simple_type):
        self.idx_range = idx_range
        self.simple_type = simple_type

    def print(self):
        self.idx_range.print()
        self.simple_type.print()


class Index_range(BaseBox):
    def __init__(self, beginning, ending):
        self.beginning = beginning
        self.ending = ending

    def print(self):
        self.beginning.print()
        self.ending.print()


class Simple_type(BaseBox):
    def __init__(self, simple_type):
        self.simple_type = simple_type

    def print(self):
        self.simple_type.print()


class Type_identifier(BaseBox):
    def __init__(self, identifier):
        self.identifier = identifier

    def print(self):
        self.identifier.print()


class Subroutine_decl_part(BaseBox):
    def __init__(self, declaration):
        self.declaration = declaration

    def print(self):
        self.declaration.print()


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
        self.param_section.print()


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
        self.compound_statement.print()


class Compound_statement(BaseBox):
    def __init__(self, statement, statements):
        self.statement = statement
        self.statements = statements

    def print(self):
        self.statement.print()
        for statement in self.statements:
            statement.print()


class Statement(BaseBox):
    def __init__(self, simple_or_structured_statement):
        self.simple_or_structured_statement = simple_or_structured_statement

    def print(self):
        self.simple_or_structured_statement.print()


class Simple_statement(BaseBox):
    def __init__(self, type_of_stat):
        self.type_of_stat = variable

    def print(self):
        self.type_of_stat.print()


class Assignment_statement(BaseBox):
    def __init__(self, variable, expression):
        self.variable = variable
        self.expression = expression

    def print(self):
        self.variable.print()
        self.expression.print()


class Function_procedure_statement(BaseBox):
    def __init__(self, function_procedure_identifier):
        self.function_procedure_identifier = function_procedure_identifier

    def print(self):
        self.function_procedure_identifier.print()


class Function_procedure_statement_var(BaseBox):
    def __init__(self, variable, function_procedure_identifier):
        self.variable = variable
        self.function_procedure_identifier = function_procedure_identifier

    def print(self):
        self.variable.print()
        self.function_procedure_identifier.print()


class Function_procedure_identifier(BaseBox):
    def __init__(self, identifier):
        self.identifier = identifier

    def print(self):
        self.identifier.print()


class Read_statement(BaseBox):
    def __init__(self, variable, arglist):
        self.variable = variable
        self.arglist = arglist

    def print(self):
        self.variable.print()
        for arg in arglist:
            arg.print()



class Write_statement(BaseBox):
    def __init__(self, variable, arglist):
        self.variable = variable
        self.arglist = arglist

    def eval(self):
        return self.variable.eval()

    def print(self):
        self.variable.print()
        for arg in self.arglist:
            arg.print()


class Structured_statement(BaseBox):
    def __init__(self, stat_type):
        self.stat_type = stat_type

    def print(self):
        self.stat_type.print()


class If_statement(BaseBox):
    def __init__(self, expression, statement):
        self.expression = expression
        self.statement = statement

    def print(self):
        self.expression.print()
        self.statement.print()


class If_else_statement(BaseBox):
    def __init__(self, expression, pos_stat, neg_stat):
        self.expression = expression
        self.pos_stat = pos_stat
        self.neg_stat = neg_stat

    def print(self):
        self.expression.print()
        self.pos_stat.print()
        self.neg_stat.print()


class While_statement(BaseBox):
    def __init__(self, expression, statement):
        self.expression = expression
        self.statement = statement

    def print(self):
        self.expression.print()
        self.statement.print()


class Expression_simple(BaseBox):
    def __init__(self, simple_exp):
        self.simple_exp = simple_exp
    
    def print(self):
        self.simple_exp.print()


class Expression_comp(BaseBox):
    def __init__(self, simple_exp, relat_op, last_simple_exp):
        self.simple_exp = simple_exp
        self.relat_op = relat_op
        self.last_simple_exp = last_simple_exp

    def print(self):
        self.simple_exp.print()
        self.relat_op.print()
        self.last_simple_exp.print()


class Simple_expression(BaseBox):
    def __init__(self, sign, term):
        self.sign = sign
        self.term = term

    def print(self):
        self.sign.print()
        self.term.print()


class Term(BaseBox):
    def __init__(self, factor):
        self.factor = factor

    def print(self):
        self.factor.print()
        

class Factor(BaseBox):
    def __init__(self, var_const_exp_or_factor):
        self.var_const_exp_or_factor = var_const_exp_or_factor

    def print(self):
        self.var_const_exp_or_factor.print()


class Relational_operator(BaseBox):
    def __init__(self, operator):
        self.operator = factor

    def print(self):
        self.operator.print()


class Sign(BaseBox):
    def __init__(self, sign):
        self.sign = sign

    def print(self):
        self.sign.print()


class Adding_operator(BaseBox):
    def __init__(self, sign):
        self.sign = sign

    def print(self):
        self.sign.print()


class Mult_operator(BaseBox):
    def __init__(self, operator):
        self.operator = operator

    def print(self):
        self.operator.print()


class Variable(BaseBox):
    def __init__(self, var):
        self.var = var

    def print(self):
        self.var.print()


class Indexed_variable(BaseBox):
    def __init__(self, array_var, expr):
        self.array_var = array_var
        self.expr = expr

    def print(self):
        self.array_var.print()
        self.expr.print()


class Array_variable(BaseBox):
    def __init__(self, entire_var):
        self.entire_var = entire_var

    def print(self):
        self.entire_var.print()


class Entire_variable(BaseBox):
    def __init__(self, var_id):
        self.var_id = var_id

    def print(self):
        self.var_id.print()


class Variable_identifier(BaseBox):
    def __init__(self, identifier):
        self.identifier = identifier

    def print(self):
        self.identifier.print()


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


class Lesser_than(BinaryOp):
    def eval(self):
        return self.left.eval() < self.right.eval()


class Lesser_or_equals(BinaryOp):
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