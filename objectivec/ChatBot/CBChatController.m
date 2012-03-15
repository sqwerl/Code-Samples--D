//
//  CBChatController.m
//  ChatBot
//
//  Created by Ian Henderson on 01.27.09.
//  Copyright 2009 __MyCompanyName__. All rights reserved.
//

#import "CBChatController.h"
#import "LCChatBot.h"

@implementation CBChatController
@synthesize bot;
@synthesize chatView;
- (id)init
{
  if (![super init]) {
    return nil;
  }
  
  bot = [[LCChatBot alloc] init]; // replace this with your chatbot class
  [bot setChatController:self];
  
  return self;
}

- (void)dealloc
{
  [bot release];
  [super dealloc];
}

- (void)appendText:(NSString *)text withAttributes:(NSDictionary *)attributes
{
  [[chatView textStorage] appendAttributedString:[[[NSAttributedString alloc] initWithString:text attributes:attributes] autorelease]];
}

- (void)appendMessage:(NSString *)messageString fromScreenName:(NSString *)screenName withColor:(NSColor *)color
{
  if (![[[chatView textStorage] string] isEqualToString:@""]) {
    [self appendText:@"\n" withAttributes:nil];
  }
  [self appendText:[NSString stringWithFormat:@"<%@>", screenName] withAttributes:[NSDictionary dictionaryWithObject:color forKey:NSForegroundColorAttributeName]];
  [self appendText:@" " withAttributes:nil];
  [self appendText:messageString withAttributes:nil];
}

- (IBAction)sendMessage:(id)sender
{
  [self appendMessage:[sender stringValue] fromScreenName:@"user" withColor:[NSColor redColor]];
  [bot respondToChatMessage:[sender stringValue]];
  [sender setStringValue:@""];
}

@end
