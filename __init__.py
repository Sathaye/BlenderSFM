bl_info = {
    "name": "BlenderSFM",
    "author": "Apoorva Joshi",
    "version": (0, 1),
    "blender": (2, 6, 9),
    "location": "View3D > Add > Mesh",
    "description": "Construct point cloud from photographs",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Add Mesh"}

if "bpy" in locals():
    import imp
    imp.reload(PointCloud)
else:
    from blenderSFM import PointCloud

import bpy
import sys

<<<<<<< HEAD
################################################################################
##### REGISTER #####

def add_mesh_point_cloud(self, context):
    self.layout.operator(PointCloud.add_mesh_point_cloud.bl_idname, text="Point Cloud", icon="GROUP_VERTEX")
=======
>>>>>>> d1dae371d33b701dec2536e57df92c4597f7ea16

def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)
    
if __name__ == "__main__":
    register()
