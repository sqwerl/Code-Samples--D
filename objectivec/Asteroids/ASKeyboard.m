//
//  ASKeyboard.m
//  Asteroids
//
//

#import "ASKeyboard.h"

@implementation ASKeyboard

@synthesize leftArrowPressed, rightArrowPressed, upArrowPressed, downArrowPressed, shootPressed, shieldPressed;

- (void)_keyEvent:(NSEvent *)event
{
    BOOL down = ([event type] == NSKeyDown);
    switch ([[event charactersIgnoringModifiers] characterAtIndex:0]) {
        case NSLeftArrowFunctionKey:
            leftArrowPressed = down;
            return;
        case NSRightArrowFunctionKey:
            rightArrowPressed = down;
            return;
        case NSUpArrowFunctionKey:
            upArrowPressed = down;
            return;
        case NSDownArrowFunctionKey:
            downArrowPressed = down;
            return;
        case 's':
            shieldPressed = down;
            return;
        case ' ':
            shootPressed = down;
            return;
    }
}

+ (ASKeyboard *)sharedKeyboard
{
    static ASKeyboard *k = nil;
    if (!k) {
        k = [[self alloc] init];
    }
    return k;
}

@end
