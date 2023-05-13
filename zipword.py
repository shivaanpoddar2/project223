import zipfile
import time

folderpath = input('Path to the file: ')
zipf = zipfile.Zipfile(folderpath)
global result
result = 0
global tried
tried = 0
c=0
if not zipf:
    print('the zipped file/folder in not password protected! you can successfully open it')

else:
    starttime = time.time()
    wordListFile = open('wordlist.txt', 'r', errors='ignore')
    body = wordListFile.read().lower()
    words = body.split('/n')
    for i in range(len(words)):
        word = words[i]
        password=word.encode('utf8').strip()
        c=c+1
        print('Trying to decode password by: {}'. format(word))
        try:
            with zipfile.ZipFile(folderpath,'r') as zf:
                zf.extractall(pwd=password)
                print('Success! the password is: '+ word)
                endtime = time.time()
                result = 1
            break
        except:
            pass
        if (result == 0):
            print("Sorry, password not found. A total of"+str(c)+"+ possible combinations tried in"+ str(duration)+"seconds. Password is not of 4 characters.")
        else:
            duration = endtime - starttime
            print('Congratulation!! password found after trying '+str(c)+' combination in '+str(duration)+'seconds')