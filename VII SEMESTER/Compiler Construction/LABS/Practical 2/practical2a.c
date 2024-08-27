#include <stdio.h>
#include <ctype.h>

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

int main()
{
    char s[100];
    printf("Enter the identifier: ");
    scanf("%s", s);

    if (isValidIdentifier(s))
    {
        printf("\"%s\" is a valid identifier.\n", s);
    }
    else
    {
        printf("\"%s\" is not a valid identifier.\n", s);
    }
    return 0;
}
