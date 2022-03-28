
#pragma once
#include <iostream>

using namespace std;
using constexpr int SIZE=100; 
 
class Queue
{
    int *arr;
    int capacity;
    int front;
    int rear;
    int count;
 
public:
Queue(int size)
{
    arr = new int[size];
    capacity = size;
    front = 0;
    rear = -1;
    count = 0;
}
 
~Queue() {
    delete[] arr;
}
 
int Dequeue()
{
    if (isEmpty())
        exit(EXIT_FAILURE);
 
    int temp = arr[front];
 
    front = (front + 1) % capacity;
    count--;
 
    return temp;
}
 
void Enqueue(int value)
{
    if (IsFull())
        exit(EXIT_FAILURE);
  
    rear = (rear + 1) % capacity;
    arr[rear] = item;
    count++;
}
 
int Peek()
{
    if (IsEmpty())
        exit(EXIT_FAILURE);
    return arr[front];
}
 
int Size() {
    return count;
}
 
bool IsEmpty() {
    return (size() == 0);
}
 
bool IsFull() {
    return (size() == capacity);
}
};
 