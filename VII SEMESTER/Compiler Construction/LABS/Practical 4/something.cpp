/*

E -> iE'
E' -> +iE' | #

*/

#include <bits/stdc++.h>

using namespace std;

void match(char a, char b)
{
  if(a != b)
    throw invalid_argument("LL(1) Grammer Not Follows");
}

void EI()
{
  char ch = getchar();
  match(ch, '+');
  ch = getchar();
  match(ch, 'i');
}

void E()
{
  char ch = getchar();
  match(ch, 'i');
  EI();
}


int main()
{

  try
  {
    E();
    char ch = getchar();
    match(ch, '$');
    cout << "Successfully Executed LL(1) Grammer" << endl;
  }
  catch(const std::exception& e)
  {
    std::cerr << e.what() << '\n';
  }
  
  return 0;
}