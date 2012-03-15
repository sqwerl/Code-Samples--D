//
//  ASAsteroid.m
//  Asteroids
//
//  Created by Admin on 2/3/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#import "ASAsteroid.h"
#import "ASShip.h"
#import "ASBullet.h"

@implementation ASAsteroid

- (id) initLarge
{
    [super initWithImage:[NSImage imageNamed:@"asteroidLarge"]];
    ASAsteroid *asteroid1 = [[ASAsteroid alloc] initMedium];
    ASAsteroid *asteroid2 = [[ASAsteroid alloc] initMedium];
    
    smallerAsteroids = [[NSArray alloc] initWithObjects:asteroid1, asteroid2, nil]; 
    return self;
}

- (id) initMedium
{
    [super initWithImage:[NSImage imageNamed:@"asteroidMedium"]];
    ASAsteroid *asteroid1 = [[ASAsteroid alloc] initSmall];
    ASAsteroid *asteroid2 = [[ASAsteroid alloc] initSmall];
    ASAsteroid *asteroid3 = [[ASAsteroid alloc] initSmall];
    
    smallerAsteroids = [[NSArray alloc] initWithObjects:asteroid1, asteroid2, asteroid3, nil];
    return self;
}
- (id) initSmall
{
    [super initWithImage:[NSImage imageNamed:@"asteroidSmall"]];
    smallerAsteroids = [[NSArray alloc] init];
    return self;
}    

- (void) update
{
    for (ASDrawable *drawable in self.view.drawables)
    {
        if ([drawable isKindOfClass:[ASShip class]] && [drawable collidesWith:self])
        {
            if ([drawable shield] == nil)
            {
                [drawable die];
            }
        }
        if ([drawable isKindOfClass:[ASBullet class]] && [drawable collidesWith:self])
        {
            [drawable die];
            for (ASAsteroid *smallerAsteroid in smallerAsteroids)
            {
                smallerAsteroid.x = self.x;
                smallerAsteroid.y = self.y;
                smallerAsteroid.xVelocity = self.xVelocity + (rand() % 7) - 3;
                smallerAsteroid.yVelocity = self.yVelocity + (rand() % 7) - 3;
                [self.view addDrawable:smallerAsteroid];
            }
            [self die];
            [self release];
        } 
    }

}

- (void) dealloc
{
    [smallerAsteroids release];
    [super dealloc];
}
@end
