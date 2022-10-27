// add a node at the beginning of a linked list
#include<stdio.h>
#include<stdlib.h>
struct Node{
    int data;
    struct Node* next;
};
struct Node* head;
void insert(int x)
{
    struct Node* temp = (struct Node*)malloc(sizeof(struct Node));
    temp->data = x;
    temp->next = NULL;
    if(head != NULL)
    {
        temp->next = head;
    }
    head = temp;
}
void print()
{
    struct Node* temp = head;
    printf("List is ");
    while(temp != NULL)
    {
        printf("%d ",temp->data);
        temp = temp->next;
    }
    printf("\n");
}
int main()
{
    head = NULL;
    printf("How many numbers?\n");
    int n, i, x;
    scanf("%d", &n);
    printf("\n");
    for(i = 0; i < n; i++)
    {
        printf("Enter the number\n");
        scanf("%d",&x);
        printf("\n");
        insert(x);
        print();
    }

}
