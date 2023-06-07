#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Insert node into sorted list
 *
 * @head: list head
 * @number: new data
 * Return: listint_t*
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *prev = *head;
	listint_t *new_node;
	int found = 0;

	while (current && current->next)
	{
		if (current->n > number)
		{
			new_node = (listint_t *)malloc(sizeof(listint_t));
			if (!new_node)
				return (NULL);
			new_node->n = number;
			new_node->next = NULL;
			prev->next = new_node;
			new_node->next = current;
			found = 1;
			break;
		}
		prev = current;
		current = current->next;
	}
	if (found == 0)
	{
		new_node = (listint_t *)malloc(sizeof(listint_t));
		if (!new_node)
			return (NULL);
		new_node->n = number;
		new_node->next = NULL;
		prev = current;
		prev->next = new_node;
	}
	return (new_node);
}
