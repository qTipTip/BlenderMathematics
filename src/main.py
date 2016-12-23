from parametric_surfaces import *
import bpy

# surface of choice

U_RESOLUTION = 40
V_RESOLUTION = 40

surface = klein_bottle(U_RESOLUTION, V_RESOLUTION)

mesh = bpy.data.meshes.new(surface.name)
blender_object = bpy.data.objects.new(surface.name, mesh)

blender_object.location = bpy.context.scene.cursor_location
bpy.context.scene.objects.link(blender_object)

vertices, faces = surface.generate_mesh_data()
mesh.from_pydata(vertices, [], faces)
mesh.update(calc_edges=True)
