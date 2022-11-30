#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include "lists.h"

/**
 *insert_node -inserts new num to linkedlist 
 * @head: head of the linked list
 * @number: number to insert
 */

listint_t *insert_node(listint_t **head, int number)
{
listint_t *prev, *current;
listint_t *mynode;
unsigned int m = 0;
mynode = malloc(sizeof(listint_t));

if(!mynode)
{
printf("Error\n");
return (NULL);
}
mynode->n = number;
current = *head;
while (current)
{
if(current->n < number)
{
m++;
prev = current;
current = current->next;
}
else
break;
}
if (!m)
{
mynode->next = *head;
*head = mynode;
return (mynode);
}
mynode->next = prev->next;
prev->next = mynode;

return (mynode);
}
