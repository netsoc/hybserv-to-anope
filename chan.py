#!/usr/bin/env python

import re

class chan:
    def __init__(self):
        self.autodeop = "999"
        self.autovoice = "998"
        self.cmdvoice = "997"
        self.access = "996"
        self.cmdinvite = "995"
        self.autohalfop = "994"
        self.cmdhalfop = "993"
        self.autoop = "992"
        self.cmdop = "991"
        self.cmdunban = "990"
        self.autokick = "989"
        self.cmdclear = "988"
        self.set = "987"
        
        self.channel = "#lol"
        self.founder = ""
        self.pw = ""
        self.founded = "0"
        self.successor = ""
        self.topic = ""

    def __str__(self):
        retval = "INSERT INTO `anope_cs_levels` (channel, position, level) VALUES \n" +\
            "('" + self.channel + "',35,-10000),\n" +\
            "('" + self.channel + "',34,-10000),\n" +\
            "('" + self.channel + "',33,-10000),\n" +\
            "('" + self.channel + "',32,-10000),\n" +\
            "('" + self.channel + "',31,-10000),\n" +\
            "('" + self.channel + "',30,-10000),\n" +\
            "('" + self.channel + "',29,-10000),\n" +\
            "('" + self.channel + "',28,-10000),\n" +\
            "('" + self.channel + "',27,-10000),\n" +\
            "('" + self.channel + "',26," + self.cmdhalfop + "),\n" +\
            "('" + self.channel + "',25," + self.cmdhalfop + "),\n" +\
            "('" + self.channel + "',24," + self.cmdop + "),\n" +\
            "('" + self.channel + "',23,-10000),\n" +\
            "('" + self.channel + "',22," + self.autohalfop + "),\n" +\
            "('" + self.channel + "',21,-10000),\n" +\
            "('" + self.channel + "',20," + self.cmdvoice + "),\n" +\
            "('" + self.channel + "',19," + self.cmdvoice + "),\n" +\
            "('" + self.channel + "',18,-10000),\n" +\
            "('" + self.channel + "',17,-10000),\n" +\
            "('" + self.channel + "',16,-10000),\n" +\
            "('" + self.channel + "',15,-10000),\n" +\
            "('" + self.channel + "',14,-10000),\n" +\
            "('" + self.channel + "',13,-10000),\n" +\
            "('" + self.channel + "',12,-10000),\n" +\
            "('" + self.channel + "',11," + self.access + "),\n" +\
            "('" + self.channel + "',10,-10000),\n" +\
            "('" + self.channel + "',9," + self.cmdclear + "),\n" +\
            "('" + self.channel + "',8," + self.access + "),\n" +\
            "('" + self.channel + "',7," + self.cmdop + "),\n" +\
            "('" + self.channel + "',6," + self.autovoice + "),\n" +\
            "('" + self.channel + "',5," + self.autodeop + "),\n" +\
            "('" + self.channel + "',4," + self.autoop + "),\n" +\
            "('" + self.channel + "',3," + self.cmdunban + "),\n" +\
            "('" + self.channel + "',2," + self.set + "),\n" +\
            "('" + self.channel + "',1," + self.autokick + "),\n" +\
            "('" + self.channel + "',0," + self.cmdinvite + ");\n"

        retval += "INSERT INTO `anope_cs_info` (name, founder, successor, founderpass, descr, url, email, " +\
            "last_topic, last_topic_setter, forbidby, forbidreason, mlock_key, mlock_flood, mlock_redirect, " +\
            "entry_message, time_registered) VALUES ('" + self.channel + "', '" + self.founder + "', " +\
            "'" + self.successor + "', " +\
            "'" + self.pw + "\\0\\0\\0\\0\\0\\0\\0XXX\\0\\0\\0\\0\\0\\0\\0\\0\\0', '" + self.channel + "', " +\
            "'', '', '" + self.topic + "', '', '', '', '', '', '', '', " + self.founded + ");\n"

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
                c.channel = re.escape(split[0])
                c.founded = split[2]
            
            else:
                if line[0:6] == "->ALVL":
                    split = line.split(' ')
                    c.autodeop = split[1]
                    c.autovoice = split[2]
                    c.cmdvoice = split[3]
                    c.access = split[4]
                    c.cmdinvite = split[5]
                    c.autohalfop = split[6]
                    c.cmdhalfop = split[7]
                    c.autoop = split[8]
                    c.cmdop = split[9]
                    c.cmdunban = split[10]
                    c.autokick = split[11]
                    c.cmdclear = split[12]
                    c.set = split[13]
                
                elif line[0:6] == "->FNDR":
                    c.founder = line.split(' ')[1]
                
                elif line[0:6] == "->PASS":
                    c.pw = line.split(' ')[1]
                
                elif line[0:11] == "->SUCCESSOR":
                    c.successor = line.split(' ')[1]
                
                elif line[0:9] == "->TOPIC :":
                    c.topic =  re.escape(line[9:])



        chans.append(c)

    return chans




for c in get_chans("chan.db"):
    print str(c)
