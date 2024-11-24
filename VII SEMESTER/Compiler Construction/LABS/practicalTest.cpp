// #include <bits/stdc++.h>
// using namespace std;

// unordered_set<string> keyword = {"if", "do", "for", "else", "continue", "auto","break"};
// unordered_set<string> operators = {"+","-","/","*", "="};

// string identify(const string& token)
// {
//     if (keyword.find(token) != keyword.end())
//         return "KEYWORD";
//     else if (operators.find(token) != operators.end())
//         return "OPERATOR";
//     else if (isalpha(token[0]) || token[0] == '_' )
//         return "IDENTIFIER";
//     else if (isdigit(token[0]) )
//         return "CONSTANT";
//     else
//         return "UNKNOWN";
// }

// void analyseToken(const string& input)
// {
//     string token = "";
//     vector<string> result;

//     for(const auto& ch: input)
//     {
//         if(isspace(ch) && (!token.empty()))
//         {
//             result.push_back("<" + token + "," + identify(token) + ">");
//             token.clear();
//         }
//         else
//             token += ch;
//     }
//     result.push_back("<" + token + "," + identify(token) + ">");
//     token.clear();

//     for(const auto& token : result)
//         cout << token << endl;
// }

// int main()
// {
//     string input;
//     cout << "Enter :";
//     getline(cin, input);
//     analyseToken(input);
//     return 0;
// }





// practical 2


