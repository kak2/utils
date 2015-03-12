import codecs;
import os;
import re;

rootDir = 'D:\ccTalk\Projects\webembedzing';
for dirName, subdirList, fileList in os.walk(rootDir):
	for fname in fileList:
		tmp = fname.split('.')
		filetype = tmp[len(tmp) - 1]
		filetypeTarget = ['js', 'css', 'volt', 'php']
		try:
			if filetypeTarget.index(filetype) != -1:
				filename = dirName + '\\' + fname
				f = codecs.open(filename, 'r', 'utf-8')
				for line in f:
					a = re.findall(u'[\u4e00-\u9fff]+',line)
					if len(a) > 0:
						print('filename:' + filename)
						break
				f.close()
		except:
			"Do nothing"
			