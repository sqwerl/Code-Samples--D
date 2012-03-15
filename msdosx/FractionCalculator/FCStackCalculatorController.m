//
//  FCStackCalculatorController.m
//  FractionCalculator
//
//  Created by Admin on 1/26/12.
//  Copyright 2012 __MyCompanyName__. All rights reserved.
//

#import "FCStackCalculatorController.h"
#import "FCConsole.h"
#import "Fraction.h"

@implementation FCStackCalculatorController

- (id)init
{
    self = [super init];
    if (self) {
        stack = [[FCStack alloc] init];
    }
    
    return self;
}

- (void) respondToInput: (NSString *) input;
{
    [FCConsole writeLine: input];
    if ([input hasPrefix: @"push"])
    {
        NSString *fractionString = [input substringFromIndex: 5];
        NSUInteger slash = [fractionString rangeOfString: @"/"].location;
        int numer = [[fractionString substringToIndex: slash] intValue];
        int denom = [[fractionString substringFromIndex: slash + 1] intValue];
        Fraction *fraction = [[Fraction alloc] initWithNumerator: numer 
                                                  andDenominator: denom];
        [stack push: fraction];
        [stack print];
    }
    
    if ([input hasPrefix: @"pop"])
    {
        [stack pop];
        [stack print];
    }
    
    if ([input hasPrefix: @"clear"])
    {
        [stack clear];
        [stack print];
    }
    
    if ([input isEqual:@"+"])
    {
        Fraction *fraction1 = [stack firstOperand];
        Fraction *fraction2 = [stack secondOperand];
        Fraction *result = [fraction1 add: fraction2];
        [stack pop];
        [stack pop];
        [stack push: result];
        [stack print];
    }
    
    if ([input isEqual:@"-"])
    {
        Fraction *fraction1 = [stack firstOperand];
        Fraction *fraction2 = [stack secondOperand];
        Fraction *result = [fraction1 subtract: fraction2];
        [stack pop];
        [stack pop];
        [stack push: result];
        [stack print];
    }
    
    if ([input isEqual:@"*"])
    {
        Fraction *fraction1 = [stack firstOperand];
        Fraction *fraction2 = [stack secondOperand];
        Fraction *result = [fraction1 multiply: fraction2];
        [stack pop];
        [stack pop];
        [stack push: result];
        [stack print];
    }
    
    if ([input isEqual:@"/"])
    {
        Fraction *fraction1 = [stack firstOperand];
        Fraction *fraction2 = [stack secondOperand];
        Fraction *result = [fraction1 divide: fraction2];
        [stack pop];
        [stack pop];
        [stack push: result];
        [stack print];
    }
    
    if ([input isEqual:@"invert"])
    {
        Fraction *fraction = [stack topOperand];
        Fraction *result = [fraction inverse];
        [stack pop];
        [stack push: result];
        [stack print];
    }
}

@end
