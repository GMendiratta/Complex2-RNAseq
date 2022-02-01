import requests
import os 
import shutil

with open('archive.txt','r') as f1:
	archive_new=f1.readlines()
urllist=[link.replace('\n','') for link in archive_new]



flist=[fname for fname in os.listdir() if 'tar.gz' in fname]
currfollist=[fname for fname in os.listdir() if '.' not in fname] 

for url in urllist:
	fname=url.split('/')[-1]
	# download study if absent
	if (fname not in flist) and (fname.split('.')[0] not in currfollist):
		print('downloading:',url)
		r=requests.get(url,allow_redirects=True)
		open(fname,'wb').write(r.content)

# # Unpack Raw Study Data
currfollist=[fname for fname in os.listdir() if '.' not in fname] 

# do not overwrite if folder already present
for fname in flist:
	if fname.split('.')[0] not in currfollist:
		shutil.unpack_archive(fname)
		os.remove(fname) # at this point the tar files are no longer needed.