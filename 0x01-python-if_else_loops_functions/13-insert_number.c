#include "lists.h"
#include <stdio.h>
#include <stdlib.h>


listint_t *insert_node(listint_t **head, int number)
{
	listint_t *h = *head;
	listint_t *hp;
	int b;
	listint_t *new = malloc(sizeof(listint_t));
	if (h == NULL)
		return (NULL);
	while (h)
	{
		b = h->n;
		if (b <= number)
		{
			hp = h;
			h = h->next;
		}
		else
		{
			break;	
		}
	}
	if (h == NULL)
		return (NULL);

	new->n = number;
	new->next = h;
	hp->next = new;

	return new;
}
