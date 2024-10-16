#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <iomanip>

using namespace std;

vector<vector<string>> S = {
    {"63","7c","77","7b","f2","6b","6f","c5","30","01","67","2b","fe","d7","ab","76"},
    {"ca","82","c9","7d","fa","59","47","f0","ad","d4","a2","af","9c","a4","72","c0"},
    {"b7","fd","93","26","36","3f","f7","cc","34","a5","e5","f1","71","d8","31","15"},
    {"04","c7","23","c3","18","96","05","9a","07","12","80","e2","eb","27","b2","75"},
    {"09","83","2c","1a","1b","6e","5a","a0","52","3b","d6","b3","29","e3","2f","84"},
    {"53","d1","00","ed","20","fc","b1","5b","6a","cb","be","39","4a","4c","58","cf"},
    {"d0","ef","aa","fb","43","4d","33","85","45","f9","02","7f","50","3c","9f","a8"},
    {"51","a3","40","8f","92","9d","38","f5","bc","b6","da","21","10","ff","f3","d2"},
    {"cd","0c","13","ec","5f","97","44","17","c4","a7","7e","3d","64","5d","19","73"},
    {"60","81","4f","dc","22","2a","90","88","46","ee","b8","14","de","5e","0b","db"},
    {"e0","32","3a","0a","49","06","24","5c","c2","d3","ac","62","91","95","e4","79"},
    {"e7","c8","37","6d","8d","d5","4e","a9","6c","56","f4","ea","65","7a","ae","08"},
    {"ba","78","25","2e","1c","a6","b4","c6","e8","dd","74","1f","4b","bd","8b","8a"},
    {"70","3e","b5","66","48","03","f6","0e","61","35","57","b9","86","c1","1d","9e"},
    {"e1","f8","98","11","69","d9","8e","94","9b","1e","87","e9","ce","55","28","df"},
    {"8c","a1","89","0d","bf","e6","42","68","41","99","2d","0f","b0","54","bb","16"}
};

vector<string> Rconst = {
    "00000000", "01000000", "02000000", "04000000", "08000000",
    "10000000", "20000000", "40000000", "80000000", "1B000000", "36000000"
};

vector<string> xorOperation(const vector<string> &text, const vector<string> &keywords) {
    vector<string> result = text;
    for (size_t i = 0; i < text.size(); ++i) {
        unsigned int txt = stoul(text[i], nullptr, 16);
        unsigned int key = stoul(keywords[i], nullptr, 16);
        stringstream stream;
        stream << hex << setw(8) << setfill('0') << (txt ^ key);
        result[i] = stream.str();
    }
    return result;
}

vector<string> SubBytes(vector<string> text) {
    string idx = "0123456789abcdef";
    for (size_t i = 0; i < text.size(); ++i) {
        string newWord;
        for (size_t j = 0; j < 8; j += 2) {
            int x = idx.find(text[i][j]);
            int y = idx.find(text[i][j+1]);
            newWord += S[x][y];
        }
        text[i] = newWord;
    }
    return text;
}

vector<string> shiftRows(const vector<string> &text) {
    string fullText = text[0] + text[1] + text[2] + text[3];
    string w1 = fullText.substr(0, 2) + fullText.substr(10, 2) + fullText.substr(20, 2) + fullText.substr(30, 2);
    string w2 = fullText.substr(8, 2) + fullText.substr(18, 2) + fullText.substr(28, 2) + fullText.substr(6, 2);
    string w3 = fullText.substr(16, 2) + fullText.substr(26, 2) + fullText.substr(4, 2) + fullText.substr(14, 2);
    string w4 = fullText.substr(24, 2) + fullText.substr(2, 2) + fullText.substr(12, 2) + fullText.substr(22, 2);
    return {w1, w2, w3, w4};
}

int gmul(int a, int b) {
    if (b == 1) return a;
    int tmp = (a << 1) & 0xff;
    if (b == 2) return (a < 128) ? tmp : tmp ^ 0x1b;
    if (b == 3) return gmul(a, 2) ^ a;
    return 0;
}

