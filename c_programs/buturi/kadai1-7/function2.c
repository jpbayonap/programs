#include<stdio.h>
#include<math.h>

/*  12.0 for real numbers*/
/*  functions*/


double u_tan(double v, double w)
{

	double u;
	if (w! = 0.0){
		u = tan(v/w);
	}
	return(u);
}

int main()
{
	double x,y,z;
	x = 2.0;
	y= 3.0 ;
	z= u_tan(x,y);

}