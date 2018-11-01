#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <string.h>
#include <strings.h>
#define __USE_MISC
#include <arpa/inet.h>
#include <errno.h>

int SockPrepareInetAddr(char* ip, int port, struct sockaddr_in* sockAddr)
{
	if (NULL == ip)       return -1;
	if (port > 0xffff)    return -1;
	if (NULL == sockAddr) return -1;

	struct in_addr ipAddr;
	if (0 == inet_aton(ip, &ipAddr)) return -1;

	bzero(sockAddr, sizeof(struct sockaddr_in));
	sockAddr->sin_family = AF_INET;
	sockAddr->sin_addr   = ipAddr;
	sockAddr->sin_port   = htons(port);
	
	return 0;
}

int main(void)
{
	int sockDescriptor = -1;

	if (-1 == (sockDescriptor = socket(AF_INET, SOCK_DGRAM, 0))) {
		printf("Create socket fail!\r\n");
		return -1;
	}

#if 0 
// This is a bug, as a client, it can't bind sock addr, 
// if you force do it, it will turn out error.

	// Prepare the source sock addr
	struct sockaddr_in srcInetAddr;
	if (-1 == SockPrepareInetAddr("127.0.0.1", 30000, &srcInetAddr)) {
		printf("Prepare source addr fail!\r\n");
		return -3;
	}

	if (-1 == bind(sockDescriptor, (struct sockaddr*)&srcInetAddr, sizeof(srcInetAddr))) {
		printf("Bind source addr Fail!\r\n");
		return -2;
	}
#endif

	// prepare the destination sock addr
	struct sockaddr_in destInetAddr;
	if (-1 == SockPrepareInetAddr("255.255.255.255", 30001, &destInetAddr)) {
		printf("Prepare dest addr fail!\r\n");
		return -2;
	}

	// If you send udp broadcast datagram, you must enable the sock option broadcast function.
	int sockBroadcastSet = 1;
	if (-1 == setsockopt(sockDescriptor, SOL_SOCKET, SO_BROADCAST, &sockBroadcastSet, sizeof(int))) {
		perror("Setsockopt Fail\r\n");
		return -3;
	}

	ssize_t sendtoRet = -1;
	char sendBuf[111] = "Hello";
	if (-1 == (sendtoRet = sendto(sockDescriptor, 
								  sendBuf, 
								  105, 
								  0, 
								  (struct sockaddr*)&destInetAddr, 
								  sizeof(struct sockaddr)))) {
		printf("%d = Sendto func fail!\r\n", sendtoRet);
		printf("errno : %s\r\n", strerror(errno));
		return -4;
	}

	printf("The end!\r\n");

	close(sockDescriptor);

	return 0;
}

