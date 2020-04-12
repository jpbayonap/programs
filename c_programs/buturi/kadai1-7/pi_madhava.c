#include<stdio.h>
#include<math.h>

static int N =30;


double y_n( int n)
{
	double	y;
	y = 1/(pow(-3.0,n)*(2.0*n+1));
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
		df = fabs((sqrt(12)*s) - pi);
		printf("%d %.50f \n", n, df);
	}
}
