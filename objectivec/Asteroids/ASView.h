//
//  ASView.h
//  Asteroids
//
//  Created by Ian Henderson on 9/27/09.
//  Copyright 2009 __MyCompanyName__. All rights reserved.
//

#import <Cocoa/Cocoa.h>

@class ASDrawable;

@interface ASView : NSView {
    NSMutableArray *drawables;
    NSMutableArray *queuedDrawables;
    NSMutableArray *drawablesToRemove;
    IBOutlet NSTextField *drawableCount;
    
    BOOL drawing;
}

@property(nonatomic, readonly) NSArray *drawables;

- (void)addDrawable:(ASDrawable *)drawable;
- (void)removeDrawable:(ASDrawable *)drawable;

@end
