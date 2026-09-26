import h5py
import numpy as np



with h5py.File('3-15-7-1-exponential.h5', 'r') as f:
    print("=== Root attributes ===")
    for k, v in f.attrs.items():
        print(f"  {k!r} = {v!r}")

    print("\n=== Root members ===")
    def show(name, obj):
        kind = "Group" if isinstance(obj, h5py.Group) else "Dataset"
        print(f"  [{kind}] {name}")
        for ak, av in obj.attrs.items():
            print(f"        attrs.{ak!r} = {av!r}")
    f.visititems(show)