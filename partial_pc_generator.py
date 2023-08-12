import open3d as o3d
import glob, plyfile, numpy as np, argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--data_path', help='string', default='./data/02691156')
parser.add_argument('--pose_path', help='string', default='./pose/02691156')
parser.add_argument('--result_path', help='string', default='./result/02691156')
opt = parser.parse_args()
data_path = opt.data_path
pose_path = opt.pose_path
result_path = opt.result_path
data_list = glob.glob(os.path.join(data_path,'*.ply'))

for pcd_path in data_list:
    pcd_name = pcd_path.split('/')[-1]
    pose_name = pcd_path.split('/')[-1].replace('.ply','.txt')
    pcd = o3d.io.read_point_cloud(pcd_path)
    f = open(os.path.join(pose_path,pose_name))
    diameter = np.linalg.norm(np.asarray(pcd.get_max_bound()) - np.asarray(pcd.get_min_bound()))
    radius = diameter * 1000
    lines = f.readlines()
    camera = [float(lines[0].split()[3]), float(lines[1].split()[3]), float(lines[2].split()[3])]
    _, pt_map = pcd.hidden_point_removal(camera, radius)
    pcd2 = pcd.select_by_index(pt_map)
    o3d.io.write_point_cloud(os.path.join(result_path,pcd_name), pcd2)
    import pdb;pdb.set_trace()
    
# pcd = o3d.io.read_point_cloud('/mnt/jihun/Research_jh/PCN-PyTorch/data/PCN/train/complete/02691156/1a04e3eab45ca15dd86060f189eb133.ply')
# f = open('/mnt/jihun2/shapenet_cameras/02691156/1a04e3eab45ca15dd86060f189eb133__0__.txt')
# diameter = np.linalg.norm(np.asarray(pcd.get_max_bound()) - np.asarray(pcd.get_min_bound()))
# radius = diameter * 1000
# lines = f.readlines()
# camera = [float(lines[0].split()[3]), float(lines[1].split()[3]), float(lines[2].split()[3])]
# _, pt_map = pcd.hidden_point_removal(camera, radius)
# pcd2 = pcd.select_by_index(pt_map)
# o3d.io.write_point_cloud('./partial_test.ply',pcd2)
