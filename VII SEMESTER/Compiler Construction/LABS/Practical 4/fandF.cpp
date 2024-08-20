#include <bits/stdc++.h>
using namespace std;

void first(map<char, vector<string>> &regex, char ch, set<char> &F)
{
    vector<string> exp = regex[ch];
    for (const auto &t : exp)
    {
        char f = t[0];
        if (isupper(f) && f != ch)
        {
            first(regex, f, F);
        }
        else
        {
            F.insert(f);
        }
    }
}

void follow(map<char, vector<string>> &regex, char ch, set<char> &F, char startSymbol)
{
    if (ch == startSymbol)
    {
        F.insert('$');
    }

    for (auto &rule : regex)
    {
        vector<string> exp = rule.second;
        for (const auto &t : exp)
        {
            for (size_t i = 0; i < t.length(); ++i)
            {
                if (t[i] == ch)
                {
                    if (i + 1 < t.length())
                    {
                        char nextChar = t[i + 1];
                        if (isupper(nextChar))
                        {
                            set<char> tempFirst;
                            first(regex, nextChar, tempFirst);
                            if (tempFirst.find('#') != tempFirst.end())
                            {
                                tempFirst.erase('#');
                                F.insert(tempFirst.begin(), tempFirst.end());
                                follow(regex, nextChar, F, startSymbol);
                            }
                            else
                            {
                                F.insert(tempFirst.begin(), tempFirst.end());
                            }
                        }
                        else
                        {
                            F.insert(nextChar);
                        }
                    }
                    else
                    {
                        if (rule.first != ch)
                        {
                            follow(regex, rule.first, F, startSymbol);
                        }
                    }
                }
            }
        }
    }
}

int main()
{
    map<char, vector<string>> regex;
    int size;
    char startSymbol;

    cout << "How many regular Expressions: ";
    cin >> size;

    for (int i = 0; i < size; ++i)
    {
        char header;
        vector<string> expression;
        string s, t;

        cout << "Enter Header: ";
        cin >> header;
        cout << header << "->";
        cin >> s;
        if (i == 0)
            startSymbol = header;

        stringstream X(s);
        while (getline(X, t, '|'))
        {
            expression.push_back(t);
        }
        regex[header] = expression;
    }

    cout << "\nFIRST sets:\n";
    for (auto &it : regex)
    {
        set<char> F;
        char ch = it.first;
        first(regex, ch, F);
        cout << ch << " -> ";
        for (auto &str : F)
        {
            cout << str << ' ';
        }
        cout << endl;
    }

    cout << "\nFOLLOW sets:\n";
    for (auto &it : regex)
    {
        set<char> F;
        char ch = it.first;
        follow(regex, ch, F, startSymbol);
        cout << ch << " -> ";
        for (auto &str : F)
        {
            cout << str << ' ';
        }
        cout << endl;
    }

    return 0;
}
