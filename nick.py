#!/usr/bin/env python

import re

class user:
    
    def __init__(self):
        self.name = ""
        self.pw = ""
        self.seen = "0"
        self.registered = "0"
        self.link = ""
    
    def __str__(self):
        #return "Name: " + self.name + ", Pw: " + self.pw + ", Seen: " + self.seen + ", Regd: " + self.registered + ", Link: " + self.link

        alias = "INSERT INTO `anope_ns_alias` (display, nick, last_usermask, last_realname, last_quit, time_registered, last_seen) VALUES ('"
        if(self.link):
            alias += self.link
        else:
            alias += self.name

        alias += "', '" + self.name + "',  '', '', '', " + self.registered + ", " + self.seen + ");"
        
        if(not self.link):
            access = "INSERT INTO `anope_ns_access` (display, access) VALUES ('" + self.name + "','');"

            core = "INSERT INTO `anope_ns_core` (display, pass, email, url, greet) VALUES ('" + self.name + "', '" + self.pw + "\\0\\0\\0\\0\\0\\0\\0XXX\\0\\0\\0\\0\\0\\0\\0\\0\\0', '', '', '');"
        else:
            access = ""
            core = ""



        return access + "\n" + alias + "\n" + core + "\n"




def get_users(filename):
    f = open(filename, 'r')

    users_str = []

    for line in f.readlines():
        #line = line[:-1]

        if line[0] == ';':
            continue

        if line[0:2] != "->":
            #print line.split(' ')
            users_str.append([line])
        else:
            users_str[-1].append(line)

    f.close()


    users = []

    for user_str in users_str:
        u = user()
        for line in user_str:
            line = line[:-1]

            if line[0:2] != "->":
               split = line.split(' ')
               u.name = split[0]

               u.seen = split[3]
               u.registered = split[2]

            else:
                if line[0:6] == "->PASS":
                    u.pw = line.split(' ')[1]

                if line[0:6] == "->LINK":
                    u.link = re.escape(line.split(' ')[1])
                        
        users.append(u)
    
    return users


for u in get_users('nick.db'):
    print str(u)





