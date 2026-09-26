import h5py
#create a new file and add a dataset
with h5py.File('newfile.h5', 'w') as f:
    f.create_dataset('temperature', data=[300, 310, 320]) 
#read the file
f = h5py.File('newfile.h5', 'r') 
print(f.filename)   # 'data.h5'
print(f.mode)       # 'r'
#print the keys in the file
with h5py.File('newfile.h5', 'r') as f:
    for key in f.keys():
        print(key)
#create a new file and add datasets
import numpy as np

with h5py.File('data.h5', 'w') as f:
    f.create_dataset('temp',  data=np.arange(100))
    f.create_dataset('deps',  data=np.random.rand(100))
    f.create_dataset('matrix', shape=(1000, 1000), dtype='f8')  # preallocated
#create a new file and add a group and datasets(something like a folder)
with h5py.File('data.h5', 'w') as f:
    grp = f.create_group('experiment1')
    grp.create_dataset('temp', data=[300, 310, 320])
    grp.create_dataset('deps', data=[0.1, 0.2, 0.3])
#read the group and datasets
with h5py.File('data.h5', 'r') as f:
    dset = f['experiment1/temp']     # like a dict lookup
    print(dset.shape)                # (3,)
    print(dset.dtype)                # int64
    print(dset[:])                   # [300 310 320] — NumPy array


