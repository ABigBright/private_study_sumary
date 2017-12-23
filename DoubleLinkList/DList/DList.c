// Description : the list datastruct fulfill 
// Author      : brightq
// Date        : 2017.10.11
// Version     : v1.0.0

#include <stdio.h>
#include "DList.h"

// description : init the list
void dListInit(void)
{

}

// description : insert node into list     
int dListInsertNodeIntoHead(dlist_node* dList, dlist_node* node)
{
	if ((NULL == node) || (NULL == dList))
		return false;
	
	node->next = dList;
	if (dList) dList->prev = node;
	dList = node;	

	return true;
}


// Description   : Insert node into list tail
// 
// Specification :  We'll only do one things which is to look up the tail node, 
// 					then make the tail next pointer value change, tail -> next = node
int dListInsertNodeIntoTail(dlist_node* dList, dlist_node* node)
{   
	dlist_node** walk = &dList;
	dlist_node* lastNode = dList;

	if (NULL == node)
		return false;
	
	while (*walk) {
		lastNode = *walk;
		walk = &((*walk)->next);
	}

	*walk = node;
	node->prev = lastNode; 
	
	return true;
}


// description : delete node from list
dlist_node* dListDeleteNode(dlist_node* dList, 
							  dlist_node* node)
{
	dlist_node** walk = &dList;

	if ((NULL == dList) || (NULL == node))
		return NULL;

	/* look up the right node position in dlist */
	while (*walk != node) {
		walk = &(*walk)->next;
	}
	
	*walk = node->next;

 	/* not the dlist tail */
	if (node->next) 						 
		node->next->prev = node->prev;
	
	return node;
}

// description : alloc the node from free list
dlist_node* freeListAllocNode(dlist_node* freeList)
{

}

// description : free the node into free list
dlist_node* freeListFreeNode(dlist_node* freeList, dlist_node* node)
{

}

// description : freelist initializing 
void freeListInit(void)
{

}

