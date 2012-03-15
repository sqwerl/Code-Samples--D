#include <stdio.h>
#include "math_functions.h"
#include "song.h"

main ()
{
  const int numberOfSongs = 3;
  printf ("total number of songs will be: %i\n", numberOfSongs);

  int i;
  for (i = 0; i < numberOfSongs; i++) {
    printf ("loop trip %i ", i);
  }

  printf ("\n");

  Song song1  = make_song (223, 1998);
  Song song2  = make_song (303, 2004);
  Song song3  = { 315, 1992 };

  display_song (song3);

  int combinedLength = sum (song1.lengthInSeconds, song2.lengthInSeconds);
  printf ("combined length of song1 and song2 is %i\n", combinedLength);

  float x = (float) song1.lengthInSeconds;
  float y = (float) song2.lengthInSeconds;
  float z = (float) song3.lengthInSeconds;

  float averageLength;
  averageLength = average (x, y, z);

  printf ("average length is: %f as a float ", averageLength);
  printf ("and %i as an int\n", (int) averageLength);	
}