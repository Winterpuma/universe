/* codeforces.com/problemset/problem/1020/A */

#include <stdio.h>
#include <math.h>

int main()
{
	int n, h, a, b;
	int k;
	int ta, fa, tb, fb;
	int steps;

	scanf("%d %d %d %d", &n, &h, &a, &b);
	scanf("%d", &k);
		
	while (k--)
	{
		scanf("%d %d %d %d", &ta, &fa, &tb, &fb);
		steps = 0;
		if (ta != tb) // ���� � ������ ������
		{
			if (fa < a) // ���� ���� ��������
			{
				steps += a - fa;
				fa = a;	
			}
			else if (fa > b) // ���� ���� ��������
			{
				steps += fa - b;
				fa = b;	
			}
			
			steps += abs(ta-tb);
		}

		steps += abs(fa - fb);
		printf("%d\n", steps);
	}
}
