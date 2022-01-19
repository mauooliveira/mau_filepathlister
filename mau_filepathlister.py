#--------------------------------------------------
# mau_filepathlister.py
# version: 1.0.0
# last updated: 19.01.22 (DD.MM.YY)
#--------------------------------------------------
#BenMcEwans Python101 Course
#--------------------------------------------------

import nuke
import os

def fileLister():
	print "\n\nNuke Script: " + os.path.basename(nuke.root()['name'].value())
	print "\nFile & version list: \n"

	node_classes = ['Read', 'ReadGeo', 'Camera']
	node_list = []

	for i in nuke.allNodes():
		for x in node_classes:
			if i.knob('file') and i.Class() == x:
				node_list.append(i)

	for node in node_list:
		filepath = node['file'].value()
		filename = os.path.basename(filepath)

		filename_no_version = filename[0:filename.find('_v')]
		version = filename[filename.find('_v')+1:filename.find('_v')+6]

		print filename_no_version + " - " + version


nuke.menu('Nuke').addCommand('Edit/Filepath Lister','mau_filepathlister.fileLister()')
