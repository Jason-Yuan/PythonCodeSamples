import os, glob
import chardet
from codecs import BOM_UTF8

os.chdir("/Path/to/your/folder")

# grap all *.cue files in target folder
for file in glob.glob("*.cue"):
	with open(file) as f:
		content = f.read()
		code = chardet.detect(content)['encoding']
		if code == 'UTF-8':
			continue
		try:
			content = content.decode(code).encode('utf8')
		except:
			print 'Unable to encode', file
			continue
		new_cue = os.path.splitext(file)[0]+'-UTF8.cue'
		with open(new_cue, 'w') as f:
			f.write(BOM_UTF8)
			f.write(content)