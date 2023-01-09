#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

void reverse_array(int ori[], int rev[], int len)
{
	int i;
	int j = 0;

	for (i = len - 1; i >= 0; i--)
	{
		rev[j] = ori[i];
		j++;
	}

}
int is_palindrome(listint_t **head)
{
	int store[1024];
	int rep[1024];
	listint_t *h;
	int i = 0;
	int is_pal = 1;

	h = *head;
	while (h != NULL)
	{
		store[i] = h->n;
		h = h->next;
		i++;
	}

	reverse_array(store, rep, i);

	for (i = i - 1; i >= 0; i--)
	{
		if (store[i] != rep[i])
			is_pal = 0;
		printf("ori: %d; dup: %d\n", store[i], rep[i]);
	}


	return (is_pal);
}
