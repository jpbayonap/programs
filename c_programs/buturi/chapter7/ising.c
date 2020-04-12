#include <stdio.h>
#include<stdlib.h>
#include<math.h>
#include "cpgplot.h"
#include "mtwister.h"
#define NPANEL 100
#define SAMPLE 1000
static int spins[NPANEL][NPANEL];  //spin matrix
static double T ;
double drnd()  // 0,1 random number
{
	return(genrand_real2());
}


void setspins(){
int i ,j ;

	for (i=0;i<NPANEL; i++){
		for(j=0 ;j<NPANEL;j++){
			if (drnd()<0.5){
				spins[i][j] = 1	;
			}else{
				spins[i][j] = -1;
			}	
		}
	}
}
int ginit()
{

	cpgopen("/xwindow"); 
	cpgscr(10,0.7,0.0,0.0);
	cpgscr(20,0.1,0.4,0.1);
	cpgenv(0,NPANEL,0,NPANEL,1,-2);

}


int gdraw(){

int i,j;
	
	cpgbbuf();
	cpgeras();
	for (i=0;i<NPANEL; i++){
		for(j=0 ;j<NPANEL;j++){
			if (spins[i][j] >0 ){
				cpgsci(20);
		}else{
			cpgsci(10);
		}
			cpgrect(i+0.1,i+0.9,j+0.1,j+0.9);  //panel size 
		}
	}
	cpgebuf();
	usleep(100000);

}


// set k and j parameter


void onestep(){
 int k,l ;
 double delta;
 double p;
 
k = drnd()*NPANEL;
l = drnd()*NPANEL;
 delta = 2*spins[k][l]*(spins[(k+1)%NPANEL][l]+spins[(k-1+NPANEL)%NPANEL][l]+spins[k][(l+1)%NPANEL]
		+spins[k][(l-1+NPANEL)%NPANEL]);
 p = exp(-1.0*delta/T);
 if (p>drnd()){
 	spins[k][l] = -1*spins[k][l];
 }else{
 	spins[k][l] = spins[k][l];
 }

}




double EN( ){
	int N;
	int i,j;
	double e; 
	double E;
	N= NPANEL*NPANEL;
	e =0.0;

	for (i =0 ;i <NPANEL; i++){
		for(j= 0; j<NPANEL; j++){
			e += spins[i][j]*(spins[(i+1)%NPANEL][j]+spins[i][(j+1)%NPANEL]);
		}
	}
 
E = -e/N;
return E;

}


double MA(){
	int N; 
	int i,j;
	double m ;
	double M;
	N = NPANEL*NPANEL ;
	m = 0.0;
	for (i =0 ;i <NPANEL; i++){
		for(j= 0; j<NPANEL; j++){

			m += spins[i][j];
		}

	} 

	M = pow(m/N,1);
return M;
}


int gfini()
{

	cpgclos();
}



int main()
{
	double Esum, E2sum, En;
	double Msum, M2sum, Mn;
	double c;
	double x;
	int i, j;
	int N;

	init_genrand(2525);  //random number
	// Run algorithm for different temperatures
	
		setspins(); 
		N= NPANEL*NPANEL;
		for (T=0;T<5;T+=0.1){
			setspins(); 
			// bring the system to equilibrium
			for  (i =0;i<10000;i++)
				onestep();
			x = 0.0;
			c = 0.0;
			/*ginit();*/
			Esum = 0.0;
			E2sum = 0.0;
			Msum = 0.0;
			M2sum =0.0;
			// data sampling
			for (i =0;i<1000;i++){
			/*gdraw();	*/
				En = EN();
				Mn = MA();
				Esum = Esum +En ; 
				E2sum = E2sum + En*En ;
				Msum = Msum + Mn ;
				M2sum =  M2sum + Mn*Mn ; 
				// montecarlo step for taking independent measurements
				for (j=0;j<100;j++)
					onestep();
			/*gfini();*/

			}

			c = (E2sum/1000 - pow(Esum/1000,2)) /pow(T,2);
			x = (M2sum/1000 - pow(Msum/1000,2));

			printf("%f %f %f %f %f \n", T,Esum/1000,c,Msum/1000,x);
			
		}
			
}