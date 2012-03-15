//
//  FCStackCalculatorController.h
//  FractionCalculator
//
//  Created by Admin on 1/26/12.
//  Copyright 2012 __MyCompanyName__. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "FCStack.h"

@interface FCStackCalculatorController : NSObject
{
    FCStack *stack;
}

- (void) respondToInput: (NSString *) input;


@end
