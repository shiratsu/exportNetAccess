#!/usr/bin/env python

import lldb
import commands
import requests


def processGet(debugger, command, result, internal_dict):
    r = requests.get(command)
    print(r)
    print(r.text)


def __lldb_init_module(debugger,internal_dict):
    debugger.HandleCommand("command script add -f exportNetAccess.processGet exportGetAccess")
    print "exportNetAccess command enabled."
