//
//  ChatBotLogicTests.m
//  ChatBotLogicTests
//
//  Created by Admin on 2/24/12.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#import "ChatBotLogicTests.h"


@implementation ChatBotLogicTests

- (void)setUp
{
    NSLog(@"%@ setUp", self.name);
    lcchatcontroller = [[[CBChatController alloc] init] retain];
    STAssertNotNil(lcchatcontroller, @"Cannot create CBChatController instance");
}

- (void)tearDown
{
    // Tear-down code here.
    
    [lcchatcontroller release];
    NSLog(@"%@ tearDown", self.name);
}

- (void) testHello {
    NSLog(@"%@ start", self.name);   // self.name is the name of the test-case method.
    [[lcchatcontroller bot] respondToChatMessage:@"hello"];
    NSLog(@"%@", [[[lcchatcontroller chatView] textStorage] string]);
    STAssertTrue([[[[lcchatcontroller chatView] textStorage] string] isEqualToString:@"<user> hello\n<Awesomebot> hello"], @"Hello does not work properly");

    NSLog(@"%@ end", self.name);
}

@end
