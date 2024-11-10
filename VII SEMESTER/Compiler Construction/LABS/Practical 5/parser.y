%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_RULES 100
#define MAX_SYMBOLS 100

typedef struct {
    char non_terminal;
    char production[10];
} Rule;

Rule rules[MAX_RULES];
int rule_count = 0;
char first[MAX_SYMBOLS][MAX_SYMBOLS], follow[MAX_SYMBOLS][MAX_SYMBOLS];
char parsing_table[MAX_SYMBOLS][MAX_SYMBOLS];
char non_terminals[MAX_SYMBOLS];
int nt_count = 0;

void compute_first();
void compute_follow();
void create_parsing_table();
void print_parsing_table();

%}

%token a b
%left 'ε'

%%
Grammar:
    Rules { 
        compute_first();
        compute_follow();
        create_parsing_table();
        print_parsing_table();
    }
;

Rules:
    Rule
    | Rules Rule
;

Rule:
    NonTerminal '→' Production { 
        rules[rule_count].non_terminal = $1;
        strcpy(rules[rule_count].production, $3);
        rule_count++;
        
        if (strchr(non_terminals, $1) == NULL) {
            non_terminals[nt_count++] = $1;
        }
    }
;

NonTerminal:
    'S' { $$ = 'S'; }
    | 'A' { $$ = 'A'; }
    | 'B' { $$ = 'B'; }
;

Production:
    'a' { $$ = "a"; }
    | 'b' { $$ = "b"; }
    | 'ε' { $$ = "ε"; }
;
%%

int main() {
    yyparse();
    return 0;
}

void compute_first() {
    printf("First sets:\n");
    for (int i = 0; i < nt_count; i++) {
        printf("First(%c): {a, b, ε}\n", non_terminals[i]); // Placeholder
    }
}

void compute_follow() {
    printf("Follow sets:\n");
    for (int i = 0; i < nt_count; i++) {
        printf("Follow(%c): {a, b, $}\n", non_terminals[i]); // Placeholder
    }
}

void create_parsing_table() {
    printf("Creating parsing table...\n");
}

void print_parsing_table() {
    printf("Predictive Parsing Table:\n");
}