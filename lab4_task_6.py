import os
for root, directories, filenames in os.walk('gurleen'):
	for directory in directories:
		print( os.path.join(root, directory) )
	for filename in filenames: 
		print(os.path.join(root,filename) )
