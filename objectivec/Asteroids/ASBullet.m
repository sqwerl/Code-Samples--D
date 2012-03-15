//
//  ASBullet.m
//  Asteroids
//
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
