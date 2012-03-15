//
//  CBChatBot.m
//  ChatBot
//
//  Created by Ian Henderson on 01.27.09.
//  Copyright 2009 __MyCompanyName__. All rights reserved.
//

#import "CBChatBot.h"
#import "CBChatController.h"

@implementation CBChatBot

- (void)setChatController:(CBChatController *)ctrlr
{
  controller = ctrlr;
}
- (void)sendMessage:(NSString *)chatMessage
{
  [controller appendMessage:chatMessage fromScreenName:[[self class] screenName] withColor:[NSColor blueColor]];
}

- (void)respondToChatMessage:(NSString *)chatMessage
{
  [self sendMessage:[NSString stringWithFormat:@"you said \"%@\"", chatMessage]];
}

+ (NSString *)screenName
{
  return @"default bot";
}

@end
