/*
****************************************************************
* Description     :		the list datastruct fulfill 
* Author          :		brightq
* Date            :		2017.10.11
* Version         :		v1.0.0
****************************************************************
*/
#include <stdio.h>
#include "list.h"

/*
****************************************************************
* description     :     init the list
****************************************************************
*/
void dlistInit(void)
{

}

/*
****************************************************************
* description     :		insert node into list     
****************************************************************
*/
bool dlistInsertNodeIntoHead(dlist_node** dlist_head, 
								 dlist_node* insert_node)
{
	if ((NULL == insert_node) || (NULL == dlist_head))
		return false;

	/* 链表不是空链表 */
	if (NULL != *dlist_head)
		*dlist_head->prev = insert_node;
	
	insert_node->next = *dlist_head;
	*dlist_head = insert_node;
	
	return true;
}

/*
****************************************************************
* description     :		insert node into list     
****************************************************************
*/
bool dlistInsertNodeIntoTail(dlist_node** dlist_head, 
					   			 dlist_node* insert_node)
{   
	dlist_node* dlist_tail = NULL;

	if ((NULL == insert_node) || (NULL == dlist_head))
		return false;

	while (NULL != *dlist_head) {
		dlist_tail = *dlist_head;
		dlist_head = &(*dlist_head)->next;
	}

	*dlist_head = insert_node;
	insert_node->prev = dlist_tail;

	return true;
}

/*
****************************************************************
* description     :		delete node from list
****************************************************************
*/
dlist_node* dlistDeleteNode(dlist_node** dlist_head, 
							  dlist_node* node)
{
	dlist_node** walk = dlist_head;

	if ((NULL == dlist_head) || (NULL == node))
		return NULL;

	/* look up the right node position in dlist */
	while (*walk != node) {
		walk = &(*walk)->next;
	}
	
	*walk = node->next;

 	/* not the dlist tail */
	if (node->next) 						 
		node->next->prev = *walk->prev;
	
	return node;
}

/*
****************************************************************
* description     :		alloc the node from free list
****************************************************************
*/
bool freelistAllocNode(dlist_node* node)
{

}

/*
****************************************************************
* description     :		free the node into free list
****************************************************************
*/
dlist_node* freelistFreeNode(dlist_node* node)
{

}

/*
****************************************************************
* description     :		freelist initializing 
****************************************************************
*/
void freelistInit(void)
{

}

