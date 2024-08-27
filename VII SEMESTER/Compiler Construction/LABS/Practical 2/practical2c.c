#include <stdio.h>
#include <string.h>
#include <ctype.h>

const char *keywords[] = {
    "auto", "break", "case", "char", "const", "continue", "default", "do", "double", "else", "enum", "extern",
    "float", "for", "goto", "if", "int", "long", "register", "return", "short", "signed", "sizeof", "static",
    "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while"};

int isKeyword(char s[])
{
    for (int i = 0; i < sizeof(keywords) / sizeof(keywords[0]); i++)
    {
        if (strcmp(s, keywords[i]) == 0)
        {
            return 1;
        }
    }
    return 0;
}

int isValidIdentifier(char s[])
{
    if (!isalpha(s[0]) && s[0] != '_')
    {
        return 0;
    }
    for (int i = 1; s[i] != '\0'; i++)
    {
        if (!isalnum(s[i]) && s[i] != '_')
        {
            return 0;
        }
    }
    return 1;
}

int isConstant(char s[])
{
    for (int i = 0; s[i] != '\0'; i++)
    {
        if (!isdigit(s[i]))
        {
            return 0;
        }
    }
    return 1;
}

int main()
{
    char s[100];
    printf("Enter the string: ");
    scanf("%s", s);

    if (isKeyword(s))
    {
        printf("\"%s\" is a keyword.\n", s);
    }
    else if (isConstant(s))
    {
        printf("\"%s\" is a constant.\n", s);
    }
    else if (isValidIdentifier(s))
    {
        printf("\"%s\" is a valid identifier.\n", s);
    }
    else
    {
        printf("\"%s\" is not a valid identifier.\n", s);
    }
    return 0;
}
