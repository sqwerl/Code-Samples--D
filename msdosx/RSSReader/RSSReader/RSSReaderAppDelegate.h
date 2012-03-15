//
//  RSSReaderAppDelegate.h
//  RSSReader
//
//  Created by Kevin Jorgensen on 8/7/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import <Cocoa/Cocoa.h>

@interface RSSReaderAppDelegate : NSObject <NSApplicationDelegate>
{
    NSWindow *_window;
    
    NSTextField *feedNameEntryField, *feedURLEntryField;
}

@property (nonatomic, retain) IBOutlet NSWindow *window;
@property (nonatomic, retain) IBOutlet NSTextField *feedNameEntryField, *feedURLEntryField;


- (IBAction) openFeed: (id) sender;

- (IBAction) open: (NSButton *) sender;

@end
