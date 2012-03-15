//
//  ASKeyboard.h
//  Asteroids
//
//  Created by Ian Henderson on 9/27/09.
//  Copyright 2009 __MyCompanyName__. All rights reserved.
//

#import <Cocoa/Cocoa.h>


@interface ASKeyboard : NSObject {
    BOOL leftArrowPressed, rightArrowPressed, upArrowPressed, downArrowPressed, shootPressed, shieldPressed;
}

@property(nonatomic, readonly) BOOL leftArrowPressed;
@property(nonatomic, readonly) BOOL rightArrowPressed;
@property(nonatomic, readonly) BOOL upArrowPressed;
@property(nonatomic, readonly) BOOL downArrowPressed;

@property(nonatomic, readonly) BOOL shootPressed;
@property(nonatomic, readonly) BOOL shieldPressed;


+ (ASKeyboard *)sharedKeyboard;


- (void)_keyEvent:(NSEvent *)event;

@end
