#include <bits\stdc++.h>
using namespace std;

void first(map<char, vector<string>> regex, char ch, set<char> &F)
{
    vector<string> exp = regex[ch];
    for (const auto &t : exp)
    {
        char f = t[0];
        if (isupper(f) && f != ch)
            first(regex, f, F);
        else if (f != ch)
            F.insert(f);
    }
}

void follow(map<char, vector<string>> regex, char ch, set<char> &F)
{
    map<char, vector<string>>::iterator it = regex.begin();
    while (it != regex.end())
    {
        vector<string> exp = it->second;
        for (const auto &t : exp)
        {
            bool flag = false;
            bool find = false;
            for (auto &c : t)
            {
                if (flag)
                {
                    flag = false;
                    if (isupper(c) && c != ch)
                        first(regex, c, F);
                    else if (c != ch)
                        F.insert(c);
                }
                if (c == ch)
                {
                    flag = true;
                    find = true;
                }
            }
            if (flag && find)
            {
                flag = false;
                find = false;
                follow(regex, ch, F);
            }
        }
    }
}

int main()
{
    map<char, vector<string>> regex;
    int size;

    cout << "How many regular Expression :";
    cin >> size;

    for (int i = 0; i < size; ++i)
    {
        char header;
        vector<string> expression;
        string s, t;

        cout << "Enter Header: ";
        cin >> header;
        cout << "Enter Expresssion: ";
        cin >> s;

        stringstream X(s);
        while (getline(X, t, '|'))
        {
            expression.push_back(t);
        }
        regex[header] = expression;
    }

    map<char, vector<string>>::iterator it = regex.begin();

    while (it != regex.end())
    {
        set<char> F;
        char ch = it->first;
        first(regex, ch, F);
        cout << ch << "->";
        for (auto &str : F)
        {
            std::cout << str << ' ';
        }
        cout << endl;
        ++it;
    }

    return 0;
}