#!/usr/bin/env python

import os
import sys
import json
from collections import defaultdict

smw_jsonfile = sys.argv[1]
dat = json.load(open(smw_jsonfile))

people = sorted(dat['results'].keys())
# for user in people:
#     for exper in dat['results'][user]['printouts']['On experiment']:
#         exper = exper['fulltext']
#         experiments.add(exper)
#         userexp[user].append(exper)
# experiments = list(experiments)
# experiments.sort()


print '''drop table Author;
CREATE TABLE Author (
  AuthorID int(11) NOT NULL auto_increment,
  FirstName varchar(32) NOT NULL default '',
  MiddleInitials varchar(16) default NULL,
  LastName varchar(32) NOT NULL default '',
  InstitutionID int(11) NOT NULL default '0',
  Active int(11) default '1',
  TimeStamp timestamp NOT NULL,
  PRIMARY KEY  (AuthorID),
  KEY Name (LastName)
) Engine=MyISAM;
'''

for user in people:
    first,last = user.split(' ',1)
    print "insert into Author set FirstName='%s',LastName='%s',InstitutionID=1,Active=1;" % (first,last)



