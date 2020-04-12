#include <stdio.h>
main()
{
  int p, i , m , tab[50];
  printf(" Donnez le nombre des elements du tableau :");
  scanf("%d", &m);
  for (i=1 ;i <= m ; i++)
  {  // collect data
    printf(" Donnez tab[%d] : ",i);
    scanf("%d", &tab[i]);
  }
  printf(" Entrez indice element a supprimer : ");
  scanf("%d", &p);
  // check for validity of the index
  if ((p<=0) ||(p>= m))
    printf("Supression impossible, indice entre 1 est %d" ,m);
  else
  {
    // Supression
    for (i = p; i<=m ;i++ )
      tab[i]= tab[i+1];
    printf(" Apres suppresion de l element : %d " ,p);
    // forget about the last element
    for (i =1 ; i<m; i++)
      printf("\n  tab[%d] = %d", i, tab[i]);
  }

}
