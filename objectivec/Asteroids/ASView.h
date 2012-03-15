//
//  ASView.h
//  Asteroids
//
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
