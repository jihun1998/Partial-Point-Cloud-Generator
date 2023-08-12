# Partial-Point-Cloud-Generator

1. Clone this repository.

2. Install python dependencies
```
    pip install open3d
    pip install os
    pip install glob
    pip install plyfile
    pip install numpy
```   
3. Download dataset and prepare pose files. We used PCN dataset. We provide pose files that we use.

4. Run partial point cloud generator code.
```
    python partial_pc_generator.py --data_path DATAPATH --pose_path POSEPATH --result_path RESULTPATH
```
You should indicate DATAPATH, POSEPATH, and RESULTPATH according to your environment.

---
Note that point cloud files should be '.ply' format and pose files should be '.txt' format.
