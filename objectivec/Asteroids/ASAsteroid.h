//
//  ASAsteroid.h
//  Asteroids
//
//  Created by Admin on 2/3/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
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
