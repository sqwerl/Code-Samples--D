//
//  FCConsole.h
//  FractionCalculator
//
//  Created by Kevin Jorgensen on 7/16/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface FCConsole : NSObject

/** Output "> " to standard output */
+ (void) writePrompt;

/** Read in a line from standard input */
+ (NSString *) readLine;

/** Output a line to standard output */
+ (void) writeLine: (NSString *) line;

@end
