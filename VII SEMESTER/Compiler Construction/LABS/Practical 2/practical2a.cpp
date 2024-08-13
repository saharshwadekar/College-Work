// #include <iostream>
// #include <string>

// using namespace std;

// bool isValid(string s)
// {
//     if (s[0] == char(32) || isdigit(s[0]))
//         return false;

//     for(const auto& ch: s){
//         if(!(ch =='_' || isalnum(ch))){
//             return false;
//         }
//     }
//     return true;
// }

// int main()
// {
//     string s;
//     cout << "Enter Your String : ";
//     getline(cin, s);

//     if (isValid(s))
//         cout << "\"" << s << "\" is valid Identifier.";
//     else
//         cout << "\"" << s << "\" is not valid Identifer.";
//     return 0;
// }

#include <iostream>
#include <string>
#include <cctype>
#include <vector>
#include <algorithm>

using namespace std;

bool isValid(const string &s)
{
    if (s.empty() || !(isalpha(s[0]) || s[0] == '_'))
        return false;

    for (char ch : s)
    {
        if (!(isalnum(ch) || ch == '_'))
        {
            return false;
        }
    }

    return true;
}

bool identifyComment(const string &s)
{
    size_t singleLineComment = s.find("//");
    size_t multiLineCommentStart = s.find("/*");
    size_t multiLineCommentEnd = s.find("*/");

    if (singleLineComment != string::npos)
    {
        return true;
    }

    if (multiLineCommentStart != string::npos)
    {
        if (multiLineCommentEnd != string::npos && multiLineCommentEnd > multiLineCommentStart)
        {
            return true;
        }
        else
        {
            cout << "ERROR: Your comment does not end with '*/'\n\n";
            return true;
        }
    }

    return false;
}

bool isKeyword(const string &s)
{
    vector<string> keywords = {
        "alignas", "alignof", "and", "and_eq", "asm", "auto",
        "bitand", "bitor", "bool", "break",
        "case", "catch", "char", "char16_t", "char32_t", "class", "compl", "const", "const_cast", "constexpr", "continue",
        "decltype", "default", "delete", "do", "double", "dynamic_cast",
        "else", "enum", "explicit", "export", "extern",
        "false", "float", "for", "friend",
        "goto",
        "if", "inline", "int",
        "long",
        "mutable",
        "namespace", "new", "noexcept", "not", "not_eq", "nullptr",
        "operator", "or", "or_eq",
        "private", "protected", "public",
        "register", "reinterpret_cast", "return",
        "short", "signed", "sizeof", "static", "static_assert", "static_cast", "struct", "switch",
        "template", "this", "thread_local", "throw", "true", "try", "typedef", "typeid", "typename",
        "union", "unsigned", "using",
        "virtual", "void", "volatile",
        "wchar_t", "while",
        "xor", "xor_eq"};

    return find(keywords.begin(), keywords.end(), s) != keywords.end();
}

int main()
{
    string s;
    cout << "Enter Your String: ";
    getline(cin, s);

    if (isValid(s))
    {
        if (isKeyword(s))
        {
            cout << "\"" << s << "\" is a keyword.\n";
        }
        else
        {
            cout << "\"" << s << "\" is a valid identifier.\n";
        }
    }
    else
    {
        cout << "\"" << s << "\" is not a valid identifier.\n";
    }

    if (identifyComment(s))
    {
        cout << "Your string consists of a comment!\n";
    }
    else
    {
        cout << "Your string does not consist of a comment.\n";
    }

    return 0;
}
