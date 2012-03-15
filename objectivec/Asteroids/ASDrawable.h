//
//  ASDrawable.h
//  Asteroids
//
//

#import <Cocoa/Cocoa.h>
#import "ASView.h"

@interface ASDrawable : NSObject {
    NSRect frame;
    float rotation;
    
    float xVelocity, yVelocity;
    
    ASView *view;
    
    NSImage *image;
}

@property(nonatomic) float x;
@property(nonatomic) float y;
@property(nonatomic) float xVelocity;
@property(nonatomic) float yVelocity;
@property(nonatomic) float rotation;

// note the "assign" -- this is to prevent a "cycle" where the drawable
// retains its view, and the view retains every drawable
@property(nonatomic, assign) ASView *view;

+ (unsigned)drawableCount;

- (id)initWithImage:(NSImage *)image;

- (BOOL)onScreen;
- (BOOL)collidesWith:(ASDrawable *)otherDrawable;

- (void)die;

- (void)draw;

/// you implement this ////
- (void)update;

@end
