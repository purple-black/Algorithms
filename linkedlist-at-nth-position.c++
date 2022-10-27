//C++ CODE
//This code is written in C++. u will see struct here np problem, because c syntax will work for c++ BUT NOT VISE VERSA!!!!!!!!!!!1
// this is c++ code as operator NEW is used here( which is used for creating (memory for)/a new node in heap )
// and that is why file is saved as <filename>.c++
#include<stdio.h>
#include<stdlib.h>
struct Node{
    int data;
    struct Node* next;
};
struct Node* head;
void Print()
{
    struct Node* temp = head;
    while(temp != NULL)
    {
        printf("%d\n", temp->data);
        temp = temp->next;
    }
    printf("\n");
}
void Insert(int data, int n) //now in stack main will pause and insert will start. and space for data and n willbe allocated  
{
    struct Node* temp1 = new Node(); //now in stack a space for temp1 will be allocated and space for a new node will be allocated in heap also.
    temp1->data = data; // now the data for the list is entered.
    temp1->next = NULL; // first list was empty and now the first number is being added. so the first digit doesnot point to any other node now. now there is only one number in the list. 
    if (n == 1) // running the loop now. if n ==1 means if we want to insert at position 1, then this loop will be implemented . otherwise if n !== 1 then not implemeted and moves to the next line.
    {
        temp1->next = head; // head is null but temp1->next is already null. so this will work for emprt case ok!!!
        head = temp1; // now we are saying head = temp1 . so now head will point to temp1. that is it will store the address of this newly created node.
        return; // now the controls returns to the main methos and so the insert func. we did now will be erased.
    }
    struct Node* temp2 = head; // the above written loop i.e., from if onwards will not work, because n is not equal to 1 now as we inserting at 2 now. so a temp2 which is pointer to head is created now
    // now another new node is created and now temp1 will store the address of this new node.((refer to line 20)... because n is not equal to 1, will move on to create another temporary variable temp2.
    //temp2 is initailly equal to HEAD NODE ......(it is not head fool, it is HEAD NODE)
    for(int i = 0; i < n-2; i++) // IN THIS CASE this loop won't run as we want to insert in the second position so n-1 th node is first node itself. so control move to execute next lines.
    {
        temp2 = temp2->next;
    }
    temp1->next = temp2->next; // temp1->next is same as temp2->next but in this case it is 0 only.
    temp2->next = temp1; //now temp2->next is resetted as temp1. temp1 stores the address of the newly created node. so now thisnode is linked to the previously created node.

}
int main(){
    head = NULL; // INITIALLY THE LIST IS EMPTY
    Insert(2, 1); // list : 2
    Insert(3, 2); //list now is 2, 3 // now the controls goes to insert func. and main will pause.
    Insert(4, 1); // now list should be 4,2,3
    Insert(5, 2); // now list is 4, 5, 2, 3
    Print();

}
