#include <iostream>
#include <cstdlib>
using namespace std;

//using rand();
class Node
{
	public:
		int data;
		Node *parent;
		Node *left;
		Node *right;
	public :
		Node(int value){
		data=value;
		parent=NULL;
		left=NULL;
		right=NULL;	
	}
	
};
class BST{
	private:
		Node* root;
	public:
		BST()
		{
			root=NULL;
		}
		~BST()
		{
			
		}
		BST(int arr[],int size)
		{
			int x=rand();
			int y=x%size;
			root->data=arr[0];
			for (int i=1;i<size;i++){
				insertNode(arr[i]);
			}
		}
		bool isEmpty(){
			if (root==NULL){
				cout<<"Empty"<<endl;
				return 1;
			}
			return 0;
		}
		Node* getTree(){
			return root;
		}
		Node* insertNode(x){
			if (root==NULL){
				return newNode
			}
			
		}
		public:
		void inOrderTraversel(Node* T)
		{
			if (T!=NULL){
				inOrderTraversel(T->left);
				cout<< T->data<<"  ";
				inOrderTraversel(T->right);
			}
		}
		void preOrderTraversel(Node* T)
		{
			if (T!=NULL){
				cout<< T->data<<"  ";
				preOrderTraversel(T->left);				
				preOrderTraversel(T->right);
			}
		}
		void postOrderTraversel(Node* T)
		{
			if (T!=NULL){			
				postOrderTraversel(T->left);
				postOrderTraversel(T->right);
				cout<< T->data<<"  ";
			}
		}
		Node* findNode(int x){
			
		}
		bool deleteNode(int x)
		{
			
		}
		int NumberOfNodes(Node* T)
		{
			
		}
		int Height(Node* T){
			
		}
		bool isBST(Node * T)
		{
			
		}
		void LeafNodes(Node* T)
		{
			
		}
		bool isSparseTree(Node *T)
		{
			
		}
		void visualizeTree(Node * T)
		{
			
		}
};
main(){
	BST S;
	S.isEmpty();
	int AC[10]={3,4,5,8,32,64,74,86,90,95};
	BST(AC,10);
//	S.postOrderTraversel(S.root);
}
