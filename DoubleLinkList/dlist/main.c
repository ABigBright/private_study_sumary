#include <stdio.h>
#include "dlist.h"

int main(void)
{
	dlist_node* alloc_node = NULL;
	int nn                 = 10;

	printf("Enter main.\r\n");

	dlist_init();

	alloc_node = node_array;

	printf("Freelist:%d\r\n", (int)freelist);
	
	printf("\r\n");
	printf("\r\n");

	printf("Print FreeList:\r\n");
	printf("===============\r\n");

	while (nn--) {
		printf("\r\n");
		printf("Offset: %d\r\n", (int)alloc_node);
		printf("Next  : %d\r\n", (int)alloc_node->next);
		printf("\r\n");
		alloc_node = alloc_node->next;
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

	nn = 10;
	alloc_node = dlist;
	printf("\r\n");
	printf("Print User's List:\r\n");
	printf("==================\r\n");
	while (nn--) {
		printf("\r\n");
		printf("Offset: %d\r\n", (int)alloc_node);
		printf("Next  : %d\r\n", (int)alloc_node->next);
		printf("Prev  : %d\r\n", (int)alloc_node->prev);
		printf("\r\n");
		alloc_node = alloc_node->next;
	}

	
	printf("Print User's List:\r\n");
	printf("==================\r\n");
	dlist_delete_node(&dlist, dlist); 
	alloc_node = dlist;
	printf("\r\n");
	while (alloc_node) {
		printf("Offset : %d\r\n", (int)alloc_node);
		printf("Prev   : %d\r\n", (int)alloc_node->prev);
		printf("Next   : %d\r\n", (int)alloc_node->next);
		printf("\r\n");
		alloc_node = alloc_node->next;
	}
	printf("\r\n");

	return -1;
}
