//
//  FCStack.m
//  FractionCalculator
//
//  Created by Kevin Jorgensen on 7/16/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import "FCStack.h"

#import "FCConsole.h"


@implementation FCStack


- (id) init
{
    self = [super init];
    
    if (self)
    {
        stack = [[NSMutableArray alloc] init];
    }
    
    return self;
}


- (void) dealloc
{
    [stack release];
    
    [super dealloc];
}


#pragma mark -
#pragma mark Stack management

- (void) push: (id) object
{
    [stack addObject: object];
}


- (void) pop
{
    [stack removeLastObject];
}


- (void) clear
{
    while ([stack count])
        [stack removeLastObject];
}


#pragma mark -

- (void) print
{
    [FCConsole writeLine: @"--------------------- top of stack"];
    for (int i = (int) [stack count] - 1; i >= 0; i -= 1)
    {
        [FCConsole writeLine: [NSString stringWithFormat: @"%@", [stack objectAtIndex: i]]];
    }
    [FCConsole writeLine: @"--------------------- bottom of stack"];
}


#pragma mark -
#pragma mark Operand handling

- (BOOL) isEmpty
{
    return ([stack count] == 0);
}


- (BOOL) hasTwoOperands
{
    return ([stack count] >= 2);
}


- (id) firstOperand
{
    return [stack objectAtIndex: [stack count] - 2];
}


- (id) secondOperand
{
    return [stack objectAtIndex: [stack count] - 1];
}


- (id) topOperand
{
    return [self secondOperand];
}


@end
