//
//  RSSReaderAppDelegate.m
//  RSSReader
//
//  Created by Kevin Jorgensen on 8/7/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import "RSSReaderAppDelegate.h"

#import "RSSFeedWindowController.h"

@implementation RSSReaderAppDelegate

@synthesize window = _window;
@synthesize feedNameEntryField, feedURLEntryField;


#pragma mark -
#pragma mark Memory management

- (void) dealloc
{
    [_window release];
    
    [feedNameEntryField release];
    [feedURLEntryField release];
    
    [super dealloc];
}


#pragma mark -
#pragma mark NSApplicationDelegate

- (void)applicationDidFinishLaunching:(NSNotification *)aNotification
{
    [_window makeKeyAndOrderFront: self];
}


#pragma mark -

- (void) openFeed: (id) sender
{
    if (![_window isVisible])
        [_window makeKeyAndOrderFront: self];
}


- (void) open: (NSButton *) sender
{
    NSString *feedName = [feedNameEntryField stringValue];
    NSString *feedURL  = [feedURLEntryField stringValue];
    
    RSSFeedWindowController *windowController = [[RSSFeedWindowController alloc] initWithWindowNibName: @"RSSFeedWindow"];
    windowController.feedName = feedName;
    windowController.feedURL = [NSURL URLWithString: feedURL];
    [windowController.window makeKeyAndOrderFront: self];
    
    /* Reset the window and close it */
    [feedNameEntryField setStringValue: @""];
    [feedURLEntryField setStringValue: @""];
    [_window makeFirstResponder: feedNameEntryField];
    
    [_window orderOut: self];
}

@end
