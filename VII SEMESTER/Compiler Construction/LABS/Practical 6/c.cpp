#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct Production {
    string lhs;  // Left-hand side of the production
    string rhs;  // Right-hand side of the production
};

int main() {
    int numProductions;
    cout << "Enter the number of productions: ";
    cin >> numProductions;

    vector<Production> productions(numProductions);
    
    // Input productions
    cout << "Enter productions in the form A->xyz:\n";
    for (int i = 0; i < numProductions; ++i) {
        string input;
        cin >> input;
        productions[i].lhs = input.substr(0, 1);
        productions[i].rhs = input.substr(3);
    }

    // Input string to parse
    string input;
    cout << "Enter input string: ";
    cin >> input;

    string stack;
    int inputPos = 0;
    stack.push_back(input[inputPos++]);

    cout << "\nStack\tInput\tAction\n";

    while (true) {
        bool reduced = false;

        // Display stack and remaining input
        cout << stack << "\t" << input.substr(inputPos) << "\t";

        // Attempt to reduce the stack by matching with productions
        for (const auto& prod : productions) {
            size_t pos = stack.rfind(prod.rhs);
            if (pos != string::npos && pos == stack.size() - prod.rhs.size()) {
                // Reduction: replace RHS with LHS in the stack
                stack.erase(pos);
                stack += prod.lhs;
                cout << "Reduced by " << prod.lhs << " -> " << prod.rhs << "\n";
                reduced = true;
                break;
            }
        }

        if (!reduced) {
            // If no reduction occurred, shift the next input symbol to the stack
            if (inputPos < input.size()) {
                stack += input[inputPos++];
                cout << "Shifted\n";
            } else {
                break;
            }
        }
    }

    // Final check to see if the stack contains the start symbol only
    if (stack == productions[0].lhs) {
        cout << "\nString Accepted\n";
    } else {
        cout << "\nString Rejected\n";
    }

    return 0;
}


/**
 * E->E+E
E->E*E
E->(E)
E->a
Enter input string: (a+a)*a
 */