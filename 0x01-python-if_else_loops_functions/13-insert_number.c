#include "lists.h"
#include <stdio.h>
#include <stdlib.h>


listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *next;
	listint_t *h = *head;
	int current_int;

	if (*head == NULL)
	{
		/*insert into empty list*/
		new->n = number;
		new->next = NULL;
		*head = new;
		return (*head);
	}
	current_int = h->n;
	if (current_int >= number)
	{
		/*insert at start/begining*/
		new->n = number;
		new->next = *head;
		*head = new;
		return (*head);
	}
	next = h->next;
	while(next != NULL)
	{
		current_int = next->n;
		if (current_int >= number)
			break;
		h = next;
		next = h->next;
	}
	if (next == NULL)
	{
		/*insert at end*/
		new->n = number;
		new->next = next;
		h->next = new;
		return (*head);
	}
	new->n = number;
	new->next = h->next;
	h->next = new;
	return (*head);
}
