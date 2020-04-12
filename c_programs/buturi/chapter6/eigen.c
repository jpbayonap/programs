#include<stdio.h>
#include<math.h>

#define N 1000
#define XMIN 0.0
#define XMAX 10.0

static double D[N],E[N-1],Z[N*N];
static double delta = (XMAX-XMIN)/(N+1);
/* Set the potential */
double potential(double x)
{
	double V;
	V = pow(x,1) ;
	return V;
}
int SetMatrix()
{
	double x;
	int i;
	for (i=0;i<N;i++){
		D[i] = 2/pow(delta,2)+ potential(XMIN +(i+1)*delta);
		E[i] = -1/pow(delta,2);
	}
	return 0;
}

int main()
{
  char JOBZ;
  int n;
  int ldz;
  double WORK[2*N-2];
  int INFO;
  int i,j;
  SetMatrix();

  JOBZ ='V';
  n = N;
  ldz = N;
  dstev_(&JOBZ,&n,D,E,Z,&ldz,WORK,&INFO,1);
/*print */

  for(i=0;i<3;i++){
    printf("%f " ,D[i]);
    for (j =0;j<N;j++){
    	Z[i*N] =0;
    	Z[i*N+N-1]=0;

printf("%f ",Z[i*N+j]);
    }
    printf("\n");
  }
}
