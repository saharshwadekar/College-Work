#include <map>
#include <vector>
#include <string>
#include <iostream>

using namespace std;

bool isIdentifier(string s)
{
    map<char, vector<string>> keyword_map = {
        {'a', {"alignas", "alignof", "and", "and_eq", "asm", "auto"}},
        {'b', {"bitand", "bitor", "bool", "break"}},
        {'c', {"case", "catch", "char", "char16_t", "char32_t", "class", "compl", "const", "const_cast", "constexpr", "continue"}},
        {'d', {"decltype", "default", "delete", "do", "double", "dynamic_cast"}},
        {'e', {"else", "enum", "explicit", "export", "extern"}},
        {'f', {"false", "float", "for", "friend"}},
        {'g', {"goto"}},
        {'i', {"if", "inline", "int"}},
        {'l', {"long"}},
        {'m', {"mutable"}},
        {'n', {"namespace", "new", "noexcept", "not", "not_eq", "nullptr"}},
        {'o', {"operator", "or", "or_eq"}},
        {'p', {"private", "protected", "public"}},
        {'r', {"register", "reinterpret_cast", "return"}},
        {'s', {"short", "signed", "sizeof", "static", "static_assert", "static_cast", "struct", "switch"}},
        {'t', {"template", "this", "thread_local", "throw", "true", "try", "typedef", "typeid", "typename"}},
        {'u', {"union", "unsigned", "using"}},
        {'v', {"virtual", "void", "volatile"}},
        {'w', {"wchar_t", "while"}},
        {'x', {"xor", "xor_eq"}}
    };

    for (const auto& key : keyword_map) {

        if (s[0] == key.first)
        {
            for (const auto& keyword : key.second) {
                if(s == keyword){
                    return true;
                }
            }
        }
    }
    return false;
}

int main() {
    string s;
    cout << "Enter Your String : ";
    cin >> s;
    if(isIdentifier(s))
        cout << "Entered string is Identifier.";
    else
        cout << "Entered string is non Identifer.";
    return 0;
}
