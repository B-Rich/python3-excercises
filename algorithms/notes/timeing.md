# Timing 

### For timing things, use timeit.
```
>>> import timeit
>>> timeit.timeit("x = 2 + 2") 
>>> 0.034976959228515625""
```

### To find bottlenecks, use a profiler.
```
import cProfile 
cProfile.run('main()')
```
