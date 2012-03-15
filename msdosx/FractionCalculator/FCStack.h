//
//  FCStack.h
//  FractionCalculator
//
//  Created by Kevin Jorgensen on 7/16/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface FCStack : NSObject
{
    NSMutableArray *stack;
}

/** Push OBJECT onto the top of the stack */
- (void) push: (id) object;

/** Pop off the top of the stack */
- (void) pop;

/** Empty the stack */
- (void) clear;

/** Print out the stack */
- (void) print;

/** Return whether the stack is empty or not */
- (BOOL) isEmpty;

/** Return whether the stack has at least two objects on it or not */
- (BOOL) hasTwoOperands;

/** Return the next-to-top object in the stack */
- (id) firstOperand;

/** Return the top object in the stack */
- (id) secondOperand;

/** Return the top object in the stack */
- (id) topOperand;

@end
