//
//  RSSFeedWindowController.m
//  RSSReader
//
//  Created by Kevin Jorgensen on 8/7/11.
//  Copyright 2011 Kevin Jorgensen. All rights reserved.
//

#import "RSSFeedWindowController.h"


@implementation RSSFeedWindowController

@synthesize tableView;
@synthesize feedName, feedURL;


#pragma mark -
#pragma mark NSTableViewDataSource

- (NSInteger) numberOfRowsInTableView: (NSTableView *) tableView
{
    return [rssEntries count];
}


- (id) tableView: (NSTableView *) tableView objectValueForTableColumn: (NSTableColumn *) tableColumn row: (NSInteger) row
{
    NSDictionary *entry = [rssEntries objectAtIndex: row];
    NSString *header = [[tableColumn headerCell] title];
    
    NSDictionary *keyMap = [NSDictionary dictionaryWithObjectsAndKeys: @"title", @"Title", @"link", @"Link", @"description", @"Description", @"pubDate", @"Publication Date", nil];
    
    return [entry objectForKey: [keyMap objectForKey: header]];
}


#pragma mark -
#pragma mark NSURLConnectionDelegate

- (void) connection: (NSURLConnection *) connection didReceiveResponse: (NSURLResponse *) response
{
    [resultData setLength: 0];
}


- (void) connection: (NSURLConnection *) connection didReceiveData: (NSData *) data
{
    [resultData appendData: data];
}


- (void) connection: (NSURLConnection *) connection didFailWithError: (NSError *) error
{
    [resultData release];
    [connection release];
    
    [[NSApplication sharedApplication] presentError: error];
}


- (void) connectionDidFinishLoading: (NSURLConnection *) connection
{
    NSXMLParser *parser = [[NSXMLParser alloc] initWithData: resultData];
    [resultData release];
    [connection release];
    
    parser.delegate = self;
    [parser parse];
}


#pragma mark - NSWindowDelegate

- (BOOL) windowShouldClose: (id) sender
{
    NSAlert *alert = [NSAlert alertWithMessageText: @"This window has unsaved changes."
                                     defaultButton: @"Save"
                                   alternateButton: @"Cancel"
                                       otherButton: @"Don't Save"
                         informativeTextWithFormat: @"Are you sure you want to close?"];
    
    [alert beginSheetModalForWindow: self.window modalDelegate: self didEndSelector: @selector(alertDidEnd:returnCode:contextInfo:) contextInfo: nil];
    
    return NO;
}


- (void) alertDidEnd: (NSAlert *) alert returnCode: (NSInteger) returnCode contextInfo: (void *) contextInfo
{
    if (returnCode == NSAlertOtherReturn)
        [self.window close];
}


#pragma mark - NSXMLParserDelegate

- (void) parserDidStartDocument: (NSXMLParser *) parser
{
    if (rssEntries)
        [rssEntries release];
    
    rssEntries = [[NSMutableArray alloc] init];
    
    tagStack = [[NSMutableArray alloc] init];
}


- (void) parser: (NSXMLParser *) parser 
didStartElement: (NSString *) elementName 
   namespaceURI: (NSString *) namespaceURI 
  qualifiedName: (NSString *) qName
     attributes: (NSDictionary *) attributeDict
{
    [tagStack addObject: elementName];
    
    if ([elementName isEqualToString: @"item"])
    {
        currentEntry = [[NSMutableDictionary alloc] init];
    }
}


- (void) parser: (NSXMLParser *) parser foundCharacters: (NSString *) string
{
    NSString *currentTag = [tagStack lastObject];
    
    if ([[NSArray arrayWithObjects: @"title", @"link", @"description", @"pubDate", nil] containsObject: currentTag])
    {
        if ([currentEntry objectForKey: currentTag])
        {
            [currentEntry setObject: [[currentEntry objectForKey: currentTag] stringByAppendingString: string] forKey: currentTag];
        }
        else
        {
            [currentEntry setObject: string forKey: currentTag];
        }
    }
}


- (void) parser: (NSXMLParser *) parser 
  didEndElement: (NSString *) elementName
   namespaceURI: (NSString *) namespaceURI
  qualifiedName: (NSString *) qName
{
    [tagStack removeLastObject];
    
    if ([elementName isEqualToString: @"item"])
    {
        [rssEntries addObject: currentEntry];
        
        [currentEntry release];
        currentEntry = nil;
    }
}


- (void) parserDidEndDocument: (NSXMLParser *) parser
{
    [parser release];
    [tagStack release];
    
    [tableView reloadData];
}


#pragma mark -

- (void) setFeedName: (NSString *) _feedName
{
    if (feedName)
        [feedName release];
    
    feedName = [_feedName retain];
    
    [self.window setTitle: feedName];
}


- (void) setFeedURL: (NSURL *) _feedURL
{
    if (feedURL)
        [feedURL release];
    
    feedURL = [_feedURL retain];
    
    NSURLRequest *request = [NSURLRequest requestWithURL: feedURL];
    
    NSURLConnection *connection = [[NSURLConnection alloc] initWithRequest: request delegate: self];
    
    if (connection)
    {
        resultData = [[NSMutableData alloc] init];
    }
    else
    {
        NSError *error = [[NSError alloc] initWithDomain: @"RSSReaderErrorDomain" 
                                                    code: 1 
                                                userInfo: [NSDictionary dictionaryWithObject: @"Could not connect to feed" forKey: NSLocalizedDescriptionKey]];
        [[NSApplication sharedApplication] presentError: error];
        [error release];
    }
}


#pragma mark -
#pragma mark Memory lifecycle

- (id) initWithWindow: (NSWindow *) window
{
    self = [super initWithWindow: window];
    
    if (self)
    {
        
    }
    
    return self;
}


- (void) dealloc
{
    [feedName release];
    [feedURL release];
    
    [tableView release];
    
    [super dealloc];
}


#pragma mark -

- (void) windowDidLoad
{
    [super windowDidLoad];
    
    // Implement this method to handle any initialization after your window controller's window has been loaded from its nib file.
}


@end
