//
//  ASShip.m
//  Asteroids
//
//  Created by Ian Henderson on 9/27/09.
//  Copyright 2009 __MyCompanyName__. All rights reserved.
//

#import "ASShip.h"
#import "ASKeyboard.h"
#import "ASBullet.h"


@implementation ASShip

@synthesize shield;

- (id)init
{
    return [super initWithImage:[NSImage imageNamed:@"ship"]];
}


- (void)update
{
    [super update];
    
    ASKeyboard *k = [ASKeyboard sharedKeyboard];
    if (k.upArrowPressed) {
        self.xVelocity += -sin(rotation/180.*3.14159)*0.2;
        self.yVelocity += cos(rotation/180.*3.14159)*0.2;
    }
    if (k.leftArrowPressed) {
        rotation += 5;
    }
    if (k.rightArrowPressed) {
        rotation -= 5;
    }
    
    if (k.shootPressed) {
        if (!(bulletReadiness++ % 8)) {
            
            // create the bullet
            
            ASBullet *d = [[ASBullet alloc] init];
            d.x = self.x + -sin(rotation/180.*3.14159)*40;
            d.y = self.y + cos(rotation/180.*3.14159)*40;
            d.xVelocity = self.xVelocity + -sin(rotation/180.*3.14159)*7;
            d.yVelocity = self.yVelocity + cos(rotation/180.*3.14159)*7;
            d.rotation = self.rotation;
            [self.view addDrawable:d];
            [d release];
            
        }
    } else {
        bulletReadiness = 0;
    }
    if (self.shield == nil && k.shieldPressed == YES){
        self.shield = [[ASDrawable alloc] initWithImage:[NSImage imageNamed:@"shield"]];
        [shield release];
    }
    if (self.shield != nil && k.shieldPressed != YES){
        self.shield = nil;
    }
    [self.shield draw];
}

- (void) dealloc
{
    [shield release];
    [super dealloc];
}
@end
