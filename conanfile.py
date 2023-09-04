from conan import ConanFile
from conan.tools.files import copy
from os.path import join


class RemoteryConan(ConanFile):
    name = "remotery"
    version = "e4ae3baacd"
    license = "Apache-2.0"
    author = "@Celtoys"
    url = "https://github.com/Celtoys/Remotery"
    description = "A realtime CPU/GPU profiler hosted in a single C file with a viewer that runs in a web browser."
    topics = ("profiler")

    def source(self):
        remotery_version = self.version.split('-')[0]
        self.run("git clone https://github.com/Celtoys/Remotery.git")
        self.run("cd Remotery && git checkout %s" % remotery_version)

    def package(self):
        copy(self, "*.h", join(self.source_folder, "Remotery/lib"), join(self.package_folder, "include"))
        copy(self, "*.c", join(self.source_folder, "Remotery/lib"), join(self.package_folder, "src"))
        copy(self, "*.mm", join(self.source_folder, "Remotery/lib"), join(self.package_folder, "src"))
        copy(self, "*", join(self.source_folder, "Remotery/vis"), join(self.package_folder, "js_client"))

    def package_id(self):
        self.info.clear()

    def package_info(self):
        self.cpp_info.includedirs = ['include']
        self.cpp_info.srcdirs = ['src']
