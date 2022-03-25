#pragma once
#include <iostream>

using namespace std;

class DoublyLinkedList;

class Node
{
    friend class DoublyLinkedList;
private:
    int value;
    Node* next;
    Node* prev;
public:
    Node(int _value, Node* _next, Node* _prev)
    {
        next = _next;
        prev = _prev;
        value = _value;
    }
};

class DoublyLinkedList
{
private:
    Node* head;
    Node* tail;
    int size;
public:
    DoublyLinkedList(int _value)
    {
        tail = head = new Node(_value);
        size = 1;
    }
    ~DoublyLinkedList()
    {
        Node* cur = head;
        while (cur != nullptr)
        {
            DeleteHead();
        }
    }
    void InsertTail(int _value)
    {
        Node* newNode = new Node(_value);
        if (tail == nullptr) {
            head = tail;
        } else {
            newNode->prev = tail;
            tail->next = newNode;
        } tail = newNode;
        size++;
    }
    void Insert(int data)
    {
        Node* cur = head;
        int idx = 0;
        while (cur != nullptr) {
            if (_value == cur->value)
                return;
            else if (_value > cur->value)
                 idx++;
            cur = cur->next;
        }
        if (idx == 0) {
            Node* newNode = new Node(_value);
            if (head == nullptr) {
                tail = head;
            } else { 
                newNode->next = head;
                head->prev = newNode;
            } head = newNode;
        } else if (idx == size) {
            Node* newNode = new Node(_value);
            if (tail == nullptr) {
                head = tail;
            } else {
                newNode->prev = tail;
                tail->next = newNode;
            } tail = newNode;
        } else {
            Node* newNode = new Node(_value);
            Node* cur = head;
            int i = 0;
            while (i < idx - 1) {
                cur = cur->next;
                i++;
            }
            newNode->prev = cur;
            newNode->next = cur->next;
            cur->next = newNode;
            cur->prev = newNode->prev;
        }
        size++;
    }
    void DeleteHead()
    {
        if (head != nullptr) {
            Node* remove = head;
            head = head->next;
            head->prev = nullptr;
            delete remove;
            size--;
        }
    }
    void Delete(int _value)
    {
        if (size == 0) {
            return;
        } else if (head->value == _value) {
            Node* cur = head;
            head = head->next;
            delete cur;
            size--;
        }
        else {
            Node* prev = head;
            Node* cur = head->next;
            while (cur != nullptr)
            {
                if (cur->value == _value)
                    break;
                else {
                    prev = cur;
                    cur = cur->next;
                }
            }
            if (cur == nullptr)
                return;
            else {
                prev->next = cur->next;
                delete cur;
                size--;
            }
        }
    }
};
