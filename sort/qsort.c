#include <stdio.h>

typedef char t;

void swap(t* a, t* b)
{
	t tmp = 0;

	tmp = *a;
	*a = *b;
	*b = tmp;
}

void arr_show(t* a, int n)
{
	for (int i = 0; i < n; i++) {
		printf("%d ", a[i]);
	}
	printf("\r\n");
}

void my_qsort(t* start, t* end)
{
	t ref = 0;
	t* left = NULL;
	t* right = NULL;

	if ((NULL == start) || (NULL == end)) return;
	if (start >= end) return;

	ref = *start;
	left = start;
	right = end;

	while (left < right) {
		while ((left < right) && (ref <= *right))
			right--;
		if (left < right) {
			swap(left, right);
			left++;
		}
		
		while ((left < right) && (ref > *left))
			left++;
		if (left < right) {
			swap(left, right);
			right--;
		}
	}

	my_qsort(start, left);
	my_qsort(left+1, end);
}

int main(void)
{
	t a[10] = {1, 6, 4, 3, 3, 5, 9, 2, 6, 8};

	arr_show(a, 10);
	my_qsort(a, a+9);
	arr_show(a, 10);
}
