#include<stdio.h>
#include<math.h>


static  int N=100;


double y_in(double x, int i)
{
  double y;
  y= (pow(-1, i)* pow(x,2.0*i+1.0) )/ (2.0*i+1.0);
  return y;
}

int main()
{
  int i;
  double sum;
  double dif;
  double pi;
  double x;
  x = 1.0; 
  pi = 4*atan(1.0);
  for (i = 0 ; i<N; i++){
   sum = sum + y_in(x, i) ;
   dif = fabs(pi -4*sum) ;
   printf("%d %f \n", i, dif);
  }
}

