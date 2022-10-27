//reverse a linked list using recursion
#include<stdio.h>
#include<stdlib.h>
struct Node{
    int data;
    struct Node* next;
};
struct Node* head; //global variable
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
void Print(struct Node* head)
{
    if(head->next == NULL)
    {
        printf(" %d", head->data);
        printf("\n");
        return;
    }
    printf(" %d", head->data);
    Print(head->next);
}
void ReversePrint(struct Node* head)
{
    if(head->next == NULL)
    {
        printf(" %d", head->data);
        return;
    }
    ReversePrint(head->next); // recursive call
    printf(" %d", head->data);
}
int main()
{
    head = NULL;
    Insert(7 , 1);
    Insert(4 , 2);
    Insert(1 , 3);
    Insert(8 , 4);
    Insert(9, 5);
    
    Print(head);
    ReversePrint(head);

}