#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_listsint - Reverses a singly linked list
 * @head: Double pointer to the head of the list
 * Return: Pointer to the first node of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
	return (*head);
}

/**
 * compare_lists - Compares two singly linked lists
 * @head1: Pointer to the head of the first list
 * @head2: Pointer to the head of the second list
 * Return: 1 if lists are identical, 0 otherwise
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
	listint_t *temp1 = head1;
	listint_t *temp2 = head2;

	while (temp1 && temp2)
	{
		if (temp1->n == temp2->n)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
			return (0);
	}

	if (temp1 == NULL && temp2 == NULL)
		return (1);

	return (0);
}

/**
 * is_palindrome - Checks if a singly liked list is a palindrome
 * @head: Double pointer to the head of the list
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	if (!head || !*head)
		return (1);

	listint_t *slow = *head, *fast = *head, *second_half, *prev_slow = *head;
	listint_t *midnode = NULL;
	int res = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}

		if (fast != NULL)
		{
			midnode = slow;
			slow = slow->next;
		}

		second_half = slow;
		prev_slow->next = NULL;
		reverse_listint(&second_half);
		res = compare_lists(*head, second_half);

		reverse_listint(&second_half);
		if (midnode != NULL)
		{
			prev_slow->next = midnode;
			midnode->next = second_half;
		}
		else
			prev_slow->next = second_half;
	}
	return (res);
}
