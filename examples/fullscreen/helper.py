#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs

def getId(path='.', filename = 'id.lst', condition = True):
    filePath = os.path.join(path, filename)
    if os.path.isfile(filePath):
        vpFile = open(filePath, 'r')
    else:
        print('Error! id.lst does not exist or is not accessable.')
        quit()
    
    tmp = []
    line = '*'
    while '*' in line:
        line = vpFile.readline()
        tmp.append(line)
    
    if line == '':
        print('Error! No number available.')
        quit()
    
    infos = line.split()
    id = int(infos[0])
    if (condition):
        cond = str(infos[1])
    
    tmp.pop()
    if (condition):
        nline = infos[0] + ' ' + infos[1] + ' *\n'
    else:
        nline = infos[0] + ' *\n'
    tmp.append(nline)

    while line != '':
        line = vpFile.readline()
        tmp.append(line)

    vpFile.close()
    tmpPath = os.path.join(path,  filename +'.tmp')
    tmpFile = open(tmpPath,'w')
    tmpFile.writelines(tmp)
    tmpFile.close()    
    os.remove(filePath)
    os.rename(tmpPath, filePath)
    
    if (condition):
        return id, cond
    else:
        return id


def writeTrials(header, list, path, expName, id, sep = "\t", part = '', extension = '.rtd', mode = 'w', print_header = True):
    # write data to file
    output = []
    if (print_header):
        output.append(header)
    for trial in list:
        line = map(trial.get, header)
        output.append(line)
    
    if (part != ''):
        part = part + '_'

    outfileLN = os.path.join(path, expName + '_' + part + str(id) + extension)
    outfileL = codecs.open(outfileLN, mode, encoding='utf-8')
    
    for line in output:
        for i in range(len(line)):
            outfileL.write(unicode(line[i]))
            outfileL.write(sep)
        outfileL.write('\n')
    outfileL.close()

def writeDemographics(header, dict, path, expName, id, condition, sep = "\t", extension = '_demographics.dat', mode = 'a'):
    
    data = map(dict.get, header)
    
    outfileLN = os.path.join(path, expName + extension)
    outfile = codecs.open(outfileLN, mode, encoding='utf-8')
    
    outfile.write(unicode(id))
    outfile.write(sep)
    outfile.write(unicode(condition))
    outfile.write(sep)
    for dat in data:
        outfile.write(unicode(dat))
        outfile.write(sep)
    outfile.write('\n')
    outfile.close()

def writeComments(comment, path, id, expName):
    if (comment["comment"] != ""):
        if not(os.path.exists(os.path.join(path, "comments"))):
            os.mkdir(os.path.join(path, "comments"))
        commentFile = codecs.open(os.path.join(path, "comments", (expName + "_comment_" + str(id) + ".txt")) ,'w', encoding='utf-8')
        commentFile.write(unicode(comment["comment"]))
        commentFile.write("\n")
        commentFile.close()
    
    