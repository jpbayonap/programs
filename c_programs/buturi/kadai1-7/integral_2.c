#include<stdio.h>
#include<math.h>

int main()
{
  int i;
  double x;
  double sum;
  double DX;
  double pi;
  
  DX= 0.01;
  sum= 0.0;
  pi= 4*atan(1.0);
  for(x=0;x<= pi/2; x=x+DX){
    double y;
    y = pow(sin(x), 2.0);
      sum = sum + y*DX;
  }

  printf("Ans= %f\n",sum );
}

