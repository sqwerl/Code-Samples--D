//
//  ASView.m
//  Asteroids
//
//  Created by Ian Henderson on 9/27/09.
//  Copyright 2009 __MyCompanyName__. All rights reserved.
//

#import "ASView.h"
#import "ASDrawable.h"
#import "ASShip.h"
#import "ASKeyboard.h"
#import "ASAsteroid.h"

@implementation ASView

@synthesize drawables;

- (void)awakeFromNib
{
    ASShip *ship = [[ASShip alloc] init];
    ship.x = NSMidX(self.frame);
    ship.y = NSMidY(self.frame);
    [self addDrawable:ship];
    [ship release];
    
    // add more drawables here
    ASAsteroid *asteroid = [[ASAsteroid alloc] initLarge];
    [self addDrawable:asteroid];
    asteroid.xVelocity = 1;
    asteroid.yVelocity = 1;
    [NSTimer scheduledTimerWithTimeInterval:1./60. target:self selector:@selector(tick:) userInfo:nil repeats:YES];
}

- (id)initWithFrame:(NSRect)frame {
    self = [super initWithFrame:frame];
    if (self) {
        drawables = [[NSMutableArray alloc] init];
        queuedDrawables = [[NSMutableArray alloc] init];
        drawablesToRemove = [[NSMutableArray alloc] init];
    }
    return self;
}

- (void)addDrawable:(ASDrawable *)drawable
{
    drawable.view = self;
    [(drawing ? queuedDrawables : drawables) addObject:drawable];
}

- (void)removeDrawable:(ASDrawable *)drawable
{
    if (drawing) {
        [drawablesToRemove addObject:drawable];
    } else {
        [drawables removeObject:drawable];
    }
}

- (void)tick:(NSTimer *)timer
{
    unsigned count = [ASDrawable drawableCount];
    [drawableCount setStringValue:[NSString stringWithFormat:@"%d drawable%s", count, (count == 1 ? "" : "s")]];
    [self setNeedsDisplay:YES];
}

- (BOOL)acceptsFirstResponder
{
    return YES;
}

- (void)keyDown:(NSEvent *)event
{
    [[ASKeyboard sharedKeyboard] _keyEvent:event];
}

- (void)keyUp:(NSEvent *)event
{
    [[ASKeyboard sharedKeyboard] _keyEvent:event];
}


- (void)dealloc
{
    [drawables release];
    [queuedDrawables release];
    [drawablesToRemove release];
    [super dealloc];
}

- (void)drawRect:(NSRect)dirtyRect {
    drawing = YES;
    for (ASDrawable *drawable in drawables) {
        [drawable draw];
    }
    [drawables addObjectsFromArray:queuedDrawables];
    [queuedDrawables removeAllObjects];
    [drawables removeObjectsInArray:drawablesToRemove];
    [drawablesToRemove removeAllObjects];
    drawing = NO;
}

@end
