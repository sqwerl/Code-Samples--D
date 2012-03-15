//
//  ASShip.h
//  Asteroids
//
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
