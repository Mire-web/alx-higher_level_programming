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

	if (check_list(head) == -1)
	{
		new_node = create_node(new_node, number);
		*head = new_node;
	}
	else
	{
		while (current && current->next)
		{
			if (current->n > number)
			{
				new_node = create_node(new_node, number);
				if (!new_node)
					return (NULL);
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
			new_node = create_node(new_node, number);
			if (!new_node)
				return (NULL);
			prev = current;
			prev->next = new_node;
		}
	}
	return (new_node);
}

/**
 * check_list - check if list is empty
 *
 * @head: head node
 * Return: int
 */

int check_list(listint_t **head)
{
	if (!*head)
		return (-1);
	else
		return (0);
}

/**
 * create_node - Create a node object
 *
 * @node: new node
 * @number: new data
 * Return: listint_t*
 */

listint_t *create_node(listint_t *node, int number)
{
	node = (listint_t *) malloc(sizeof(listint_t));
	if (!node)
	return (NULL);
	node->n = number;
	node->next = NULL;
	return (node);
}
