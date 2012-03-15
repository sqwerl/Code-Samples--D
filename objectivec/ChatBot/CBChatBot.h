//
//  CBChatBot.h
//  ChatBot
//
//  Created by Ian Henderson on 01.27.09.
//  Copyright 2009 __MyCompanyName__. All rights reserved.
//

#import <Cocoa/Cocoa.h>

@class CBChatController;

@interface CBChatBot : NSObject {
@public
  CBChatController *controller;
}

// do not override
- (void)setChatController:(CBChatController *)controller;
- (void)sendMessage:(NSString *)chatMessage;

// override these
- (void)respondToChatMessage:(NSString *)chatMessage;
+ (NSString *)screenName;

@end
