import os;
import _thread;

def run(fileName , threadName):
    print("Thread Name " + threadName);
    filedata = open(fileName);
    for line in filedata:
        print(threadName + "  >>>>>> " + line );
try:
    dirList = os.listdir("c:/input/flt")
    for file in dirList:
        _thread.start_new_thread(run, ("c:/input/flt/"+file , 'thread-process-'+file));
except Exception as err:
    print(err);

while 1:
    pass;