#include<stdio.h>
//only works with natural numbers
int main(){
int t[100], rep[100] ;
int i ,j;
printf("Donnez la taille du tableau :");
scanf("%d",&i);
for(j=1; j<=i ;j++)
  {
  printf("Donnez t[%d] :", j);
  scanf("%d",&t[j]);
  }

for (j =1 ; j<=100; j++)
  rep[j]= 0 ;

for (j=1; j<=i;j++)
  rep[t[j]] +=1;
for (j =1; j<= 100;j++)
  {
    if(rep[j] != 0)
    printf(" valeur %d  est repete  %d fois\n",j, rep[j] );
  }
  return 0;
}
