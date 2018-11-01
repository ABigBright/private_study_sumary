OBJS = $(patsubst %.c, %.o, $(wildcard *.c))
BIN_NAME = udpbrocast
CFLAGS = -std=c11 -I . -g

$(BIN_NAME) : $(OBJS)
	$(CC) -o $@ $^	

clean : 
	rm -rf $(OBJS) $(BIN_NAME)
.PHONY = clean