vector<string> MixColumn(vector<string> text) {
    for (size_t i = 0; i < text.size(); ++i) {
        int a = stoi(text[i].substr(0, 2), nullptr, 16);
        int b = stoi(text[i].substr(2, 4), nullptr, 16);
        int c = stoi(text[i].substr(4, 6), nullptr, 16);
        int d = stoi(text[i].substr(6, 8), nullptr, 16);

        string w1 = to_string(gmul(a, 2) ^ gmul(b, 3) ^ gmul(c, 1) ^ gmul(d, 1));
        string w2 = to_string(gmul(a, 1) ^ gmul(b, 2) ^ gmul(c, 3) ^ gmul(d, 1));
        string w3 = to_string(gmul(a, 1) ^ gmul(b, 1) ^ gmul(c, 2) ^ gmul(d, 3));
        string w4 = to_string(gmul(a, 3) ^ gmul(b, 1) ^ gmul(c, 1) ^ gmul(d, 2));

        text[i] = w1 + w2 + w3 + w4;
    }
    return text;
}

vector<string> generateKey(const vector<string> &keywords, int roundCount) {
    string Rcnst = Rconst[roundCount];
    string four = keywords.back().substr(2) + keywords.back().substr(0, 2); // Rotate word
    vector<string> subbed = SubBytes({four});
    four = xorOperation(subbed, {Rcnst})[0];  // XOR with Rconst
    vector<string> newKeywords;
    newKeywords.push_back(four);

    for (size_t i = 0; i < keywords.size(); ++i) {
        newKeywords.push_back(xorOperation({newKeywords[i]}, {keywords[i]})[0]);
    }

    newKeywords.erase(newKeywords.begin());
    return newKeywords;
}

void printAES(const string &round, const vector<string> &text, const vector<string> &state, const vector<string> &keyword) {
    cout << string(60, '-') << "\n";
    for (int i = 0; i < 4; ++i) {
        if (i == 2) {
            cout << "| " << setw(10) << round << " | ";
        } else {
            cout << "| " << setw(10) << " " << " | ";
        }
        cout << text[0].substr(i*2, 2) << " " << text[1].substr(i*2, 2) << " " << text[2].substr(i*2, 2) << " " << text[3].substr(i*2, 2) << " | ";
        cout << state[0].substr(i*2, 2) << " " << state[1].substr(i*2, 2) << " " << state[2].substr(i*2, 2) << " " << state[3].substr(i*2, 2) << " | ";
        cout << keyword[0].substr(i*2, 2) << " " << keyword[1].substr(i*2, 2) << " " << keyword[2].substr(i*2, 2) << " " << keyword[3].substr(i*2, 2) << " |\n";
    }
    cout << string(60, '-') << "\n";
}

void advanceEncryptionStandard(vector<string> plaintext, vector<string> keywords) {
    vector<string> stateMatrix = xorOperation(plaintext, keywords);
    printAES("PreRound", plaintext, stateMatrix, keywords);

    for (int roundCount = 1; roundCount <= 10; ++roundCount) {
        vector<string> pt = stateMatrix;
        stateMatrix = SubBytes(stateMatrix);
        stateMatrix = shiftRows(stateMatrix);
        if (roundCount != 10) {
            stateMatrix = MixColumn(stateMatrix);
        }
        keywords = generateKey(keywords, roundCount);
        stateMatrix = xorOperation(stateMatrix, keywords);
        printAES(to_string(roundCount), pt, stateMatrix, keywords);
    }
}

int main() {
    cout << "Enter PlainText (in HEX format XXXX XXXX XXXX XXXX): ";
    string input;
    vector<string> plaintext(4), keywords(4);
    for (auto &p : plaintext) cin >> p;
    cout << "Enter Your Key (in HEX format XXXX XXXX XXXX XXXX): ";
    for (auto &k : keywords) cin >> k;

    if (plaintext.size() != 4 || keywords.size() != 4) {
        cout << "There must be 4 input keys.\n";
        return 0;
    }

    for (size_t i = 0; i < 4; ++i) {
        if (plaintext[i].length() != 8 || keywords[i].length() != 8) {
            cout << "Each input key must be 8 hex characters long!\n";
            return 0;
        }
    }

    advanceEncryptionStandard(plaintext, keywords);
    return 0;
}
