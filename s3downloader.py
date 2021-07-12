from cloudpathlib import CloudPath

root_dir = CloudPath("s3://bucketname")

path= 'C:/Users/g2/Desktop'

for f in root_dir.glob('**/*.txt'):
    text_data = f.read_text()
    print(f)            #Print all files and directories in bucket
    print(text_data)    #Print all content from .txt
    
root_dir.download_to(path)  #Download whole bucket to defined path
