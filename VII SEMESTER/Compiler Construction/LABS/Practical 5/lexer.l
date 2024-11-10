%{
#include "parser.tab.h"
%}

%%
a      return 'a';
b      return 'b';
\n     return '\n'; // For recognizing newlines
[ \t]  ;            // Ignore whitespace
.      return yytext[0];
%%

int yywrap() {
    return 1;
}
