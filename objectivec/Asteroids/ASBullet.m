//
//  ASBullet.m
//  Asteroids
//
//  Created by Ian Henderson on 9/27/09.
//  Copyright 2009 __MyCompanyName__. All rights reserved.
//

#import "ASBullet.h"

@implementation ASBullet

- (id)init
{
    if (![super initWithImage:[NSImage imageNamed:@"bullet"]]) {
        return nil;
    }
    lifetime = 60;
    return self;
}

- (void)update
{
    [super update];
    if (!lifetime--) {
        [self die];
    }
}

@end
