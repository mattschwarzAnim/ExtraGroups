#====================== BEGIN GPL LICENSE BLOCK ======================
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
#======================= END GPL LICENSE BLOCK ========================
TEMPLATE = '''# This file is partially auto-generated by addon ExtraGroups
# User can have completed / changed auto-generated code
# http://julienduroure.com/ExtraGroups
# for any questions, please ask contact@julienduroure.com
##########################################################################################
#	GPL LICENSE:
#-------------------------
# This file is part of ExtraGroups.
#
#    ExtraGroups is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    ExtraGroups is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with ExtraGroups.  If not, see <http://www.gnu.org/licenses/>.
##########################################################################################
#
#	Copyright 2016 Julien Duroure (contact@julienduroure.com)
#
##########################################################################################

import bpy

from bpy.props import (
	BoolProperty,
	StringProperty,
	IntProperty,
)

from bpy.types import (
	Operator,
)

############################################################ Before change bones ##################################
def function_###opsclass###_before(on_off):
	pass

############################################################ After change bones ###################################
def function_###opsclass###_after(on_off):
	pass

############################################################ Change bones #########################################
def function_###opsclass###_(on_off,bone_tab,bonename):
	pass




########################################### class : do not touch :)
class POSE_OT_###opsclass###(Operator):
	"""User defined Operator"""
	bl_idname = "pose.ope_###opsclass###"
	bl_label = "###opsclass###"
	
	
	ops_id		 = StringProperty()
	index			= IntProperty()
	
	@classmethod
	def poll(self, context):
		return (context.object and
				context.object.type == 'ARMATURE' and
				context.mode == 'POSE')
				
	def execute(self, context):
		armature = context.object
		
		#retrieve on_off
		on_off = False
		found = False
		for ops in armature.jueg_grouptypelist[armature.jueg_active_grouptype].group_ids[self.index].on_off:
			if ops.id == self.ops_id:
				on_off = ops.on_off
				found = True
		
		if found == False:
			print("error")
		
		#check if this is a classic group or current selection
		current_selection = armature.jueg_grouptypelist[armature.jueg_active_grouptype].group_ids[self.index].current_selection
		if current_selection == False:
			#retrieve bones from group
			bones = armature.jueg_grouptypelist[armature.jueg_active_grouptype].group_ids[self.index].bone_ids
		else:
			#retrieve bones from current selection
			bones = []
			for bone in armature.pose.bones:
				if bone.bone.select == True:
					bones.append(bone)		
		
		function_###opsclass###_before(on_off)
		
		to_delete = []
		idx = -1
		for bone in bones:
			idx = idx + 1
			if bone.name not in armature.data.bones: #If bone no more exists
				to_delete.append(idx)
				continue
			function_###opsclass###_(on_off, armature.pose.bones, bone.name)
			
		function_###opsclass###_after(on_off)
		
		#delete bones if any
		if len(to_delete) > 0:
			for i in to_delete:
				armature.jueg_grouptypelist[armature.jueg_active_grouptype].group_ids[self.index].bone_ids.remove(i)
		 
		 #switch on/off
		for ops in armature.jueg_grouptypelist[armature.jueg_active_grouptype].group_ids[self.index].on_off:
			if ops.id == self.ops_id:
				ops.on_off = not ops.on_off
		
		return {'FINISHED'}
	
def register():
	bpy.utils.register_class(POSE_OT_###opsclass###)
	
def unregister():
	bpy.utils.unregister_class(POSE_OT_###opsclass###)
	
if __name__ == "__main__":
	register()	
'''
