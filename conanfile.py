from conans import ConanFile, CMake, tools


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

        self.copy("*.h", dst="include", src="Remotery/lib" )
        self.copy("*.c", dst="src", src="Remotery/lib" )
        self.copy("*.mm", dst="src", src="Remotery/lib" )

        self.copy("*", dst="js_client", src="Remotery/vis" )

    def package_id(self):
        self.info.header_only()

    def package_info(self):
        self.cpp_info.includedirs = ['include']
        self.cpp_info.srcdirs = ['src']

