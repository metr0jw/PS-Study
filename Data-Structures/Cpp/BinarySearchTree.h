#pragma once
#include <iostream>
using namespace std;

struct Node
{
	Node* left;
	Node* right;
	int value;
};

class BinarySearchTree
{
private:
	Node* root = nullptr;
	Node* SearchMaxNode(Node* node)
	{
		if (node == nullptr)
			return NULL;

		while (node->right != nullptr)
		{
			node = node->right;
		}
		return node;
	}
	Node* RemoveNodeSequences(Node* node, int argv)
	{
		if (node == nullptr) return node;
		else if (node->value > argv)
			node->left = RemoveNodeSequences(node->left, argv);
		else if (node->value < argv)
			node->right = RemoveNodeSequences(node->right, argv);
		else
		{
			Node* remove = node;

			if (node->right == nullptr && node->left == nullptr)
			{
				delete node;
				node = nullptr;
			}
			else if (node->right == nullptr)
			{
				node = node->left;
				delete remove;
			}
			else if (node->left == nullptr)
			{
				node = node->right;
				delete remove;
			}
			else
			{
				remove = SearchMaxNode(node->left);
				node->value = remove->value;
				node->left = RemoveNodeSequences(node->left, remove->value);
			}
		}
		return node;
	}
public:
	void AddNode(int argv)
	{
		Node* node = new Node();
		Node* temp = nullptr;

		node->value = argv;

		if (root == nullptr)
			root = node;
		else
		{
			Node* cmpNode = root;

			while (cmpNode != nullptr)
			{
				temp = cmpNode;
				if (node->value < cmpNode->value)
					cmpNode = cmpNode->left;
				else
					cmpNode = cmpNode->right;
			}

			if (node->value < temp->value)
				temp->left = node;
			else
				temp->right = node;
		}
	}
	bool Search(int argv)
	{
		Node* temp = root;

		while (temp != nullptr)
		{
			if (temp->value == argv)
			{
				cout << argv << endl;
				return true;
			}
			else if (temp->value > argv)
			{
				cout << temp->value << " ";
				temp = temp->left;
			}
			else
			{
				cout << temp->value << " ";
				temp = temp->right;
			}
		}
		return false;
	}
	void DeleteNode(int argv)
	{
		Node* node = root;
		RemoveNodeSequences(node, argv);
	}
};
