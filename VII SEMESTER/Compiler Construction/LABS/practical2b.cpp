#include <iostream>
#include <string>

using namespace std;

bool identifyComment(string s)
{
    int count = 0;
    bool flag = false;
    for (int i = 0; i < s.length(); i++)
    {
        if (!flag)
        {
            if (s[i] == '/' && s[i + 1] == '/')
            {
                return true;
            }
            if (s[i] == '/' && s[i + 1] == '*')
            {
                flag = true;
                count++;
            }
        }
        else if (s[i] == '*' && s[i + 1] == '/')
            count++;

        if (count == 2)
            return true;
    }
    if (flag == true && count == 1)
    {
        cout << "ERROR : Your comment does not ends with '*/'\n\n";
        return true;
    }
    return false;
}

int main()
{
    string s;
    cout << "Enter Your String : ";
    getline(cin,s);
    if (identifyComment(s))
        cout << "Your string consist of comment!";
    else
        cout << "Your string does not consist of comment";
    return 0;
}

