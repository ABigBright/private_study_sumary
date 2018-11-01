/*
****************************************************************
* Description     :		the list datastruct fulfill 
* Author          :		brightq
* Date            :		2017.10.11
* Version         :		v1.0.0
****************************************************************
*/
#ifndef DLIST_H
#define DLIST_H

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
#define NODE_NUM 10

#ifdef DLIST_LOCAL
	#define DLIST_EXT
	
	dlist_node  node_array[NODE_NUM];
	dlist_node* freelist = NULL;
	dlist_node* dlist = NULL;

#else
	#define DLIST_EXT extern

	extern dlist_node  node_array[NODE_NUM];
	extern dlist_node* freelist;
	extern dlist_node* dlist;

#endif

#endif
/*
****************************************************************
* description     :     init the list
****************************************************************
*/
void dlist_init(void);
/*
****************************************************************
* description     :		insert node into list     
****************************************************************
*/
char dlist_insert_node_into_head(dlist_node** dlist_head, 
								 dlist_node* insert_node);
/*
****************************************************************
* description     :		insert node into list     
****************************************************************
*/
char dlist_insert_node_into_tail(dlist_node** dlist_head, 
					   			 dlist_node* insert_node);
/*
****************************************************************
* description     :		delete node from list
****************************************************************
*/
dlist_node* dlist_delete_node(dlist_node** dlist_head, 
							  dlist_node* node);
/*
****************************************************************
* description     :		alloc the node from free list
****************************************************************
*/
char freelist_alloc_node(dlist_node** fresslist, dlist_node** node);
/*
****************************************************************
* description     :		free the node into free list
****************************************************************
*/
dlist_node* freelist_free_node(dlist_node** freelist, dlist_node* node);
/*
****************************************************************
* description     :		freelist initializing 
****************************************************************
*/
void freelist_init(dlist_node** freelist, 
				   void* node_buf, 
				   unsigned int node_num, 
				   unsigned int node_len);

