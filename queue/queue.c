#include "queue.h"

// que : queue pointer
// len : queue total size(B)
void que_init(que_t* qcb, char* que, int len)
{
	if ((NULL == qcb) || 
		(NULL == que) || 
		(0 == len))
		return;

	qcb->q_curr_n = 0;
	qcb->q_max_n  = len;
	qcb->q_wr_p   = que;
	qcb->q_rd_p   = que;

	qcb->q_h = que;
	qcb->q_t = que + len;
}

// return value : 
// 		0, success
//		1, queue full
//		2, qcb is NULL
char que_wr_byte(que_t* qcb, char data)
{
	if (NULL == qcb) 
		return 2;

	if (qcb->q_curr_n >= qcb->q_max_n)
		return 1;

	if (qcb->q_wr_p >= qcb->q_t)
		qcb->q_wr_p = qcb->q_h;

	*qcb->q_wr_p++ = data;
	qcb->q_curr_n++;

	return 0;
}

// return value : 
// 		0, success
//		1, queue empty
//		2, qcb is NULL
char que_rd_byte(que_t* qcb, char* data)
{
	if (NULL == qcb)
		return 2;

	if (qcb->q_curr_n <= 0)
		return 1;

	if (qcb->q_rd_p >= qcb->q_t)
		qcb->q_rd_p = qcb->q_h;

	*data = *qcb->q_rd_p++;
	qcb->q_curr_n--;

	return 0;
}

