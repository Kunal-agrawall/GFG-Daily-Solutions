//{ Driver Code Starts
#include <stdint.h>

#include <bits/stdc++.h>
using namespace std;

struct Node {
    int data;
    struct Node *npx;

    Node(int x) {
        data = x;
        npx = NULL;
    }
};

struct Node *XOR(struct Node *a, struct Node *b) {
    return (struct Node *)((uintptr_t)(a) ^ (uintptr_t)(b));
}

struct Node *insert(struct Node *head, int data);

vector<int> getList(struct Node *head);

int main() {
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        struct Node *head = NULL;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;

        while (ss >> number) {
            head = insert(head, number);
        }

        vector<int> vec = getList(head);
        for (int x : vec)
            cout << x << " ";
        cout << endl;
        for (int i = vec.size() - 1; i >= 0; i--) {
            cout << vec[i] << " ";
        }
        cout << "\n";
    }
    return (0);
}

// } Driver Code Ends


/*
Structure of linked list is as
struct Node
{
    int data;
    struct Node* npx;

    Node(int x){
        data = x;
        npx = NULL;
    }
};

Utility function to get XOR of two Struct Node pointer
use this function to get XOR of two pointers
struct Node* XOR (struct Node *a, struct Node *b)
{
    return (struct Node*) ((uintptr_t) (a) ^ (uintptr_t) (b));
}
*/

// function should insert the data to the front of the list
struct Node *insert(struct Node *head, int data) {
    // create a new node with the given data
    struct Node *new_node = new Node(data);

    // make the new node's npx point to the current head
    new_node->npx = head;

    // if the current head is not NULL, update the npx of the head
    if (head != NULL)
        head->npx = XOR(new_node, head->npx);

    // return the new node as the new head
    return new_node;
}

// function to print the linked list
vector<int> getList(struct Node *head) {
    // initialize three pointers: current, previous, and next
    struct Node *curr = head;
    struct Node *prev = NULL;
    struct Node *next;

    // create a vector to store the values of the nodes in the list
    vector<int> vec;

    // iterate through the linked list
    while (curr != NULL) {
        // add the data of the current node to the vector
        vec.push_back(curr->data);

        // calculate the next node using XOR operation
        next = XOR(prev, curr->npx);

        // update the previous and current nodes
        prev = curr;
        curr = next;
    }

    // return the vector containing the values of the nodes in the list
    return vec;
}