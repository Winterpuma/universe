#include <stdio.h>
#include <unistd.h>
#define N 101

int main()
{
	for (int i = 0; i < N; i++)
	{
		usleep(100000); // usleep(microseconds)
		printf("\rLoading...%d", i);
	}
}
