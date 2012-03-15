//
//  RSSFeedWindowController.h
//  RSSReader
//
//  Created by Kevin Jorgensen on 8/7/11.
//  Copyright 2011 Kevin Jorgensen. All rights reserved.
//

#import <Cocoa/Cocoa.h>


@interface RSSFeedWindowController : NSWindowController <NSTableViewDataSource, NSURLConnectionDelegate, NSWindowDelegate, NSXMLParserDelegate>
{
    NSString *feedName;
    NSURL *feedURL;
   
    NSMutableArray *rssEntries;
    
    NSMutableData *resultData;
    NSMutableArray *tagStack;
    NSMutableDictionary *currentEntry;
}


@property (nonatomic, retain) IBOutlet NSTableView *tableView;

@property (nonatomic, retain) NSString *feedName;
@property (nonatomic, retain) NSURL *feedURL;

@end
