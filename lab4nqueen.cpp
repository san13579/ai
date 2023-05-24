#include <iostream>
#include <vector>

using namespace std;

// Function to check if placing a queen at a particular position is safe
bool isSafe(vector<vector<int>>& board, int row, int col, int n) {
    // Check if there is a queen in the same column
    for (int i = 0; i < row; ++i) {
        if (board[i][col] == 1) {
            return false;
        }
    }

    // Check if there is a queen in the upper left diagonal
    for (int i = row, j = col; i >= 0 && j >= 0; --i, --j) {
        if (board[i][j] == 1) {
            return false;
        }
    }

    // Check if there is a queen in the upper right diagonal
    for (int i = row, j = col; i >= 0 && j < n; --i, ++j) {
        if (board[i][j] == 1) {
            return false;
        }
    }

    return true;
}

// Function to solve the n-queens problem using Branch and Bound and Backtracking
bool solveNQueens(vector<vector<int>>& board, int row, int n) {
    if (row == n) {
        // All queens have been placed successfully
        return true;
    }

    for (int col = 0; col < n; ++col) {
        if (isSafe(board, row, col, n)) {
            // Place the queen at position (row, col)
            board[row][col] = 1;

            // Recur to place the rest of the queens
            if (solveNQueens(board, row + 1, n)) {
                return true;
            }

            // If placing the queen at (row, col) leads to an invalid solution, backtrack
            board[row][col] = 0;
        }
    }

    // No valid solution found
    return false;
}

// Function to print the board configuration
void printBoard(vector<vector<int>>& board) {
    int n = board.size();
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cout << board[i][j] << " ";
        }
        cout << endl;
    }
}

// Function to solve the n-queens problem and print the board configuration
void solveNQueens(int n) {
    vector<vector<int>> board(n, vector<int>(n, 0));

    if (solveNQueens(board, 0, n)) {
        cout << "Solution exists. Board configuration:\n";
        printBoard(board);
    } else {
        cout << "No solution exists for n = " << n << endl;
    }
}

int main() {
    int n;
    cout << "Enter the value of n for the n-queens problem: ";
    cin >> n;

    solveNQueens(n);

    return 0;
}
