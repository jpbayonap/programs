#include<stdio.h>
#include<math.h>
static double h;
static double r1f;
static double r2f;
static double r3f;
static double v1f;
static double v2f;
static double v3f;
static double q;
static double m;
static double b;

double drdt (double t, double ri, double vi)
{
double bibun;
bibun = vi;
return(bibun);
}

double dv1dt(double t ,double r1i, double v2i )
{
  double bibun;
  bibun = (q/m)*b*v2i;
  return(bibun);
}

double dv2dt(double t ,double r2i, double v1i )
{
  double bibun;
  bibun = -(q/m)*b*v1i;
  return(bibun);
}

int ProceedOneStep (double t, double r1i, double r2i, double r3i, double v1i, double v2i, double v3i)
{
  double dr11,dr21,dr31;
  double dv11,dv21 ,dv31;
  double dr12,dr22;
  double dv12,dv22;

  dr31 = h*drdt(t,r3i,v3i);
  dv31 = 0;
  dr21 = h*drdt(t,r2i,v2i);
  dv21 = h*dv2dt(t,r2i,v1i);
  dr11 = h*drdt(t,r1i,v1i);
  dv11 = h*dv1dt(t,r1i,v2i);
/* second step */
  dr22 = h*drdt(t,r2i+dr21,v2i+dv21);
  dr12 = h*drdt(t,r1i+dr11, v1i+dv11);
  dv22 = h*dv2dt(t,r2i+dr21,v1i+dv11);
  dv12 = h*dv1dt(t,r1i+dr11,v2i+dv21);
  r1f = r1i +0.5*(dr11+dr12);
  r2f = r2i + 0.5*(dr21+dr22);
  r3f = r3i +dr31;
  v1f = v1i + 0.5*(dv11+dv12);
  v2f = v2i + 0.5*(dv21+dv22);
  v3f = v3i + dv31;
  return(0);
}

int main()
{
double t;
double r1i,r2i,r3i;
double v1i,v2i,v3i;
r1i = 1;
r2i = 0;
r3i = 0;
v1i = 0;
v2i = 0.5;
v3i = 0.8;
h = 1.0E-1;
q= 1.9;
m = 1.9;
b = 4.0;
for (t= 0.0;t<10.0; t=t+h){
  printf("%0.18f %0.18f %0.18f %0.18f \n",t,r1i,r2i,r3i );
  ProceedOneStep(t,r1i,r2i,r3i,v1i,v2i,v3i);
  r1i =r1f;
  r2i= r2f;
  r3i= r3f;
  v1i= v1f;
  v2i = v2f;
  v3i = v3f;
}
}
