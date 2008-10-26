from swlib.pysw import SW
import os
class ModuleCreator(object):
	def __init__(self, module_name, driver, key_type, extra_attrs={}, encoding="UTF-8", duplicates=False):
		self.driver = driver
		self.key_type = key_type
		self.module_name = module_name
		self.encoding = encoding
		self.duplicates = duplicates
		self.keys = {}
		
		module_dir = "./modules/%s" % module_name
		if isinstance(driver, (SW.RawVerse, SW.zVerse)):
			self.module_extra = ""
		else:
			self.module_extra = "/" + module_name
		
		path = module_dir + self.module_extra
		if not os.path.exists("mods.d"):
			os.mkdir("mods.d")

		if os.path.exists(module_dir):
			# empty directory
			for dir_item in os.listdir(module_dir):
				try:
					os.remove(module_dir + "/" + dir_item)
				except OSError, e:
					print "ERROR", e
			pass
		else:
			os.makedirs(module_dir)
			

		assert driver.createModule(path) == '\x00', \
			"Failed creating module"
		

		self.module = driver(path)
		assert self.module.isWritable(), "MODULE MUST BE WRITABLE"

		driver_type = driver.__name__
		f2 = open("mods.d/%s.conf" % self.module_name, "w")
		f2.write('''\
[%(module_name)s]
DataPath=%(path)s
Encoding=%(encoding)s
ModDrv=%(driver_type)s\n''' % locals())
		for key, value in extra_attrs.items():
			f2.write("%s=%s\n" % (key, value.encode(encoding)))
		
		f2.close()
		

	def add_entry(self, key, text):
		if key in self.keys:
			assert self.duplicates, "Duplicate key %s" % key
			self.keys[key] += 1
			key += " (%d)" % self.keys[key]

		else:
			self.keys[key] = 1

		self.module.setKey(self.key_type(key.encode(self.encoding)))
		self.module.setEntry(text.encode(self.encoding))
		return key
