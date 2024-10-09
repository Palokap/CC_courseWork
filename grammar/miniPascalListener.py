# Generated from miniPascal.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .miniPascalParser import miniPascalParser
else:
    from miniPascalParser import miniPascalParser

# This class defines a complete listener for a parse tree produced by miniPascalParser.
class miniPascalListener(ParseTreeListener):

    # Enter a parse tree produced by miniPascalParser#program.
    def enterProgram(self, ctx:miniPascalParser.ProgramContext):
        pass

    # Exit a parse tree produced by miniPascalParser#program.
    def exitProgram(self, ctx:miniPascalParser.ProgramContext):
        pass


    # Enter a parse tree produced by miniPascalParser#identifier_list.
    def enterIdentifier_list(self, ctx:miniPascalParser.Identifier_listContext):
        pass

    # Exit a parse tree produced by miniPascalParser#identifier_list.
    def exitIdentifier_list(self, ctx:miniPascalParser.Identifier_listContext):
        pass


    # Enter a parse tree produced by miniPascalParser#declarations.
    def enterDeclarations(self, ctx:miniPascalParser.DeclarationsContext):
        pass

    # Exit a parse tree produced by miniPascalParser#declarations.
    def exitDeclarations(self, ctx:miniPascalParser.DeclarationsContext):
        pass


    # Enter a parse tree produced by miniPascalParser#declaration.
    def enterDeclaration(self, ctx:miniPascalParser.DeclarationContext):
        pass

    # Exit a parse tree produced by miniPascalParser#declaration.
    def exitDeclaration(self, ctx:miniPascalParser.DeclarationContext):
        pass


    # Enter a parse tree produced by miniPascalParser#type.
    def enterType(self, ctx:miniPascalParser.TypeContext):
        pass

    # Exit a parse tree produced by miniPascalParser#type.
    def exitType(self, ctx:miniPascalParser.TypeContext):
        pass


    # Enter a parse tree produced by miniPascalParser#standard_type.
    def enterStandard_type(self, ctx:miniPascalParser.Standard_typeContext):
        pass

    # Exit a parse tree produced by miniPascalParser#standard_type.
    def exitStandard_type(self, ctx:miniPascalParser.Standard_typeContext):
        pass


    # Enter a parse tree produced by miniPascalParser#subprogram_declarations.
    def enterSubprogram_declarations(self, ctx:miniPascalParser.Subprogram_declarationsContext):
        pass

    # Exit a parse tree produced by miniPascalParser#subprogram_declarations.
    def exitSubprogram_declarations(self, ctx:miniPascalParser.Subprogram_declarationsContext):
        pass


    # Enter a parse tree produced by miniPascalParser#subprogram_declaration.
    def enterSubprogram_declaration(self, ctx:miniPascalParser.Subprogram_declarationContext):
        pass

    # Exit a parse tree produced by miniPascalParser#subprogram_declaration.
    def exitSubprogram_declaration(self, ctx:miniPascalParser.Subprogram_declarationContext):
        pass


    # Enter a parse tree produced by miniPascalParser#subprogram_head.
    def enterSubprogram_head(self, ctx:miniPascalParser.Subprogram_headContext):
        pass

    # Exit a parse tree produced by miniPascalParser#subprogram_head.
    def exitSubprogram_head(self, ctx:miniPascalParser.Subprogram_headContext):
        pass


    # Enter a parse tree produced by miniPascalParser#arguments.
    def enterArguments(self, ctx:miniPascalParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by miniPascalParser#arguments.
    def exitArguments(self, ctx:miniPascalParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by miniPascalParser#parameter_list.
    def enterParameter_list(self, ctx:miniPascalParser.Parameter_listContext):
        pass

    # Exit a parse tree produced by miniPascalParser#parameter_list.
    def exitParameter_list(self, ctx:miniPascalParser.Parameter_listContext):
        pass


    # Enter a parse tree produced by miniPascalParser#compound_statement.
    def enterCompound_statement(self, ctx:miniPascalParser.Compound_statementContext):
        pass

    # Exit a parse tree produced by miniPascalParser#compound_statement.
    def exitCompound_statement(self, ctx:miniPascalParser.Compound_statementContext):
        pass


    # Enter a parse tree produced by miniPascalParser#optional_statements.
    def enterOptional_statements(self, ctx:miniPascalParser.Optional_statementsContext):
        pass

    # Exit a parse tree produced by miniPascalParser#optional_statements.
    def exitOptional_statements(self, ctx:miniPascalParser.Optional_statementsContext):
        pass


    # Enter a parse tree produced by miniPascalParser#statement_list.
    def enterStatement_list(self, ctx:miniPascalParser.Statement_listContext):
        pass

    # Exit a parse tree produced by miniPascalParser#statement_list.
    def exitStatement_list(self, ctx:miniPascalParser.Statement_listContext):
        pass


    # Enter a parse tree produced by miniPascalParser#statement.
    def enterStatement(self, ctx:miniPascalParser.StatementContext):
        pass

    # Exit a parse tree produced by miniPascalParser#statement.
    def exitStatement(self, ctx:miniPascalParser.StatementContext):
        pass


    # Enter a parse tree produced by miniPascalParser#variable.
    def enterVariable(self, ctx:miniPascalParser.VariableContext):
        pass

    # Exit a parse tree produced by miniPascalParser#variable.
    def exitVariable(self, ctx:miniPascalParser.VariableContext):
        pass


    # Enter a parse tree produced by miniPascalParser#procedure_statement.
    def enterProcedure_statement(self, ctx:miniPascalParser.Procedure_statementContext):
        pass

    # Exit a parse tree produced by miniPascalParser#procedure_statement.
    def exitProcedure_statement(self, ctx:miniPascalParser.Procedure_statementContext):
        pass


    # Enter a parse tree produced by miniPascalParser#expression_list.
    def enterExpression_list(self, ctx:miniPascalParser.Expression_listContext):
        pass

    # Exit a parse tree produced by miniPascalParser#expression_list.
    def exitExpression_list(self, ctx:miniPascalParser.Expression_listContext):
        pass


    # Enter a parse tree produced by miniPascalParser#expression.
    def enterExpression(self, ctx:miniPascalParser.ExpressionContext):
        pass

    # Exit a parse tree produced by miniPascalParser#expression.
    def exitExpression(self, ctx:miniPascalParser.ExpressionContext):
        pass


    # Enter a parse tree produced by miniPascalParser#simple_expression.
    def enterSimple_expression(self, ctx:miniPascalParser.Simple_expressionContext):
        pass

    # Exit a parse tree produced by miniPascalParser#simple_expression.
    def exitSimple_expression(self, ctx:miniPascalParser.Simple_expressionContext):
        pass


    # Enter a parse tree produced by miniPascalParser#term.
    def enterTerm(self, ctx:miniPascalParser.TermContext):
        pass

    # Exit a parse tree produced by miniPascalParser#term.
    def exitTerm(self, ctx:miniPascalParser.TermContext):
        pass


    # Enter a parse tree produced by miniPascalParser#factor.
    def enterFactor(self, ctx:miniPascalParser.FactorContext):
        pass

    # Exit a parse tree produced by miniPascalParser#factor.
    def exitFactor(self, ctx:miniPascalParser.FactorContext):
        pass


    # Enter a parse tree produced by miniPascalParser#sign.
    def enterSign(self, ctx:miniPascalParser.SignContext):
        pass

    # Exit a parse tree produced by miniPascalParser#sign.
    def exitSign(self, ctx:miniPascalParser.SignContext):
        pass


    # Enter a parse tree produced by miniPascalParser#ident.
    def enterIdent(self, ctx:miniPascalParser.IdentContext):
        pass

    # Exit a parse tree produced by miniPascalParser#ident.
    def exitIdent(self, ctx:miniPascalParser.IdentContext):
        pass


    # Enter a parse tree produced by miniPascalParser#add.
    def enterAdd(self, ctx:miniPascalParser.AddContext):
        pass

    # Exit a parse tree produced by miniPascalParser#add.
    def exitAdd(self, ctx:miniPascalParser.AddContext):
        pass


    # Enter a parse tree produced by miniPascalParser#mul.
    def enterMul(self, ctx:miniPascalParser.MulContext):
        pass

    # Exit a parse tree produced by miniPascalParser#mul.
    def exitMul(self, ctx:miniPascalParser.MulContext):
        pass



del miniPascalParser