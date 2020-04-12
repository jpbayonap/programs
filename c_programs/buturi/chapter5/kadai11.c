#include<stdio.h>
#include<math.h>

static double h;
static double xf;
static double vf;
static double m;
static double k;
static double f ; 

/* dxdt = 0.5*(sin(x)+cos(x)) */



double dxdt (double t,	double xi,	double vi)
{

double bibun;
bibun = vi;
return(bibun);

}


double dvdt(double t,	double xi,	double vi)
{

double bibun;
bibun = -10 -(k/m)*xi -(f/m)*vi;
return(bibun);

}

int ProceedOneStep (double t,	double xi,	double vi)
{
	
	double dx1;
	double dx2;
	double dv1;
	double dv2;

	dx1 = h*dxdt(t,xi,vi);
	dv1 = h*dvdt(t,xi,vi);
	dx2 = h*dxdt(t+h,xi+dx1,vi+dv1);
	dv2 = h*dvdt(t+h,xi+dx1,vi+dv1);
	xf = xi + 0.5*(dx1+dx2);
	vf = vi +0.5*(dv1+dv2);
	return(0);
}



int main()
{

double t;
double xi = 2;
double vi = 3;

h= 1.0E-1;
m = 3;
k= 5;
f= 2;

for(t=0.0; t<5.0; t=t+h){
	printf("%f %f %f\n",t,xi,vi);
	ProceedOneStep(t,xi,vi);
	xi=xf;
	vi =vf;
	}
}

