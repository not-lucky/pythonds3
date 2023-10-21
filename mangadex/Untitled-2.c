#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE 100

// Function to check if a character is an operator
int is_operator(char ch) {
  return ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == '^' ||
         ch == '%';
}

// Function to determine the precedence of an operator
int precedence(char ch) {
  switch (ch) {
    case '^':
      return 3;
    case '*':
    case '/':
    case '%':
      return 2;
    case '+':
    case '-':
      return 1;
    default:
      return 0;
  }
}

// Function to push a character onto the stack
void push(char stack[], int* top, char ch) {
  if (*top >= MAX_SIZE - 1) {
    printf("Stack overflow\n");
    exit(1);
  }
  stack[++(*top)] = ch;
}

// Function to pop a character from the stack
char pop(char stack[], int* top) {
  if (*top < 0) {
    printf("Stack underflow\n");
    exit(1);
  }
  return stack[(*top)--];
}

// Function to peek at the top character of the stack
char peek(char stack[], int top) { return stack[top]; }

void postfix(char infix[], int n) {
  char postfix[MAX_SIZE], stack[MAX_SIZE];
  int i, j, top = -1;

  // Convert infix expression to postfix expression
  for (i = 0, j = 0; i < n - 1; i++) {
    if (isalnum(infix[i])) {
      postfix[j++] = infix[i];
    } else if (infix[i] == '(') {
      push(stack, &top, infix[i]);
    } else if (infix[i] == ')') {
      while (peek(stack, top) != '(') {
        postfix[j++] = pop(stack, &top);
      }
      pop(stack, &top);  // Remove '(' from stack
    } else if (is_operator(infix[i])) {
      while (top != -1 &&
             precedence(peek(stack, top)) >= precedence(infix[i])) {
        postfix[j++] = pop(stack, &top);
      }
      push(stack, &top, infix[i]);
    }
  }

  // Pop any remaining operators from stack
  while (top != -1) {
    postfix[j++] = pop(stack, &top);
  }

  // Add null-terminator to postfix string
  postfix[j] = '\0';

  // Print postfix expression
  printf("Postfix expression: %s\n", postfix);
}

// Main function
int main() {
  char infix[MAX_SIZE];
  // Read input infix expression
  printf("Enter infix expression: ");
  fgets(infix, MAX_SIZE, stdin);
  
  postfix(infix, strlen(infix));
  return 0;
}
