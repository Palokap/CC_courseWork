// $antlr-format alignTrailingComments true, columnLimit 150, minEmptyLines 1, maxEmptyLinesToKeep 1, reflowComments false, useTab false
// $antlr-format allowShortRulesOnASingleLine false, allowShortBlocksOnASingleLine true, alignSemicolons hanging, alignColons hanging

grammar miniPascal;

options {
    caseInsensitive = true;
}

program
    : PROGRAM ident LP identifier_list RP SC declarations subprogram_declarations compound_statement DOT
    ;

identifier_list
    : ident (BREAK ident)*
    ;

declarations
    : (declaration)*
    ;

declaration
    : VAR identifier_list COL type SC
    ;

type
    : standard_type
    | ARRAY LB NUM DOTDOT NUM RB OF standard_type
    ;

standard_type
    : INTEGER
    | REAL
    ;

subprogram_declarations
    : (subprogram_declaration SC)*
    ;

subprogram_declaration
    : subprogram_head declarations compound_statement
    ;

subprogram_head
    : FUNCTION ident arguments COL standard_type SC
    | PROCEDURE ident arguments SC
    ;

arguments
    : (LP parameter_list RP)*
    ;

parameter_list
    : (identifier_list COL type SC)* (identifier_list COL type)
    ;

compound_statement
    : BEGIN optional_statements END
    ;

optional_statements
    : statement_list
    ;

statement_list
    : statement (SC statement)*
    ;

statement
    : variable ASSIGN expression
    | procedure_statement
    | compound_statement
    | IF expression THEN statement ELSE statement
    | WHILE expression DO statement
    ;

variable
    : ident (LB expression RB)?
    ;

procedure_statement
    : ident (LP expression_list RP)?
    ;

expression_list
    : expression (BREAK expression)*
    ;

expression
    : simple_expression (REL simple_expression)?
    ;

simple_expression
    : (sign)? term (add term)*
    ;

term
    : (factor mul)* factor
    ;

factor
    : ident (LP expression_list RP)?
    | NUM
    | LP expression RP
    | NOT factor
    ;

sign
    : PLUS
    | MINUS
    ;



ident
    : ID
    ;
PROGRAM
    : 'PROGRAM'
    ;
FUNCTION
    : 'FUNCTION'
    ;
PROCEDURE
    : 'PROCEDURE'
    ;
BEGIN
    : 'BEGIN'
    ;
END
    : 'END'
    ;
LP
    : '('
    ;
RP
    : ')'
    ;
LB
    : '['
    ;
RB
    : ']'
    ;
SC
    : ';'
    ;
COL
    : ':'
    ;
DOT
    : '.'
    ;
DOTDOT
    : '..'
    ;
NUM
    : NUM_INT
    | NUM_REAL
    ;
NUM_INT
    : ('0' .. '9')+
    ;
NUM_REAL
    : ('0' .. '9')+ (('.' ('0' .. '9')+ (EXPONENT)?)? | EXPONENT)
    ;
fragment EXPONENT
    : ('E') ('+' | '-')? ('0' .. '9')+
    ;
NOT
    : 'NOT'
    ;
BREAK
    : ','
    ;
ASSIGN
    : ':='
    ;
REL
    : EQUAL
    | NOT_EQUAL
    | LT
    | LE
    | GE
    | GT
    | IN
    ;
EQUAL
    : '='
    ;
NOT_EQUAL
    : '<>'
    ;
LT
    : '<'
    ;
LE
    : '<='
    ;
GE
    : '>='
    ;
GT
    : '>'
    ;
IN
    : 'IN'
    ;

add
    : PLUS
    | MINUS
    | OR
    ;
PLUS
    : '+'
    ;
MINUS
    : '-'
    ;
OR
    : 'OR'
    ;
mul
    : STAR
    | SLASH
    | DIV
    | MOD
    | AND
    ;
STAR
    : '*'
    ;
SLASH
    : '/'
    ;
DIV
    : 'DIV'
    ;
MOD
    : 'MOD'
    ;
AND
    : 'AND'
    ;
IF
    : 'IF'
    ;
THEN
    : 'THEN'
    ;
ELSE
    : 'ELSE'
    ;
WHILE
    : 'WHILE'
    ;
DO
    : 'DO'
    ;
INTEGER
    : 'INTEGER'
    ;
REAL
    : 'REAL'
    ;
OF
    : 'OF'
    ;
VAR
    : 'VAR'
    ;
ARRAY
    : 'ARRAY'
    ;
ID
    : ('A' .. 'Z') ('A' .. 'Z' | '0' .. '9' | '_')*
    ;

