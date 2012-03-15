//
//  ASDrawable.m
//  Asteroids
//
//  Created by Ian Henderson on 9/27/09.
//  Copyright 2009 __MyCompanyName__. All rights reserved.
//

#import "ASDrawable.h"
#import "ASView.h"

@implementation ASDrawable

@synthesize view;
@synthesize rotation;
@synthesize xVelocity, yVelocity;
@dynamic x, y;

unsigned _ASDrawable_drawableCount;

+ (id)alloc
{
    _ASDrawable_drawableCount++;
    return [super alloc];
}

- (void)dealloc
{
    _ASDrawable_drawableCount--;
    [image release];
    [super dealloc];
}

+ (unsigned)drawableCount
{
    return _ASDrawable_drawableCount;
}

- (id)initWithImage:(NSImage *)img
{
    if (![super init]) {
        return nil;
    }
    image = [img retain];
    if (image) {
        frame = (NSRect){NSZeroPoint, [image size]};
    }
    return self;
}

- (float)x { return frame.origin.x+frame.size.width/2.; }
- (float)y { return frame.origin.y+frame.size.height/2.; }
- (void)setX:(float)x { frame.origin.x = x-frame.size.width/2.; }
- (void)setY:(float)y { frame.origin.y = y-frame.size.height/2.; }

- (void)update
{
    // override me
}

- (void)draw
{
    [NSGraphicsContext saveGraphicsState];
    
    // rotate and move the image based on the position and rotation
    NSAffineTransform *transform = [NSAffineTransform transform];
    [transform translateXBy:frame.origin.x+frame.size.width/2. yBy:frame.origin.y+frame.size.height/2.];
    [transform rotateByDegrees:rotation];
    [transform translateXBy:-frame.size.width/2. yBy:-frame.size.height/2.];
    [transform concat];
    
    // update position based on velocity
    self.x += self.xVelocity;
    self.y += self.yVelocity;
    
    // wrap drawables to the other side if they go offscreen
    if (![self onScreen]) {
        if (frame.origin.x >= self.view.frame.origin.x) {
            frame.origin.x -= self.view.frame.size.width;
        }
        if (frame.origin.y >= self.view.frame.origin.y) {
            frame.origin.y -= self.view.frame.size.height;
        }
        if (frame.origin.x < 0) {
            frame.origin.x += self.view.frame.size.width;
        }
        if (frame.origin.y < 0) {
            frame.origin.y += self.view.frame.size.height;
        }
    }
    
    [self update];
    
    // draw the image
    [image drawAtPoint:NSZeroPoint fromRect:(NSRect){NSZeroPoint, [image size]} operation:NSCompositeSourceOver fraction:1];
    
    [NSGraphicsContext restoreGraphicsState];
}

- (void)die
{
    [self.view removeDrawable:self];
}

- (BOOL)onScreen
{
    return NSIntersectsRect(frame, self.view.frame);
}

- (NSRect)_frame
{
    return frame;
}

- (BOOL)collidesWith:(ASDrawable *)otherDrawable
{
    return NSIntersectsRect(frame, [otherDrawable _frame]);
}

@end
