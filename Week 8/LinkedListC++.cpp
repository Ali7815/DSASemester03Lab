#include <iostream>
using namespace std;
class Node
{
	public :
	int data;
	Node *next;
	public :
		Node(int value){
		data=value;
		next=NULL;
	}
};
class LinkedList{
	private:
	Node* Head;
	public :
		linkList(){
			Head=NULL;
		}
	bool isEmpty(){
		if (Head==NULL){
		return 1;
		}
		return 0;
	}
	
	
	
	
	void printList()
	{
		//Node *temp= Head;
		Node* n=Head;
		while(n!=NULL){
			cout<< n->data <<" ";
			n=n->next;
		}
	}
	bool insertAtHead(int x)
	{
		Node* n =new Node(x);
		n->next=Head;
		Head=n;
	}
	bool insertNode(int index,int x)
	{
		Node* n =new Node(x);
		if (index==Head->data)
		{
			n->next=Head->next;
			Head->next=n;
			return 1;
		}
		Node* temp=Head;
		while(temp->data!=index){
			temp=temp->next;
			if (temp==NULL){
				return 1;
			}
		}
		n->next=temp->next;
		temp->next=n;
	}
	bool insertAtEnd(int x){
		Node* n =new Node(x);
		if (Head==NULL)
		{
			Head=n;
			return 1;
		}
		Node* temp=Head;
		while (temp->next!=NULL){
			temp=temp->next;
		}
		temp->next=n;
	}
	bool findNode(int x){
		Node* temp=Head;
		while (temp!=NULL){
			if (temp->data==x){
				return 1;
			}
			temp=temp->next;
		}
	}
	bool Delete(int key){
		
			Node* temp=Head;
			Node* prev=NULL;
			if (temp!=NULL && temp->data==key){
				Head=temp->next;
				delete temp;
				return 1;
			}
			else{
				while(temp!=NULL && temp->data!=key){
					prev=temp;
					temp=temp->next;
					
				}
				if (temp==NULL){
						return 1;
					}
				prev->next=temp->next;
				delete temp;
			}
		
	}
		
		
};
main()
{
	LinkedList L;
	L.insertAtHead(5);
	L.insertAtHead(10);
	L.insertNode(2,89);
	L.insertAtEnd(20);
	L.insertAtHead(1);
	L.printList();
}
