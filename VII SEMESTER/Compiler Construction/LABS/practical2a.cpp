#include <iostream>
#include <string>

using namespace std;

bool isValid(string s)
{
    for(const auto& ch: s){
        if(ch == char(32) || isdigit(ch) && !(ch =='_' || isalpha(ch))){
            return false;
        }
    }
    return true;
}

int main()
{
    string s;
    cout << "Enter Your String : ";
    getline(cin, s);

    if (isValid(s))
        cout << "string is valid Identifier.";
    else
        cout << "string is not valid Identifer.";
    return 0;
}