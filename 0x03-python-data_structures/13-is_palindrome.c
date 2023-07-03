#include "lists.h"

int is_palindrome(listint_t **head)
{
	if (!*head)
	return (0);
	listint_t *ptr_slow = *head;
	listint_t *ptr_fast = *head;

	while (ptr_slow && ptr_fast)
	{
		ptr_fast = ptr_fast->next->next;
		ptr_slow = ptr_slow->next;
	}
	ptr_fast = *head;
	while (ptr_fast && ptr_slow)
	{
		if (ptr_fast->n != ptr_slow->n)
		return (1);
		ptr_fast = ptr_fast->next;
		ptr_slow = ptr_slow->next;
	}
	return (0);
}
