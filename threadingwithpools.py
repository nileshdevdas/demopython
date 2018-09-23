from multiprocessing import  Pool;

# another way of restriction to tool number of threads
def myfn(x):
    print(x);

p = Pool(5);
print(p)
p.map('myfn', [1])

