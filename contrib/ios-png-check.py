#!/opt/local/bin/python

# PYTHON PORT OF http://github.com/eploko/ios-png-check
# by Matt Galloway (http://iphone.galloway.me.uk/)

import os
import glob
import re

files_wo_1x_version = []
files_wo_2x_version = []
size_errors = []

png_files = glob.glob('*.png')

for png_file in png_files:
	name_parts = re.split('[@\.]', png_file)

	v1x_exists = False
	v2x_exists = False

	if len(name_parts) == 3:
		v1_name = name_parts[0] + "." + name_parts[2]
		v2_name = name_parts[0] + "@2x." + name_parts[2]
		v1x_exists = os.path.exists(v1_name)
		v2x_exists = os.path.exists(v2_name)
		if not v1x_exists:
			files_wo_1x_version.append(png_file)

		if v1x_exists and v2x_exists:
			v1_out = os.popen('file %s' % v1_name).read()
			v1_info = re.search('(\d+) x (\d+)', v1_out)
			v2_out = os.popen('file %s' % v2_name).read()
			v2_info = re.search('(\d+) x (\d+)', v2_out)
			v1w = int(v1_info.group(1))
			v1h = int(v1_info.group(2))
			v2w = int(v2_info.group(1))
			v2h = int(v2_info.group(2))
			v2w_expected = v1w * 2
			v2h_expected = v1h * 2

			if v2w != v2w_expected or v2h != v2h_expected:
				size_errors.append("%s: SIZE IS %i x %i, EXPECTED %i x %i" % (v2_name, v2w, v2h, v2w_expected, v2h_expected))

	elif len(name_parts) == 2:
		v1_name = name_parts[0] + "." + name_parts[1]
		v2_name = name_parts[0] + "@2x." + name_parts[1]
		v1x_exists = os.path.exists(v1_name)
		v2x_exists = os.path.exists(v2_name)
		if not v1x_exists:
			files_wo_2x_version.append(png_file)

if len(png_files) == 0:
	print "HEY, THERE'S NO PNG FILES IN THE CURRENT FOLDER."

is_all_okay = True

if len(files_wo_1x_version) != 0:
	print "FILES WITHOUT @1x VERSION ============================================"
	for i in files_wo_1x_version:
		print i
	print ""
	is_all_okay = False
  
if len(files_wo_2x_version) != 0:
	print "FILES WITHOUT @2x VERSION ============================================"
	for i in files_wo_2x_version:
		print i
	print ""
	is_all_okay = False

if len(size_errors) != 0:
	print "INVALID IMAGE SIZES DETECTED FOR THE FOLLOWING FILES ================="
	for i in size_errors:
		print i
	print ""
	is_all_okay = False
  
if is_all_okay:
	print "YOUR PNG ASSETS IN THE CURRENT FOLDER ARE FINE, DUDE."
