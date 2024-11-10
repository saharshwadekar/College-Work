%{
    #include "parser.tab.h"
%}

%%

"id"        { return ID; }
"+"         { return PLUS; }
"("         { return LPAREN; }
")"         { return RPAREN; }
"$"         { return DOLLAR; }
[ \t\n]+    ;  // Ignore whitespaces
.           { printf("Unexpected character: %s\n", yytext); }

%%

int yywrap() {
    return 1;
}
