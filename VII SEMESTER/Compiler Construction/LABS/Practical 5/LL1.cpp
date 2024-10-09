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

void follow(map<char, vector<string>> &regex, char ch, set<char> &F, char startSymbol, set<char> &visited)
{
    if (visited.find(ch) != visited.end())
        return;
    visited.insert(ch);
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
                                follow(regex, nextChar, F, startSymbol, visited);
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
                            follow(regex, rule.first, F, startSymbol, visited);
                        }
                    }
                }
            }
        }
    }
}

void printTable(map<char, map<char, string>> &table)
{
    cout << "\nLL(1) Parsing Table:\n";
    for (auto &row : table)
    {
        cout << row.first << " : ";
        for (auto &col : row.second)
        {
            cout << "[" << col.first << " -> " << col.second << "] ";
        }
        cout << endl;
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

    map<char, map<char, string>> table;

    for (auto &it : regex)
    {
        set<char> F;
        char ch = it.first;
        first(regex, ch, F);
        for (auto &str : it.second)
        {
            set<char> firstSet;
            if (isupper(str[0]))
            {
                first(regex, str[0], firstSet);
            }
            else
            {
                firstSet.insert(str[0]);
            }

            for (auto &terminal : firstSet)
            {
                if (terminal != '#')
                {
                    table[ch][terminal] = str;
                }
                else
                {
                    set<char> followSet;
                    set<char> visited;
                    follow(regex, ch, followSet, startSymbol, visited);
                    for (auto &f : followSet)
                    {
                        table[ch][f] = str;
                    }
                    if (followSet.find('$') != followSet.end())
                    {
                        table[ch]['$'] = str;
                    }
                }
            }
        }
    }

    printTable(table);

    return 0;
}
