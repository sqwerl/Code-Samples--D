#include <stdio.h>
#include "song.h"

Song make_song (int seconds, int year)
{
  Song newSong;

  newSong.lengthInSeconds = seconds;
  newSong.yearRecorded    = year;
  display_song (newSong);

  return newSong;
}

void display_song (Song theSong)
{
  printf ("the song is %i seconds long ", theSong.lengthInSeconds);
  printf ("and was made in %i\n", theSong.yearRecorded);
}