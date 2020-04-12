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
  double dk11,dk12,dk13,dk14;
  double dk21,dk22,dk23,dk24;
  double dk31,dk32,dk33,dk34;
  double dvk11,dvk12,dvk13,dvk14;
  double dvk21,dvk22,dvk23,dvk24;
  double dr31,dv31;

  dr31 = h*drdt(t,r3i,v3i);
  dv31 = 0;
  dk21 = h*drdt(t,r2i,v2i);
  dvk21 = h*dv2dt(t,r2i,v1i);
  dk11 = h*drdt(t,r1i,v1i);
  dvk11 = h*dv1dt(t,r1i,v2i);
/* second step */
  dk22 = h*drdt(t+ 0.5*h,r2i+0.5*dk21,v2i+0.5*dvk21);
  dk12 = h*drdt(t+0.5*h,r1i+0.5*dk11, v1i+0.5*dvk11);
  dvk22 = h*dv2dt(t+0.5*h,r2i+0.5*dk21,v1i+0.5*dvk11);
  dvk12 = h*dv1dt(t+0.5*h,r1i+0.5*dk11,v2i+0.5*dvk21);
  /*third step */
  dk23 = h*drdt(t+0.5*h,r2i+0.5*dk22,v2i+0.5*dvk22);
  dk13 = h*drdt(t+0.5*h,r1i+0.5*dk12, v1i+0.5*dvk12);
  dvk23 = h*dv2dt(t+0.5*h,r2i+0.5*dk22,v1i+0.5*dvk12);
  dvk13 = h*dv1dt(t+0.5*h,r1i+0.5*dk12,v2i+0.5*dvk22);
  /* fourth step */
  dk24 = h*drdt(t+h,r2i+dk23,v2i+dvk23);
  dk14 = h*drdt(t+h,r1i+dk13, v1i+dvk13);
  dvk24 = h*dv2dt(t+h,r2i+dk23,v1i+dvk13);
  dvk14 = h*dv1dt(t+h,r1i+dk13,v2i+dvk23);
  /* final values */
  r1f = r1i +(dk11+2*dk12+2*dk13+dk14)/6;
  r2f = r2i +(dk21+2*dk22+2*dk23+dk24)/6;
  r3f = r3i +dr31;
  v1f = v1i + (dvk11+2*dvk12+2*dvk13+dvk14)/6;
  v2f = v2i + (dvk21+2*dvk22+2*dvk23+dvk24)/6;
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
