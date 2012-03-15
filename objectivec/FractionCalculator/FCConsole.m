//
//  FCConsole.m
//  FractionCalculator
//
//  Created by Kevin Jorgensen on 7/16/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import "FCConsole.h"

@implementation FCConsole

+ (void) writePrompt
{
    putchar('>');
    putchar(' ');
}

+ (NSString *) readLine
{
    char buffer[1024];
    fgets(buffer, 1024, stdin);
    NSString *str = [NSString stringWithUTF8String:buffer];
    return [str substringToIndex: [str length] - 1]; /* remove the newline at the end of the string */
}

+ (void) writeLine: (NSString *) line
{
    puts([line UTF8String]);
}

@end
