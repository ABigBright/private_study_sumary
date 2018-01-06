#ifndef QUEUE_H
#define QUEUE_H

// q_curr_n : queue's currunt item number
// q_max_n  : queue max item number
// q_wr_p   : queue write pointer
// q_rd_p   : queue read pointer
typedef struct _QUE_T {
	int q_curr_n;
	int q_max_n;
	char* q_wr_p;
	char* q_rd_p;
	char* q_h;
	char* q_t;
} que_t

void que_init(que_t* qcb, char* que, int len);
char que_wr_byte(que_t* qcb, char data);
char que_rd_byte(que_t* qcb, char* data);

#endif

