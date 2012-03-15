typedef struct {
  int lengthInSeconds;
  int yearRecorded;
} Song;

Song  make_song    (int seconds, int year);
void  display_song (Song theSong);