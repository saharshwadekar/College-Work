#include <stdio.h>
#include <ctype.h>

int identifier(char s[])
{
    if(!isalnum(s[0]) && s[0] != "_")
        return 0;

    for (int i = 1; s[i] != '\0'; i++)
    {
        if(!isalnum(s[i]) && s[i]!='\0')
            return 0;
    }
    return 1;
}

int main()
{
    char s[100];
    printf("Enter the indentifier: ");
    scanf("%s", &s);
    if(identifier(s))
        printf("TRUE");
    else
        printf("FALSE");
    return 0;
}