//
//  ASAsteroid.h
//  Asteroids
//
//

#import "ASDrawable.h"

@interface ASAsteroid : ASDrawable{
    NSArray *smallerAsteroids;
}


- (id) initLarge;
- (id) initMedium;
- (id) initSmall;
- (void) update;
- (void) dealloc;
@end
