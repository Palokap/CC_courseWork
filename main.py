"""
pascal to LLVM IR Compiler

Автор: Макаров Никита
Группа: ИУ7-21М
"""

from antlr4 import *
from grammar.miniPascalLexer import miniPascalLexer
from grammar.miniPascalParser import miniPascalParser
from grammar.miniPascalVisitor import miniPascalVisitor
from llvmlite import ir
import sys


class miniPascalCompiler(miniPascalVisitor):
    def __init__(self):
        self.main_func = None
        self.module = ir.Module(name='miniPascalModule')
        self.module.triple = "x86_64-pc-windows-msvc19.41.34123"
        self.builder = None
        self.context = ir.Context()
        self.func = None
        self.stack = list()
        self.condition_ctx_stack = list()
        self.variables = {}
        self.subprs = {}
        self.cmp_result = None

        # Объявление функции printf в LLVM IR
        printf_type = ir.FunctionType(ir.IntType(32), [ir.PointerType(ir.IntType(8))], var_arg=True)
        self.printf_func = ir.Function(self.module, printf_type, name="printf")

        self.format_string = ir.GlobalVariable(self.module, ir.ArrayType(ir.IntType(8), len("%d\n")),
                                               name="format_string")
        self.format_string.linkage = 'internal'
        self.format_string.global_constant = True
        self.format_string.initializer = ir.Constant(ir.ArrayType(ir.IntType(8), len("%d\n")),
                                                     bytearray("%d\n", 'utf8'))

    def visitScript(self, ctx):
        self.visitProgram(ctx.sequence())
        return self.module

    def visitProgram(self, ctx: miniPascalParser.ProgramContext):
        # Создаем функцию main
        main_type = ir.FunctionType(ir.IntType(32), [])
        self.main_func = ir.Function(self.module, main_type, name="main")
        self.entry_block = self.main_func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(self.entry_block)

        # Обходим выражения внутри program
        if ctx.identifier_list():
            self.visitIdentifierList(ctx.identifier_list())
        if ctx.declarations():
            vars = self.visitDeclarations(ctx.declarations())
            for var in vars:
                self.variables[var.name] = var

        if ctx.subprogram_declarations():
            self.visitSubprogramDeclarations(ctx.subprogram_declarations())
        if ctx.compound_statement():
            self.visitCompound_statement(ctx.compound_statement())

        # Завершаем функцию main
        self.builder.ret(ir.Constant(ir.IntType(32), 0))

        return self.module

    def visitIdentifierList(self, ctx: miniPascalParser.Identifier_listContext):
        for child_ctx in ctx.ident():
            var_name = child_ctx.getText()
            var_type = ir.IntType(32)
            var = self.builder.alloca(var_type, name=var_name)
            self.variables[var_name] = var
            print(self.variables)

    def visitDeclarations(self, ctx: miniPascalParser.DeclarationsContext):
        declared_vars = []
        for child_ctx in ctx.declaration():
            print(child_ctx.getText(),'  varvar   ')
            vars = self.visitDeclaration(child_ctx)
            declared_vars.extend(vars)
            #self.variables[var.name] = var
            #print(self.variables)
        return declared_vars

    def visitSubprogramDeclarations(self, ctx: miniPascalParser.Subprogram_declarationsContext):
        for subDec_ctx in ctx.subprogram_declaration():

            subpr = self.visitSubprogramDeclaration(subDec_ctx)
            self.subprs[subpr.name] = subpr




    def visitSubprogramDeclaration(self, ctx):
        subpr = {}
        if ctx.subprogram_head().PROCEDURE():
            func_type = ir.IntType(32)
        elif ctx.subprogram_head().FUNCTION():
            if ctx.subprogram_head().standart_type().INTEGER():
                func_type = ir.IntType(32)
            elif ctx.subprogram_head().standart_type().REAL():
                func_type = ir.DoubleType()
            else:
                raise NameError(f"Unknown type")
        else:
            raise NameError(f"Unknown subprogram type")
        args = self.visitArguments(ctx.subprogram_head().arguments())
        subpr_type = ir.FunctionType(func_type, args)
        subpr_name = ctx.subprogram_head().ident()
        subpr["name"] = subpr_name
        subpr["subpr"] = ir.Function(self.module, subpr_type, name=subpr_name)
        subpr["entry"] = subpr["subpr"].append_basic_block(name="entry"+subpr_name)
        subpr["builder"] = ir.IRBuilder(subpr["entry"])
        #compound_statement
        return subpr

    def visitDeclaration(self, ctx):
        vars = []
        type_ctx = ctx.type_()

        if type_ctx.ARRAY():
            # array надо сделать

            pass
        else:
            if type_ctx.standard_type().INTEGER():
                var_type = ir.IntType(32)
            elif type_ctx.standard_type().REAL():
                var_type = ir.DoubleType()
            else:
                raise NameError(f"Unknown type")
        for ident_ctx in ctx.identifier_list().ident():
            print(ident_ctx.getText(),'  var in list')
        for ident_ctx in ctx.identifier_list().ident():
            var_name = ident_ctx.getText()
            var = self.builder.alloca(var_type, name=var_name)
            vars.append(var)
            #self.variables[var.name] = var
            #print(self.variables)
            #return var
        
        return vars

    def visitArguments(self, ctx: miniPascalParser.ArgumentsContext):
        varlist = []
        for param_ctx in ctx.parameter_list():
            var = self.visitDeclaration(param_ctx)
            varlist.append(var)
        return varlist

    def visitCompound_statement(self, ctx: miniPascalParser.Compound_statementContext):
        print(ctx.BEGIN(),ctx.optional_statements(),'я люблю ппапп   ', ctx.END())
        self.visitOptional_statements(ctx.optional_statements())

    def visitOptional_statements(self, ctx: miniPascalParser.Optional_statementsContext):
        self.visitStatement_list(ctx.statement_list())

    def visitStatement_list(self, ctx: miniPascalParser.Statement_listContext):
        #print(ctx.SC(),'adadadad')
        for state_ctx in ctx.statement():
            self.visitStatement(state_ctx)

    def visitStatement(self, ctx: miniPascalParser.StatementContext):
        if ctx.ASSIGN():
            self.visitAssignStatement(ctx)
        elif ctx.procedure_statement():
            self.visitProcedureStatement(ctx) #передать ctx.procedure_statement
        elif ctx.compound_statement():
            self.visitCompound_statement(ctx.compound_statement())
        elif ctx.IF():
            self.visitIfStatement(ctx)
        elif ctx.WHILE():
            self.visitWhileStatement(ctx)

    def visitAssignStatement(self, ctx: miniPascalParser.StatementContext):
        variable = self.visitVariable(ctx.variable())
        value = self.visitExpression(ctx.expression())

        #print("BC", str(variable), value.type, type(value.type))
        if str(variable).find("i32")>0 and isinstance(value.type, ir.DoubleType):
            value = self.builder.fptosi(value, ir.IntType(32))

        if str(variable).find("double")>0 and isinstance(value.type, ir.IntType):
            value = self.builder.sitofp(value, ir.DoubleType())

        self.builder.store(value, variable)

    def visitVariable(self, ctx: miniPascalParser.VariableContext):
        #todo array
        var_name = ctx.getText()
        var = self.variables[var_name]
        print("vV", var_name, var, self.variables)
        return var

 #запись bytecode в ЛЛВМ

    def visitExpression(self, ctx: miniPascalParser.ExpressionContext):
        #print(ctx.getText(), 'expression')
        if ctx.REL():
            pass  #todo скорее всего сделать как в муле
        else:
            return self.visitSimple_expression(ctx.simple_expression(0)) 
            #for simple_exp_ctx in ctx.simple_expression():
            #    self.visitSimple_expression(simple_exp_ctx)

    def visitSimple_expression(self, ctx: miniPascalParser.Simple_expressionContext):
        print(ctx.getText(), ' find in expression')
        result = self.visitTerm(ctx.term(0))
        if ctx.sign():
            self.visitSign(ctx.sign())
        i = 1
        while ctx.term(i):
            #print(ctx.add(i-1).getText(), ' ad operation')
            if ctx.add(i-1).getText() == '+':
                result = self.builder.add(result, self.visitTerm(ctx.term(i)))
            elif ctx.add(i-1).getText() == '-':
                result = self.builder.sub(result, self.visitTerm(ctx.term(i)))
            elif ctx.add(i-1).getText() == 'OR':
                result = self.builder.or_(result, self.visitTerm(ctx.term(i)))
            else:
                raise NameError(f"Unknown operation")
            i = i + 1
        return result

    def visitTerm(self, ctx: miniPascalParser.TermContext):
        result = self.visitFactor(ctx.factor(0))
        isDouble = isinstance(result.type, ir.FloatType)

        i = 1
        while ctx.factor(i):
            mulka = self.visitFactor(ctx.factor(i))

            # Переключатель с инта на флоат еще проверять
            print("vT_M", result, mulka)
            if isDouble and isinstance(mulka.type, ir.IntType):
                mulka = self.builder.sitofp(mulka, ir.DoubleType())
            elif not isDouble and isinstance(mulka.type, ir.DoubleType):
                result = self.builder.sitofp(result, ir.DoubleType())
                isDouble = True

            if isDouble: 
                result = self.builder.fmul(result, mulka)
            else:
                result = self.builder.mul(result, mulka)

            i = i+1

        return result

    def visitFactor(self, ctx: miniPascalParser.FactorContext):
        factor = None
        if ctx.ident():
            print("vF_I", ctx.ident(), ctx.ident().getText())
            self.visitIdent(ctx.ident())   #iidentdent zapis
            if ctx.expression_list():       # Если при id есть expression_list, значит это вызов функции, надо просчитать значения для аргументов и сделать вызов
                self.visitExpression_list(ctx.expression_list())
                #call функции
            else:
                var = self.variables[ctx.ident().getText()] # просто достаём переменную
                factor = self.builder.load(var)
        elif ctx.expression(): # вариант когда есть какие-то вычисления в скобках
            factor = self.visitExpression(ctx.expression())
        elif ctx.NOT():
            self.visitFactor(ctx.factor())  #v skobki i otricanie
        elif ctx.NUM():
            num_str = ctx.NUM().getText()
            if num_str.find(".")>0:
                factor = ir.Constant(ir.DoubleType(), float(num_str) )
            else:
                factor = ir.Constant(ir.IntType(32), int(num_str) )
        else:
            raise NameError(f"Compilication error")
        
        return factor

#    def visitSign(self, ctx: miniPascalParser.SignContext):
        #нужен он вообще?







if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = 'tests/test.pas'

    compiler = miniPascalCompiler()
    input_stream = FileStream(input_file)
    lexer = miniPascalLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = miniPascalParser(tokens)
    tree = parser.program()
    result_module = compiler.visitProgram(tree)

    # Вывод LLVM IR кода
    print(result_module)
    with open("out.ll", "w") as f:
        f.write(str(result_module))
