#include<stdio.h>
#include<math.h>


static int N = 20;
double f (double x)
{
	double y;
	y=   cos(cos(cos(x- 0.5)+ 0.5) - 0.5) ;
	return (y);
}

double fd (double x ,double D)
{

	double y ;
	y = (f(x+ D) -f(x-D))/ 2*D ;
	return (y);

}

double true_f(double x)
{
	double y;
	y = -sin(cos(cos(x-0.5)+0.5)-0.5)*sin(cos(x-(1.0/2.0))+(1.0/2.0))*sin(x-(1.0/2.0)) ;
	return (y);
}

int main()
{
	double x = 4.0;
	int i;
	double D;
	double err;
	for (i=0;i<N;i++){
		D = pow(10,-i);
		err =fabs(fd(x,D)- true_f(x));
	printf("%g %g\n",D,err);
	}
}
