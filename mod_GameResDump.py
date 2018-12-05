
import os, Keys
import BigWorld

print 'Setting up hotkeys'
BigWorld.callback(0.2, lambda : mod_handleHotkeys())

def init():
    print 'Called init() function of mod.'

def mod_handleHotkeys():
    if BigWorld.isKeyDown(Keys.KEY_HOME):
        print 'Magic key was pressed!'
        dumpRes()
        return
    
    BigWorld.callback(0.2, lambda : mod_handleHotkeys())

def dumpRes():
    #ResMgr.root.isAttribute
    import ResMgr

    def buildNodeString(Section, f):
        if Section.asBlob:
            f.write(Section.asString)
        elif Section.asBool:
            f.write('%d' % (Section.asBool))
        elif Section.asFloat:
            f.write('%f' % (Section.asFloat))
        elif Section.asInt:
            f.write('%d' % (Section.asInt))
        elif Section.asInt64:
            f.write('%d' % (Section.asInt64))
        elif Section.asMatrix:
            f.write(Section.asString)
        elif Section.asVector2:
            f.write(Section.asString)
        elif  Section.asVector3:
            f.write(Section.asString)
        elif Section.asVector4:
            f.write(Section.asString)
        elif Section.asString:
            f.write(Section.asString)

        for (keyName, SubSection) in Section.items():
            f.write('<%s>\n' % (SubSection.name))
            buildNodeString(SubSection, f)
            f.write('</%s>\n' % (SubSection.name))


    def buildSubSectionNodes(Section, pPath, sPath = ''):
        ''' if sPath == 'content':
            return
        elif sPath == 'packages':
            return
        elif sPath == 'maps':
            return
        elif sPath == 'system/maps':
            return
        elif sPath == 'vehicles':
            return
        elif sPath == 'objects':
            return '''

        if Section.name != 'root':
            if sPath == '':
                sPath = Section.name
            else:
                sPath += '/%s' % (Section.name)

        isFile = ResMgr.isFile(sPath)
        isDir = ResMgr.isDir(sPath)
        subItems = Section.items()

        print 'in Section (%s)' % (sPath)

        if isFile:
            pPath += '\\%s' % (Section.name)
            if os.path.exists(pPath) == False:
                with open(pPath, 'wb') as f:
                    if len(subItems) == 0:
                        binStr = Section.asBinary
                        if binStr:
                            f.write(binStr)
                    else:
                        f.write('<%s>\n' % (Section.name))
                        buildNodeString(Section, f)
                        f.write('</%s>\n' % (Section.name))
                    print 'File (%s) created' % (pPath)
        elif isDir:
            pPath += '\\%s' % (Section.name)
            if os.path.exists(pPath) == False:
                os.mkdir(pPath)
                print 'Directory (%s) created' % (pPath)

        for (keyName, sec) in subItems:
            buildSubSectionNodes(sec, pPath, sPath)

        ResMgr.purge(sPath)

    print 'Dumping root section of resources . . .'
    buildSubSectionNodes(ResMgr.openSection(''), 'E:\\wot')
    print 'Dump Finished!'