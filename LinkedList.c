#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define TRUE 1
#define FALSE 0

struct Node* new_Node(int);
void insert_begin(int);
void insert_last(int);
void insert_position(int, int);
void delete_first();
void delete_last();
void delete_position();
void print();
int size();

struct Node
{
	int data;
	struct Node* next;
} *head;

int main()
{
	int n, choice, condition = TRUE, value, position;
	while(condition)
	{
		printf("Enter 1. To insert a node at beginning\n2. To insert a node at the end\n3. To insert a node at particular position\n4. To delete first node\n5. To delete the last node\n6.To delete a particular node\n7. To print the list.\n8. To exit\n");
		scanf("%d", &choice);
		switch(choice)
		{
			case 1:
				printf("Enter the node you want to insert\n");
				scanf("%d", &value);
				insert_begin(value);
				break;
			case 2:
				printf("Enter the node you want to insert\n");
				scanf("%d", &value);
				insert_last(value);
				break;
			case 3:
				printf("Enter the node you want to insert\n");
				scanf("%d", &value);
				printf("Enter the position between %d and %d\n", 1, size());
				scanf("%d", &position);
				insert_position(value, position);
				break;
			case 4:
				delete_first();
				break;
			case 5:
				delete_last();
				break;
			case 6:
				printf("Enter a valid position between %d and %d\n", 1, size());
				scanf("%d", &position);
				delete_position(position);
				break;
			case 7:
				print();
				break;
			case 8:
				condition = FALSE;
				break;
			default:
				printf("You made a wrong choice\n");
				break;
		}
	}	
	return 0;
}
struct Node* new_Node(int value)
{
	struct Node* new = (struct Node*)malloc(sizeof(struct Node));
	new -> data = value;
	new -> next = NULL;
	return  new;
}
void insert_begin(int value)
{
	if(head == NULL)
	{
		head = new_Node(value);
		return;
	}
	else
	{
		struct Node* temp = (struct Node*)malloc(sizeof(struct Node));
		temp -> data = value;
		temp -> next = head;
		head = temp;
	}
}
void insert_last(int value)
{
	if(head == NULL)
		head = new_Node(value);
	else
	{
		struct Node* new = (struct Node*)malloc(sizeof(struct Node));
		new -> data = value;
		new -> next = NULL;
		struct Node* temp = (struct Node*)malloc(sizeof(struct Node));
		temp = head;
		struct Node* pre = (struct Node*)malloc(sizeof(struct Node));
		while(temp != NULL)
		{
			pre = temp;
			temp = temp->next;
		}
		pre -> next = new;
	}
}
void insert_position(int value, int position)
{
	if(position > size())
		printf("Position Error\n");
	else
	{
		struct Node* new = (struct Node*)malloc(sizeof(struct Node));
		new -> data = value;
		struct Node* temp = (struct Node*)malloc(sizeof(struct Node));
		temp = head;
		struct Node* pre = temp;
		for(int i = 1; i < position; i++)
		{
			pre = temp;
			temp = temp -> next;
		}
		new -> next = temp;
		pre -> next = new;
	}
}
void delete_first()
{
	if(head == NULL)
	{
		printf("The list is empty\n");
		return;
	}
	else
	{
		struct Node* temp = (struct Node*)malloc(sizeof(struct Node));
		temp = head;
		head = temp -> next;
		free(temp);
	}
}
void delete_last()
{
	if(head == NULL)
	{
		printf("The list is empty\n");
		return;
	}
	else
	{
		struct Node* temp = (struct Node*)malloc(sizeof(struct Node));
		temp = head;
		struct Node* pre = (struct Node*)malloc(sizeof(struct Node));
		for(int i = 1; i < size(); i++)
		{
			pre = temp;
			temp = temp -> next;
		}
		free(temp);
		pre -> next = NULL;
	}
}
void delete_position(int position)
{
	if(head == NULL)
	{
		printf("The list is empty\n");
		return;
	}
	if(position == 1)
		delete_first();
	else if(position == size())
		delete_last();
	else
	{
		struct Node* temp = (struct Node*)malloc(sizeof(struct Node));
		struct Node* pre = (struct Node*)malloc(sizeof(struct Node));
		temp = head;
		for(int i = 1; i < position; i++)
		{
			pre = temp;
			temp = temp -> next;
		}
		pre -> next = temp -> next;
		free(temp);
	}
}
void print()
{
	if(head == NULL)
	{
		printf("List is empty\n");
		return;
	}
	else
	{
		struct Node* temp = (struct Node*)malloc(sizeof(struct Node));
		temp = head;
		while(temp)
		{
			printf("%d ", temp -> data);
			temp = temp -> next;
		}
		printf("\n");
	}
}
int size()
{
	struct Node* temp = (struct Node*)malloc(sizeof(struct Node));
	int ctr = 0;
	temp = head;
	while(temp)
	{
		temp = temp -> next;
		ctr++;
	}
	return ctr;
}
