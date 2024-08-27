#include <stdio.h>
#include <string.h>

int isComment(char s[]) {
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

int main()
{
    while(1){
    char s[200];
    printf("Enter a line of text: ");
    fgets(s, sizeof(s), stdin);

    if (isComment(s))
    {
        printf("The line is a comment.\n");
    }
    else
    {
        printf("The line is not a comment.\n");
    }
    }
    return 0;
}
