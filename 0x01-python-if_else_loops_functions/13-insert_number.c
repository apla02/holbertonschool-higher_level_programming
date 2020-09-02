#include "lists.h"
/**
 * insert_node - insert a number in a linked list
 * @head: pointer to structure
 * @number: number to be inserted
 * Return: no zero
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL, *ptr = NULL, *tmp = NULL;

	if (*head == NULL)
		return (NULL);
	new = (listint_t *)malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	ptr = *head;
	if (number == 0)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (ptr && ptr->n < number)
	{
		tmp = ptr;
		ptr = ptr->next;
	}
	if (ptr == NULL)
		return (NULL);
	new->n = number;
	new->next = ptr;
	tmp->next = new;
	return (new);
}
