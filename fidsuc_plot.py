import numpy as np

def fidsp_plot(fs):     
    smax = max(fs[1,:])
    f = max(fs[0,:])
    s = max([fs[1,i] for i in range(len(fs[0,:])) if fs[0,i] == f])
        
    fid = [f, f]
    suc = [0, s]
    
    while s < smax:
        delete = [i for i in range(len(fs[0,:])) if fs[1,i] <= s]
        fs = np.delete(fs, delete, axis = 1)
        f = max(fs[0,:])
        s = max([fs[1,i] for i in range(len(fs[0,:])) if fs[0,i] == f])
        fid.append(f)
        suc.append(s)
        
    return suc, fid


