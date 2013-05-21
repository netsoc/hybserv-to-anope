Hybserv to anope converter

This consists of a unixcrypt / sha1 module for anope (to support hybserv password hashes), and some tools for
porting the db.
The unixcrypt hashes are put into the anope db, but when you register a new nick, or change your password,
the normal sha1 module hashing is used.
The sample services.conf presented here attempts to match the default behaviour of hybserv.


To use:
    Stop anope.
    First make sure you have anope running using mysql.
    Then, run chan.py and nick.py in a folder containing chan.db and nick.db from hybserv.
    Paste the output sql into mysql.
    In your anope dir, rm *.db (everything is still in mysql, so this is ok).
    Start anope.
    Done.
