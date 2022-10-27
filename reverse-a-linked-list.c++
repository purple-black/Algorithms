//code to reverse a linked list - iterative method
#include<stdio.h>
#include<stdlib.h>
struct Node{
    int data;
    struct Node* next;
};
struct Node* head; // global variable
void Insert(int data, int n)
{
    struct Node* temp1 = new Node();
    temp1->data = data;
    temp1->next = NULL;
    if(n == 1)
    {
        temp1->next = head;
        head = temp1;
        return;
    }
    struct Node* temp2 = head;
    int i;
    for(i = 0; i<n-2; i++)
    {
        temp2 = temp2->next;

    }
    temp1->next =temp2->next;
    temp2->next = temp1;
}
void Print()
{
    struct Node* temp = head;
    while( temp != NULL)
    {
        printf(" %d", temp->data);
        temp = temp->next;
    }
    printf("\n");
}
void Reverse()
{
    struct Node *(current), *prev, *next;
    current = head;
    prev = NULL;
    while(current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    head = prev;
}
int main()
{
    head = NULL;
    Insert(2,1);
    Insert(4,2);
    Insert(6,3);
    Insert(7,4);
    Insert(8,5);
    Print();
    Reverse();
    Print();

}