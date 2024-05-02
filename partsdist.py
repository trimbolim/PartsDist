#!/usr/bin/python3
import os
import argparse


parts={
'alto': {},
'tenor1': {},
'tenor2': {'chairs': [1,2]},
'trumpet': {'chairs': [1,2,3,4,5]},
'trombone': [1,2,3,4],
'guitar': [],
'piano': [],
'bass': [],
'drums': [],
'vocal': []}

#print (parts)

parser = argparse.ArgumentParser()
parser.add_argument('outfile', type=str)
parser.add_argument('--in-dir', type=str, required=True)

args = parser.parse_args()

infiles = os.listdir(args.in_dir)

for infile in infiles:
    for part in parts:
        if part in infile.lower():
            #print ("is " + part + " in " + infile)
            #print ("and len is " + str(len(part)))
            if len(parts[part]) == 0:
                print (infile + " is the " + part + " part")
            else:
                for chair in parts[part]:
                    pos_of_string = infile.lower().find(part)
                    #print (part + " found at pos " + str(pos_of_string))
                    if str(chair) in infile[pos_of_string:]:
                        print (infile + " is the " + part + str(chair) + " part")

#print (args)
#print (infiles)
