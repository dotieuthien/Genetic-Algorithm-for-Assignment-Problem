
import time

n = 100
start_time = time.time()

for i in range(n):
    local_start_time = time.time()
    import hungarian
    hungarian.solve()
    local_time = time.time()-local_start_time
    print('#{} time(s): {:.3f}'.format(i, local_time))

end_time = time.time()
print('time(s): {:.3f}'.format((end_time-start_time)/n))
