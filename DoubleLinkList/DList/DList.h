// Description : the list datastruct fulfill 
// Author      : brightq
// Date        : 2017.10.11
// Version     : v1.0.0

#ifndef DLIST_H
#define DLIST_H

#include <stdio.h>

typedef struct _node_data {
	int val;
} str_node_data;

typedef struct _node {
	struct _node* prev;
	struct _node* next;
	str_node_data nd;
} dlist_node;

#define true 1
#define false 0

void dListInit(void);
int dListInsertNodeIntoHead(dlist_node* dList, dlist_node* node);
int dListInsertNodeIntoTail(dlist_node* dList, dlist_node* node);
dlist_node* dListDeleteNode(dlist_node* dList, dlist_node* node);
dlist_node* freeListAllocNode(dlist_node* freeList);
dlist_node* freeListFreeNode(dlist_node* freeList, dlist_node* node);
void freeListInit(void);

#endif

