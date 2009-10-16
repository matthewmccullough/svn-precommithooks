#!/usr/local/bin/python
#Official Reference: http://svnbook.red-bean.com/en/1.5/svn.reposadmin.create.html
#http://svnbook.red-bean.com/en/1.5/svn.ref.reposhooks.pre-commit.html

"""
Subversion pre-commit hook which currently checks that the commit contains
a commit message to avoid commiting empty changesets which tortoisesvn seems
to have a habbit of committing.

Based on http://svn.collab.net/repos/svn/branches/1.2.x/contrib/hook-scripts/commit-block-joke.py
and hooks/pre-commit.tmpl

Hacked together by Jacques Marneweck <jacques@php.net>
http://www.powertrip.co.za/blog/archives/pre-commit

$Id$
"""

import sys, os, string

SVNLOOK='/usr/local/bin/svnlook'

def main(repos, txn):
    log_cmd = '%s log -t "%s" "%s"' % (SVNLOOK, txn, repos)
    log_msg = os.popen(log_cmd, 'r').readline().rstrip('\n')

    if len(log_msg) < 10:
        sys.stderr.write ("Please enter a commit message which details what has changed during this commit.\n")
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: %s REPOS TXN\n" % (sys.argv[0]))
    else:
        main(sys.argv[1], sys.argv[2])