import _thread;

# the function / Job / Executor function / runnable
def run(x , x1):
    a = range(100)
    for t in a:
        print("Thread Name " + x);
        print(t);

try:
     #_thread // api
     #.start_new_thread // start a new thread
     #(run ==> the name of the method (A name that return function)
     # in python everything i and object
     _thread.start_new_thread(run, ("thread-01" , 'x'));
     _thread.start_new_thread(run, ("thread-02", 'x'));
     _thread.start_new_thread(run, ("thread-03" , 'x'));
     _thread.start_new_thread(run, ("thread-04", 'x'));
     _thread.start_new_thread(run, ("thread-05" , 'x'));
     _thread.start_new_thread(run, ("thread-06", 'x'));
    #run("it1","x");
    #run("it2", "x");
    #run("it3", "x");
    #run("it4", "x");
    #run("it5", "x");

except Exception as err:
    print(err);

#if i dont write this code my main thread will come out
# if my main thread comes out all my child thread will die
while 1:
    pass;