/**********************************************************************************
 *                                PRACTICAL NO: 2C                                *
 **********************************************************************************/
#include <iostream>
#include <string>
#include <cctype>
#include <unordered_set>
#include <vector>

using namespace std;

enum TokenType {
    KEYWORD, IDENTIFIER, CONSTANT, OPERATOR, PUNCTUATION, UNKNOWN
};

struct Token {
    string value;
    TokenType type;
};

unordered_set<string> keywords = {"if", "else", "while", "for", "return", "int", "float", "void", 
                                   "char", "double", "long", "short", "signed", "unsigned", "const", 
                                   "static", "extern", "typedef", "struct", "union", "enum", "sizeof"};

unordered_set<string> operators = {"+", "-", "*", "/", "%", "++", "--", "==", "!=", "<", ">", "<=", ">=", 
                                    "&&", "||", "!", "&", "|", "^", "~", "<<", ">>", "=", "+=", "-=", "*=", 
                                    "/=", "%=", "&=", "^=", "|=", "<<=", ">>="};

unordered_set<char> punctuations = {';', ',', '(', ')', '{', '}', '[', ']', '#', ':', '?'};

TokenType identifyToken(const string& token) {
    if (keywords.count(token)) return KEYWORD;
    if (token.find_first_not_of("0123456789") == string::npos) return CONSTANT;
    if (operators.count(token)) return OPERATOR;
    if (token.size() == 1 && punctuations.count(token[0])) return PUNCTUATION;
    if (!token.empty() && (isalpha(token[0]) || token[0] == '_')) return IDENTIFIER;
    return UNKNOWN;
}

vector<Token> lexicalAnalyser(const string& s) {
    vector<Token> tokens;
    string token;
    size_t i = 0;

    while (i < s.size()) {
        char ch = s[i];

        if (punctuations.count(ch)) {
            if (!token.empty()) {
                tokens.push_back({token, identifyToken(token)});
                token.clear();
            }
            tokens.push_back({string(1, ch), PUNCTUATION});
        }
        else if (operators.find(string(1, ch)) != operators.end() || (ch == '!' || ch == '#' || ch == ':' || ch == '?')) {
            if (!token.empty()) {
                tokens.push_back({token, identifyToken(token)});
                token.clear();
            }
            string op(1, ch);
            if (i + 1 < s.size()) {
                string nextOp(1, s[i + 1]);
                if (operators.count(op + nextOp)) {
                    op += s[i + 1];
                    ++i;
                }
            }
            tokens.push_back({op, OPERATOR});
        }
        else if (isspace(ch)) {
            if (!token.empty()) {
                tokens.push_back({token, identifyToken(token)});
                token.clear();
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
        cout << "< " << token.value << " ,";
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
