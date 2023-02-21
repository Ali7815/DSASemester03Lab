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
	bool insertNode(int index,int x)
	{
		Node* temp=Head;
		Node* n =new Node(x);
		if (index<1){
			cout<<"Invalid Index"<<endl;
		}
		if (index==1){
		n->next=Head;
		Head=n;
	}
		else
		{
			while (index!=0){
				index--;
				if (index==1){
					n->next=Head->next;
					Head->next=n;
					break;
				}
				temp=temp->next;
				if (temp==NULL){
					break;
				}
			}
		}
	}
	bool insertAtHead(int x)
	{
		Node* n =new Node(x);
		n->next=Head;
		Head=n;
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
	bool deleteNode(int x){
		Node* temp= Head;
		Node* prev=NULL;
		while (temp!=NULL && temp->data!=x){
			prev=temp;
			temp=temp->next;			
		
		}	
			if (temp==NULL){
			return 1;
			}
			prev->next=temp->next;
			delete temp;
	}
	bool deleteFromStart(){
		Head=Head->next;
		return 1;
	}
	bool deleteFromEnd(){
		Node* temp=Head;
		Node* prev=NULL;
		while (temp->next!=NULL){
			prev=temp;
			temp=temp->next;
			
		}
		prev->next=NULL;
	}
	
	void displayList()
	{
		
		Node* n=Head;
		while(n!=NULL){
			cout<< n->data <<" ";
			n=n->next;
			
			
		
		}
	}
};
///////////////////////////////////////////Doubly LinkList//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class Node2{
	public :
	int data;
	Node2 *next;
	Node2 *previous;
	public :
		Node2(int value){
		data=value;
		next=NULL;
		previous=NULL;
	}
	
};
class DoublyLinkedList{
	private:
	Node2* Head;
	Node2* Tail;
	public :
		DoublyLinkList(){
			Head=NULL;	
			Tail=NULL;		
		}
	public :
	bool isEmpty(){
		if (Head==NULL){
		cout<<"DoublyLinkList Is Empty"<<endl;
		return 1;
		}
		return 0;
	}
	bool insertAtHead(int x)
	{
		Node2* n =new Node2(x);
		n->next=Head;
		n->previous=n;
		
		Head=n;
	}
	bool insertAtEnd(int x){
		Node2* n =new Node2(x);
//		Tail->next = n;
//        n->previous = Tail;
//        Tail = n;
	}
	bool findNode(int x){
		Node2* temp=Head;
		while (temp!=NULL){
			if (temp->data==x){
				return 1;
			}
			temp=temp->next;
		}
	}
	bool insertNode(int index,int x)
	{
		Node2* temp=Head;
		Node2* n =new Node2(x);
		if (index<1){
			cout<<"Invalid Index"<<endl;
		}
		if (index==1){
		n->next=Head;
		Head=n;
	}
		else
		{
			while (index!=0){
				index--;
				if (index==1){
					n->next=Head->next;
					Head->next=n;
					break;
				}
				temp=temp->next;
				if (temp==NULL){
					break;
				}
			}
		}
	}
	bool deleteFromStart(){
		Head=Head->next;
		return 1;
	}
	void displayList()
	{
		
		Node2* n=Head;
		while(n!=NULL){
			cout<< n->data <<" ";
			n=n->next;			
		
		}
	}
};
		
		

main()
{
//	LinkedList L;
//	L.insertAtHead(5);
//	L.insertAtHead(10);
//	L.insertNode(2,89);
//	L.insertAtEnd(20);
//	L.insertAtEnd(10);
////	L.deleteNode(20);
//	L.insertAtHead(1);
//	L.deleteFromEnd();
//	L.displayList();
//	DoublyLinkedList L;
//	L.isEmpty();
//	L.insertAtHead(10);
//	L.insertAtHead(5);
//	L.insertAtEnd(3);
//	L.displayList();
}
