#include<stdio.h>
#include<math.h>

static int N =30;


double y_n( int n)
{
	double	y;
	y = 1/(pow(-3.0,n)*(2.0*n+1));
	return y;
}


double y1_n (int n)
{

	double y;
	y = (pow(-1,n))/(2.0*n+1) ;
	return y;

}





int main ()
{
	int n ;
	double s;
	double df;
	double s1;
	double df1;
	/* definition and initialization*/
	double pi = 4*atan(1.0);
	for (n = 0; n<N; n++){
		s = s+ y_n(n);
		df = fabs((sqrt(12)*s) - pi);
		s1 = s1 + y1_n(n);
		df1 = fabs(4.0*s1 -pi );

		printf("%d %.50f %.50f \n", n, df, df1);
	}
}
