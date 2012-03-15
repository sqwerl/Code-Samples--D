#include <stdio.h>
	
int sum ( int x, int y );

main ()
{
  int theSum = sum (10, 11);
  printf ( "Sum: %i\n", theSum );
}

int sum ( int x, int y )
{
  return x + y;
}