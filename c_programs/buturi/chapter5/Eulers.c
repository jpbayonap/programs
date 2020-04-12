#include<stdio.h>
#include<math.h>

static double h;
static double xf;



double dxdt(double t, double x)
{
/* dxdt = 0.5*(sin(x)+cos(x)) */
	double bibun ;
	bibun = 0.5*(-sin(x)+cos(x)+exp(-x));
	return (bibun);
}

int ProceedOneStep (double t, double xi)
{

	double dx1;
	double dx2;


	dx1 = h*dxdt(t,xi);
	dx2 = h*dxdt(t+h,xi+dx1);
	xf = xi + 0.5*(dx1+dx2);
	return(0);
}

double Ana(double t)
{

	double x;
	x= 0.5*(sin(t)+cos(t)-exp(-t));
	return(x);
}

int main()
{

double t;
double xi;

h= 1.0E-1;
xi=0.0;
for(t=0.0; t<5.0; t=t+h){
	printf("%f %f %f\n",t,xi,Ana(t));
	ProceedOneStep(t,xi);
	xi=xf;
	}
}

