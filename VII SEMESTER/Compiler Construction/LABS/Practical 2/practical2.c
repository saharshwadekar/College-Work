#include <stdio.h>
#include <string.h>
#include <ctype.h>

int isValid(char s[]) {
    if (!isalpha(s[0]) && s[0] != '_') {
        return 0;
    }

    for (int i = 1; s[i] != '\0'; i++) {
        if (!isalnum(s[i]) && s[i] != '_') {
            return 0;
        }
    }

    return 1;
}

int identifyComment(char s[]) {
    int i = 0;
    int length = strlen(s);

    while (i < length - 1) {
        if (s[i] == '/' && s[i + 1] == '/') {
            return 1;
        }
        if (s[i] == '/' && s[i + 1] == '*') {
            i += 2;
            while (i < length - 1) {
                if (s[i] == '*' && s[i + 1] == '/') {
                    return 1;
                }
                i++;
            }
            printf("ERROR: Your comment does not end with '*/'\n\n");
            return 1;
        }
        i++;
    }

    return 0;
}

int isKeyword(char s[]) {
    char *keywords[] = {
        "auto", "break", "case", "char", "const", "continue", "default", "do", "double", "else", "enum", "extern",
        "float", "for", "goto", "if", "int", "long", "register", "return", "short", "signed", "sizeof", "static",
        "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while", "_Alignas", "_Alignof",
        "_Atomic", "_Bool", "_Complex", "_Generic", "_Imaginary", "_Noreturn", "_Static_assert", "_Thread_local"
    };
    int keyword_count = sizeof(keywords) / sizeof(keywords[0]);

    for (int i = 0; i < keyword_count; i++) {
        if (strcmp(s, keywords[i]) == 0) {
            return 1;
        }
    }

    return 0;
}

int main() {
    char s[100];
    printf("Enter Your String: ");
    fgets(s, sizeof(s), stdin);

    s[strcspn(s, "\n")] = '\0';

    if (isValid(s)) {
        if (isKeyword(s)) {
            printf("\"%s\" is a keyword.\n", s);
        } else {
            printf("\"%s\" is a valid identifier.\n", s);
        }
    } else {
        printf("\"%s\" is not a valid identifier.\n", s);
    }

    if (identifyComment(s)) {
        printf("Your string consists of a comment!\n");
    } else {
        printf("Your string does not consist of a comment.\n");
    }

    return 0;
}
