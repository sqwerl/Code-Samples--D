//
//  Fraction.h
//  FractionCalculator
//
//  Created by Kevin Jorgensen on 7/16/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <Foundation/Foundation.h>

int GCD(int a, int b);

@interface Fraction : NSObject
{
    int numerator;
    int denominator;
}

- (int) numerator;
- (int) denominator;

- (id) initWithNumerator: (int) numer andDenominator: (int) denom;

- (Fraction *) add: (Fraction *) otherFraction;
- (Fraction *) subtract: (Fraction *) otherFraction;
- (Fraction *) multiply: (Fraction *) otherFraction;
- (Fraction *) divide: (Fraction *) otherFraction;

- (void) reduce;

- (Fraction *) inverse;

@end
