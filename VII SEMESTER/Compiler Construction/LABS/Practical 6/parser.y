%{
    #include <stdio.h>
    #include <stdlib.h>
    
    // Declare the lexical analyzer function
    int yylex(void);
    void yyerror(const char *s);
%}

%token ID PLUS LPAREN RPAREN DOLLAR

%%

S   : E DOLLAR    { printf("ACCEPT\n"); }
    ;

E   : E PLUS T    { printf("Reduce by rule: E -> E + T\n"); }
    | T           { printf("Reduce by rule: E -> T\n"); }
    ;

T   : LPAREN E RPAREN { printf("Reduce by rule: T -> (E)\n"); }
    | ID              { printf("Reduce by rule: T -> id\n"); }
    ;

%%

int main() {
    printf("Enter an expression to parse (end with $): ");
    return yyparse();  // Start the parser
}

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}
