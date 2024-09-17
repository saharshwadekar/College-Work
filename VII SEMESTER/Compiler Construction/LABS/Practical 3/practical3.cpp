#include <bits/stdc++.h>
using namespace std;

enum TokenType {
    KEYWORD, IDENTIFIER, CONSTANT, OPERATOR, PUNCTUATION, UNKNOWN
};

struct Token {
    string value;
    TokenType type;
};

unordered_set<string> keywords = {"if", "else", "while", "for", "return", "int", "float", "void"};
unordered_set<char> operators = {'+', '-', '*', '/', '=', '<', '>', '!'};
unordered_set<char> punctuations = {';', '(', ')', '{', '}', ','};

TokenType identifyToken(const string& token) {
    if (keywords.find(token) != keywords.end()) {
        return KEYWORD;
    } else if (all_of(token.begin(), token.end(), ::isdigit)) {
        return CONSTANT;
    } else if (token.size() == 1 && operators.find(token[0]) != operators.end()) {
        return OPERATOR;
    } else if (token.size() == 1 && punctuations.find(token[0]) != punctuations.end()) {
        return PUNCTUATION;
    } else if (!token.empty() && (isalpha(token[0]) || token[0] == '_')) {
        return IDENTIFIER;
    }
    return UNKNOWN;
}

vector<Token> lexicalAnalyser(const string& s) {
    vector<Token> tokens;
    string token = "";
    size_t i = 0;

    while (i < s.size()) {
        char ch = s[i];

        if (punctuations.find(ch) != punctuations.end()) {
            if (!token.empty()) {
                tokens.push_back({token, identifyToken(token)});
                token = "";
            }
            tokens.push_back({string(1, ch), PUNCTUATION});
        }
        else if (operators.find(ch) != operators.end()) {
            if (!token.empty()) {
                tokens.push_back({token, identifyToken(token)});
                token = "";
            }
            string op(1, ch);
            if (i + 1 < s.size() && operators.find(s[i + 1]) != operators.end()) {
                op += s[i + 1];
                ++i;
            }
            tokens.push_back({op, OPERATOR});
        }
        else if (isspace(ch)) {
            if (!token.empty()) {
                tokens.push_back({token, identifyToken(token)});
                token = "";
            }
        }
        else {
            token += ch;
        }
        ++i;
    }
    if (!token.empty()) {
        tokens.push_back({token, identifyToken(token)});
    }

    return tokens;
}

void printTokens(const vector<Token>& tokens) {
    for (const auto& token : tokens) {
        if (token.value.empty()) continue; // Skip empty tokens
        cout << "Token: <" << token.value << ", ";
        switch (token.type) {
            case KEYWORD: cout << "KEYWORD >"; break;
            case IDENTIFIER: cout << "IDENTIFIER >"; break;
            case CONSTANT: cout << "CONSTANT >"; break;
            case OPERATOR: cout << "OPERATOR >"; break;
            case PUNCTUATION: cout << "PUNCTUATION >"; break;
            default: cout << "UNKNOWN >"; break;
        }
        cout << endl;
    }
}

int main() {
    string s;
    cout << "Enter Your String: ";
    getline(cin, s);

    vector<Token> tokens = lexicalAnalyser(s);
    printTokens(tokens);

    return 0;
}