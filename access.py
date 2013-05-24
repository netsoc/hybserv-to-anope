#!/usr/bin/env python

import re

class chan:
    def __init__(self):
        self.channel = ""
        self.founder = ""

        self.alist = []

    def __str__(self):
	
        retval = ""

        for u in self.alist:

            # extract nick from hostmask 
            if u[0][0] == "*":
                split = u[0].split('*')
                
                if split[1] == "!":
                    split[1] = split[2]
                
                if split[1][0] == '!':
                    split[1] = split[1][1:]

                split[1] = split[1].split('@')[0]

                u[0] = split[1]

            if u[0] != self.founder:
                retval += "access " + self.channel + " add " + u[0] + " " + u[1] + "\n"

        return retval 


def get_chans(filename):
    f = open(filename, 'r')

    chan_str = []

    for line in f.readlines():
        #line = line[:-1]

        if line[0] == ';':
            continue

        if line[0:2] != "->":
            #print line.split(' ')
            chan_str.append([line])
        else:
            chan_str[-1].append(line)

    f.close()

    #print chan_str
    chans = []

    for c_str in chan_str:
        c = chan()
        
        for line in c_str:
            line = line[:-1]

            if line == "":
                continue
            

            if line[0:2] != "->":
                split = line.split(' ')
                c.channel = split[0]
            
            else:
                if line[0:8] == "->ACCESS":
                    split = line.split(' ')
                    c.alist.append([split[1], split[2]])

                elif line[0:6] == "->FNDR":
                    c.founder = re.escape(line.split(' ')[1])
                
        chans.append(c)

    return chans




for c in get_chans("chan.db"):
    print str(c)
