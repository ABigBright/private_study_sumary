#include <stdio.h>
#include "dlist.h"

int main(void)
{
	dlist_node* alloc_node = NULL;
	int nn                 = 10;

	printf("Enter main.\r\n");

	dlist_init();

	alloc_node = node_array;

	printf("Freelist:%d\r\n", freelist);
	
	printf("\r\n");
	printf("\r\n");

	printf("Print List:\r\n");
	printf("===========\r\n");

	while (nn--) {
		printf("\r\n");
		printf("Offset: %d\r\n", alloc_node);
		printf("Next  : %d\r\n", alloc_node->next);
		printf("\r\n");
		alloc_node++;
	}
	
	nn = 10;
	
	while (nn--) {
		if (!freelist_alloc_node(&freelist, &alloc_node)) {
			printf("Alloc fail.\r\n");
			return -1;
		}
		alloc_node->nd.val = nn;
		dlist_insert_node_into_tail(&dlist, alloc_node);
	}

	alloc_node = dlist;

	while (alloc_node) {
		printf("%d ", alloc_node->nd.val);
		alloc_node = alloc_node->next;
	}

	printf("\r\n");

	return -1;
}
