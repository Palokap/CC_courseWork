# Generated from miniPascal.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .miniPascalParser import miniPascalParser
else:
    from miniPascalParser import miniPascalParser

# This class defines a complete generic visitor for a parse tree produced by miniPascalParser.

class miniPascalVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by miniPascalParser#program.
    def visitProgram(self, ctx:miniPascalParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPascalParser#identifier_list.
    def visitIdentifier_list(self, ctx:miniPascalParser.Identifier_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPascalParser#declarations.
    def visitDeclarations(self, ctx:miniPascalParser.DeclarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPascalParser#declaration.
    def visitDeclaration(self, ctx:miniPascalParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPascalParser#type.
    def visitType(self, ctx:miniPascalParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPascalParser#standard_type.
    def visitStandard_type(self, ctx:miniPascalParser.Standard_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPascalParser#subprogram_declarations.
    def visitSubprogram_declarations(self, ctx:miniPascalParser.Subprogram_declarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPascalParser#subprogram_declaration.
    def visitSubprogram_declaration(self, ctx:miniPascalParser.Subprogram_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPascalParser#subprogram_head.
    def visitSubprogram_head(self, ctx:miniPascalParser.Subprogram_headContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPascalParser#arguments.
    def visitArguments(self, ctx:miniPascalParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPascalParser#parameter_list.
    def visitParameter_list(self, ctx:miniPascalParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPascalParser#compound_statement.
    def visitCompound_statement(self, ctx:miniPascalParser.Compound_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPascalParser#optional_statements.
    def visitOptional_statements(self, ctx:miniPascalParser.Optional_statementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPascalParser#statement_list.
    def visitStatement_list(self, ctx:miniPascalParser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPascalParser#statement.
    def visitStatement(self, ctx:miniPascalParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPascalParser#variable.
    def visitVariable(self, ctx:miniPascalParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPascalParser#procedure_statement.
    def visitProcedure_statement(self, ctx:miniPascalParser.Procedure_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPascalParser#expression_list.
    def visitExpression_list(self, ctx:miniPascalParser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPascalParser#expression.
    def visitExpression(self, ctx:miniPascalParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPascalParser#simple_expression.
    def visitSimple_expression(self, ctx:miniPascalParser.Simple_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPascalParser#term.
    def visitTerm(self, ctx:miniPascalParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPascalParser#factor.
    def visitFactor(self, ctx:miniPascalParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPascalParser#sign.
    def visitSign(self, ctx:miniPascalParser.SignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPascalParser#ident.
    def visitIdent(self, ctx:miniPascalParser.IdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPascalParser#add.
    def visitAdd(self, ctx:miniPascalParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniPascalParser#mul.
    def visitMul(self, ctx:miniPascalParser.MulContext):
        return self.visitChildren(ctx)



del miniPascalParser