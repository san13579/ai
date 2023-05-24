#include <iostream>
#include <vector>
#include <queue>

using namespace std;

// Function to perform Depth First Search (DFS)
void dfsRecursive(vector<vector<int>>& graph, vector<bool>& visited, int node) {
    visited[node] = true;
    cout << node << " ";

    for (int neighbor : graph[node]) {
        if (!visited[neighbor]) {
            dfsRecursive(graph, visited, neighbor);
        }
    }
}

// Function to perform Breadth First Search (BFS)
void bfs(vector<vector<int>>& graph, int startNode) {
    int numNodes = graph.size();
    vector<bool> visited(numNodes, false);
    queue<int> q;

    visited[startNode] = true;
    q.push(startNode);

    while (!q.empty()) {
        int currentNode = q.front();
        q.pop();
        cout << currentNode << " ";

        for (int neighbor : graph[currentNode]) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                q.push(neighbor);
            }
        }
    }
}

int main() {
    int numNodes = 6;
    vector<vector<int>> graph(numNodes);

    graph[0] = {1, 2, 3};    
    graph[1] = {0, 4};       
    graph[2] = {0, 3, 4};    
    graph[3] = {0, 2};       
    graph[4] = {1, 2, 5};    
    graph[5] = {4};          

    cout << "DFS: ";
    vector<bool> visitedDFS(numNodes, false);
    dfsRecursive(graph, visitedDFS, 0);
    cout << endl;

    cout << "BFS: ";
    bfs(graph, 0);
    cout << endl;

    return 0;
}
