from NVDAObjects.IAccessible import IAccessible
import controlTypes
import appModuleHandler
class klicktel_control(IAccessible):
	classrolemaps = {
		'TcxPageControl': controlTypes.role.Role.TABCONTROL,
		'TOvcVirtualListBox': controlTypes.role.Role.LIST,
		'TcxCheckBox': controlTypes.role.Role.CHECKBOX,
		'TMainF': controlTypes.role.Role.FORM,
		'TcxTabSheet': controlTypes.role.Role.TAB,
		'TPanel': controlTypes.role.Role.PANEL,
		'TcxHeader': controlTypes.role.Role.HEADER,
		'TEinstellF': controlTypes.role.Role.FORM,
		'TcxTreeView': controlTypes.role.Role.TREEVIEW,
		'TfrmSearchAssi': controlTypes.role.Role.FORM,
		'TdxDockControl': controlTypes.role.Role.PANEL,
		'TdxBarControl': controlTypes.role.Role.TOOLBAR,
		'TPlaceForm': controlTypes.role.Role.FORM,
		'TcxMRUEdit': controlTypes.role.Role.EDITABLETEXT,
		'TJvPanel': controlTypes.role.Role.PANEL,
		'TVirtualDrawTree': controlTypes.role.Role.TREEVIEW,
		'TfrmTradePanel': controlTypes.role.Role.PANEL,
		'HH Parent': controlTypes.role.Role.WINDOW, 
		'HH Child': controlTypes.role.Role.WINDOW,
		'Shell DocObject View': controlTypes.role.Role.DOCUMENT,
		'TcxButtonEdit': controlTypes.role.Role.EDITABLETEXT,
		'Shell Embedding': controlTypes.role.Role.EMBEDDEDOBJECT,
		'TApplication': controlTypes.role.Role.APPLICATION,
		'TSUmfangF': controlTypes.role.Role.FORM,
		'TSuchF': controlTypes.role.Role.FORM,
		'TGesamtL': controlTypes.role.Role.LIST,
		'TKTel99AdressenF': controlTypes.role.Role.FORM,
	}
	def _get_role(self):
		return self.classrolemaps[self.windowClassName]

class klicktel_pagecontrol(klicktel_control):
	def _get_name(self):
		objname = self.firstChild.firstChild.name
		if objname != "":
			return objname
class AppModule(appModuleHandler.AppModule):
	def chooseNVDAObjectOverlayClasses(self, obj, clslist):
		if isinstance(obj, IAccessible) and obj.IAccessibleRole == 10:
			clslist.insert(0,klicktel_control)
		if obj.windowClassName == 'TcxPageControl':
			clslist.insert(0,klicktel_pagecontrol)
   