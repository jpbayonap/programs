#include<stdio.h>
#include<math.h>

int main()
{
  int i;
  double x;
  double sum;
  double DX;
  
  DX= 0.01;
  sum= 0.0;
  for(x=0;x<= 5.0; x=x+DX){
    double y;
    y =cos(x);
      sum = sum + y;
  }

  printf("Ans= %f\n",sum );
}

