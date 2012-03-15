//
//  LCChatBot.m
//  ChatBot
//
//  Created by Admin on 2/1/12.
//  Copyright 2012 __MyCompanyName__. All rights reserved.
//

#import "LCChatBot.h"

@implementation LCChatBot

- (id)init
{
    self = [super init];
    if (self) {
        // Initialization code here.
    }
    
    return self;
}

+ (NSString *)screenName
{
    return @"Awesomebot";
}


- (void) timerTriggered: (NSTimer *)timer
{
    [self sendMessage: @"ding!"];
}

- (void) respondToChatMessage: (NSString *) chatMessage
{
    if([chatMessage isEqual: @"hello"]){
        [self sendMessage: @"hello"];
    }
    if([chatMessage isEqual: @"date"]){
        [self sendMessage: [[NSDate date] description]];
    }
    if([chatMessage hasPrefix: @"remember"]){
        rememberedString = [chatMessage retain];
    }
    if([chatMessage isEqual: @"recall"]){
        [self sendMessage: rememberedString];
    }
    if([chatMessage hasPrefix: @"timer"]){
        
        [NSTimer scheduledTimerWithTimeInterval:[[chatMessage substringFromIndex:6] floatValue] target:self selector:@selector(timerTriggered:) userInfo:nil repeats:NO];
    }
    
}

@end
