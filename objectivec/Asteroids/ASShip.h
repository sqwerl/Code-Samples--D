//
//  ASShip.h
//  Asteroids
//
//  Created by Ian Henderson on 9/27/09.
//  Copyright 2009 __MyCompanyName__. All rights reserved.
//

#import <Cocoa/Cocoa.h>
#import "ASDrawable.h"

@interface ASShip : ASDrawable {
    int bulletReadiness;
    ASDrawable *shield;
}

@property(nonatomic, retain) ASDrawable *shield;

- (void) dealloc;

@end
