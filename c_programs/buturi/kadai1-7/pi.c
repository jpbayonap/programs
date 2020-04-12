#include<stdio.h>
#include<math.h>

static int N =30;


double y_n( int n)
{
	double	y;
	y = (1.0/pow(16.0,n))*( (4.0/(8.0*n+1.0)) - (2.0/(8.0*n+4.0)) - (1.0/(8.0*n+5.0)) - (1.0/(8.0*n+6.0)) );
	return y;
}




int main ()
{
	int n ;
	double s;
	double df;
	/* definition and initialization*/
	double pi = 4*atan(1.0);
	for (n = 0; n<N; n++){
		s = s+ y_n(n);
		df = fabs(s - pi);
		printf("%d %.50f \n", n, df);
	}
}