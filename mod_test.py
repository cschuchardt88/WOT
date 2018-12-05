
''' import WoT
import WWISE
import BigWorld '''
''' import Keys
import Account
import Vehicle
import CommandMapping
import Settings
import helpers
import account_helpers
import constants
import gui.battle_control
import gui.battle_control.event_dispatcher as gui_event_dispatcher

from PlayerEvents import g_playerEvents
from account_helpers import * '''

import os, Keys
import BigWorld, ResMgr

BigWorld.callback(0.2, lambda : mod_handlekeys())

def init():
    print "mod_init()"
    #g_playerEvents.onAvatarReady += mod_AvatarReady # in game
    #print help(BigWorld)
    #print help(ResMgr)
#    SetDebugInfoOnBigWorld()
    print "mod_init() done"

''' def mod_AvatarReady():
    print "mod_AvatarReady()"
    mod_handlekeys() '''
    

def mod_handlekeys():
    
    if BigWorld.isKeyDown(Keys.KEY_HOME):
        print "Magic key was pressed!"
        readGameDefineFiles()
        return

    BigWorld.callback(0.2, lambda : mod_handlekeys())

#def SetDebugInfoOnBigWorld():
#    import pydevd
#    bwdebug.INFO_MSG('PyDevD connecting to %s:%d' % ("127.0.0.1", 5678))
#    pydevd.settrace(host="127.0.0.1", port=5678, suspend=False, stdoutToServer=True, stderrToServer=True, trace_only_current_thread=False)
#    #threading.currentThread().__pydevd_id__ = BigWorld.component


def readGameDefineFiles():
    gPath = "E:\wot"
    #fileName = "precache.xml"
    #section = ResMgr.openSection(fileName)
    section = ResMgr.root
    #section = ResMgr.openSection("")
    #print "ResMgr.Path ", ResMgr.resolveToAbsolutePath(fileName)
    print "Section type (%s)" % (type(section))
    print "Loading Section (%s)" % (section.name)
    print "Dumping game resources to (%s)" % (gPath)

    if (section is None):
        return

    def WriteFileContent(subsec, pPath):
        with open(pPath, "ab") as f:
            if subsec.asWideString:
                print "Writting WideString for (%s)" % (pPath)
                f.write("%s %s\n" % (subsec.name, subsec.asWideString))
            elif subsec.asString:
                print "Writting String for (%s)" % (pPath)
                f.write("%s %s\n" % (subsec.name, subsec.asString))
            elif subsec.asBlob:
                print "Writting Blob for (%s)" % (pPath)
                f.write("%s %s\n" % (subsec.name, subsec.asBlob))
            elif subsec.asMatrix:
                print "Writting Matrix for (%s)" % (pPath)
                f.write("%s %s\n" % (subsec.name, subsec.asMatrix))
            elif subsec.asVector2:
                print "Writting Vector2 for (%s)" % (pPath)
                f.write("%s %s\n" % (subsec.name, subsec.asVector2))
            elif subsec.asVector3:
                print "Writting Vector3 for (%s)" % (pPath)
                f.write("%s %s\n" % (subsec.name, subsec.asVector3))
            elif subsec.asVector4:
                print "Writting Vector4 for (%s)" % (pPath)
                f.write("%s %s\n" % (subsec.name, subsec.asVector4))
            else:
                print "Content Unknown for (%s)"

        f.close()
        return

    def getSubSec(subsec, pPath, sPath = ""):
        #if sPath == "" and subsec.name != "root":
        #    if subsec.name == "scripts":
        #        return
        #    if subsec.name == "content":
        #        return
        #    if subsec.name == "system":
        #        return
        #    if subsec.name == "packages":
        #        return
        #    if subsec.name == "vehicles":
        #        return
        #    if subsec.name == "maps":
        #        return

        if sPath != "root" and subsec.name != "root":
            if sPath == "":
                sPath = subsec.name
            else:
                sPath += "/" + subsec.name

        isFile = ResMgr.isFile(sPath)
        isDir = ResMgr.isDir(sPath)

        if isFile:
            print "in Section (%s) - File" % (sPath)
            pPath += "\\" + subsec.name
            if os.path.exists(pPath) == False:
                with open(pPath, "ab") as f:
                    if subsec.asBinary:
                        f.write(subsec.asBinary)
                    elif subsec.asWideString:
                        f.write(subsec.asWideString)
                    elif subsec.asString:
                        f.write(subsec.asString)
                f.close()

                print "File (%s) created" % (pPath)
        elif isDir:
            print "in Section (%s) - Directory" % (sPath)
            pPath += "\\" + subsec.name
            if os.path.exists(pPath) == False:
                os.mkdir(pPath)
                print "Directory (%s) created" % (pPath)
        else:
            pass
            #print "in Section (%s) - Content" % (sPath)
            #if subsec.name == "root":
            #    WriteFileContent(subsec, pPath + "\\wot_file")
            #else:
            #    WriteFileContent(subsec, pPath)

        subchilds =  subsec.items()
        if len(subchilds) != 0:
            for (keyname, sec) in subchilds:
                getSubSec(sec, pPath, sPath)
        return
        

    getSubSec(section, gPath)
    print "Finished dumping game resource files!"
    return

