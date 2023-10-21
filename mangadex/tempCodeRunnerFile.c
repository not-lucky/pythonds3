#include <stdio.h>
#include <stdlib.h>

struct Node {
  int data;
  struct Node* prev;
  struct Node* next;
};

struct Node* createNewNode(int data) {
  struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
  newNode->data = data;
  newNode->prev = NULL;
  newNode->next = NULL;
  return newNode;
}

void insertNode(struct Node** head, int data) {
  struct Node* newNode = createNewNode(data);
  struct Node* current = *head;

  // if the list is empty, make the new node as the head
  if (*head == NULL) {
    *head = newNode;
    return;
  }

  // if the new node's data is smaller than the head node's data,
  // insert the new node before the head node
  if (data < current->data) {
    newNode->next = current;
    current->prev = newNode;
    *head = newNode;
    return;
  }

  // find the correct position to insert the new node
  while (current->next != NULL && current->next->data < data) {
    current = current->next;
  }

  // insert the new node at the correct position
  newNode->prev = current;
  newNode->next = current->next;
  if (current->next != NULL) {
    current->next->prev = newNode;
  }
  current->next = newNode;
}

void displayList(struct Node* head) {
  struct Node* current = head;
  while (current != NULL) {
    printf("%d ", current->data);
    current = current->next;
  }
  printf("\n");
}

int main() {
  struct Node* head = NULL;
  int n;
  int data;
  // insert nodes in ascending order

  printf("Enter size of linked list:\n");
  scanf("%d", &n);

  printf("Enter the data:\n");
  for (int i = 0; i < n; i++) {
    scanf("%d", &data);
    insertNode(&head, data);
  }

  // display the linked list
  printf("Doubly linked list: ");
  displayList(head);

  return 0;
}
