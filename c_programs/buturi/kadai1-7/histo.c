#include <stdio.h>
#include<math.h>
#include<stdlib.h>

int main()
{

	int i,x,y;
	FILE *fp;
	int h[200];

	fp = fopen("rawdata.dat","r");
	if (NULL == fp){

	fprintf(stderr, "file open error\n" );
	exit(1);
	}


	for (i=0; i<200;i++){

		h[i]=0;
	}
	while (EOF!=fscanf(fp,"%d",&y)){
		h[y]++;
		}

	for(i=0;i<200;i++){
		printf("%d %d %f\n",i,h[i],sqrt(h[i]));
	}
	fclose(fp);
}