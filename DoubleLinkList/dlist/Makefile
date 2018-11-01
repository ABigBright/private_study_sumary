OBJS = $(patsubst %.c, %.o, $(wildcard *.c))
BIN_NAME = dl
CFLAGS = -std=c11 -I . 

$(BIN_NAME) : $(OBJS)
	$(CC) -o $@ $^	

clean : 
	rm -rf $(OBJS) $(BIN_NAME)
.PHONY = clean
