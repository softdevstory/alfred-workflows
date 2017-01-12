# -*- coding: utf-8 -*-
#
# developer@softdevstory.net, 2017

import sys
import feedparser
from workflow import Workflow3, ICON_WEB

def get_feed_data():
    return feedparser.parse('https://blog.weirdx.io/feed')

def main(wf):

    feed = wf.cached_data('feed', get_feed_data, max_age=60)
    for item in feed.entries:
        wf.add_item(item.title,
                    item.link,
                    quicklookurl=item.link,
                    icon=ICON_WEB,
                    valid=True,
                    arg=item.link)
                    
    wf.send_feedback()
    

if __name__ == '__main__':
    wf = Workflow3()        
    sys.exit(wf.run(main))
