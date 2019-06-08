#include<stdio.h>
int main()
{
    int T;
    scanf("%d",&T);
    for(int i=0;i<T;++i)
    {
        int N;
        int K;
        long A;
        scanf("%d%d%d",&N,&A,&K);
        long X;
        int Y;
        X=A*N*(N-1)+(K-1)*(360*(N-2)-2*A*N);
        Y=N*(N-1);
        for(int j=N*(N-1);j>0;--j)
        {
            if(X%j==0&&Y%j==0)
            {
                long Z;
                int W;
                Z=X/j;
                W=Y/j;
                printf("%d %d\n",Z,W);
                break;
            }

        }
    }
    return 0;
}

