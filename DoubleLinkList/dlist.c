/*
****************************************************************
* Description     :		the list datastruct fulfill 
* Author          :		brightq
* Date            :		2017.10.11
* Version         :		v1.0.0
****************************************************************
*/
#define DLIST_LOCAL
#include <stdio.h>
#include <string.h>
#include "dlist.h"

/*
****************************************************************
* description     :     init the list
****************************************************************
*/
void dlist_init(void)
{
	freelist = NULL;
	dlist    = NULL;

	freelist_init(&freelist, 
				  node_array, 
			      NODE_NUM, 
				  sizeof(dlist_node));
}

/*
****************************************************************
* description     :		insert node into list     
****************************************************************
*/
char dlist_insert_node_into_head(dlist_node** dlist_head, 
								 dlist_node* insert_node)
{
	if ((NULL == insert_node) || (NULL == dlist_head))
		return false;

	/* 链表不是空链表 */
	if (NULL != *dlist_head)
		(*dlist_head)->prev = insert_node;
	
	insert_node->next = *dlist_head;
	*dlist_head       = insert_node;
	
	return true;
}

/*
****************************************************************
* description     :		insert node into list     
****************************************************************
*/
char dlist_insert_node_into_tail(dlist_node** dlist_head, 
					   			 dlist_node* insert_node)
{   
	dlist_node* dlist_tail = NULL;
	dlist_node* tmp_node   = *dlist_head;

	if ((NULL == insert_node) || (NULL == dlist_head))
		return false;

	while (NULL != tmp_node) {
		dlist_tail = tmp_node;
		tmp_node   = tmp_node->next;
	}

	tmp_node          = insert_node;
	insert_node->prev = dlist_tail;
	
	if (!*dlist_head)
		*dlist_head = tmp_node;

	return true;
}

/*
****************************************************************
* description     :		delete node from list
****************************************************************
*/
dlist_node* dlist_delete_node(dlist_node** dlist_head, 
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

	if (node->next) 						// not the dlist tail 
		node->next->prev = (*walk)->prev;
	
	return node;
}

/*
****************************************************************
* description     :		alloc the node from free list
****************************************************************
*/
char freelist_alloc_node(dlist_node** freelist, dlist_node** node)
{
	if ((NULL == freelist) || (NULL == node) || (NULL == *freelist))
		return false;

	*node     = *freelist;
	*freelist = (*freelist)->next;
	
	return true;
}

/*
****************************************************************
* description     :		free the node into free list
****************************************************************
*/
dlist_node* freelist_free_node(dlist_node** freelist, dlist_node* node)
{
	if ((NULL == freelist) || (NULL == node))
		return NULL;

	node->next = *freelist;
	*freelist  = node;

	return node;
}

/*
****************************************************************
* description     :		freelist initializing 
****************************************************************
*/
void freelist_init(dlist_node** freelist, 
				   void* node_buf, 
				   unsigned int node_num, 
				   unsigned int node_len)
{
	dlist_node* walk = NULL;

	if ((NULL == freelist) || 
		(NULL == node_buf) || 
		(0    == node_num))
		return;

	memset(node_buf, 0x00, node_num * node_len);

	walk = *freelist = (dlist_node*)node_buf;

	while (--node_num) {
		walk->next = (dlist_node*)((char*)walk + node_len); 
		walk       = walk->next;
	}
}

