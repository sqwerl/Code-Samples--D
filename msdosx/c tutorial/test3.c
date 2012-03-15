#include <stdio.h>
#include "math_functions.h"

main ()
{
  int   theSum     = sum (8, 12);
  float theAverage = average (16.9, 7.86, 3.4);

  printf ("the sum is: %i ", theSum);
  printf ("and the average is: %f \n", theAverage);
  printf ("average casted to an int is: %i \n", (int)theAverage);
}