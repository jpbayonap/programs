#include<stdio.h>
#include<math.h>

static double DX = 0.01;

double y_sin(double x)
{

double y;
  y= pow(sin(x), 2.0);
  return y;
}

int main()
{
  int i;
  double x;
  double sum;
  double pi;
  
  DX= 0.01;
  sum= 0.0;
  pi= 4*atan(1.0);
  for(x=0;x<= pi; x=x+DX){
    double y;
    y = y_sin(x);
      sum = sum + y*DX;
  }

  printf("Ans= %f\n",sum );
}

