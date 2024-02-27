import os
from conans import ConanFile, tools

class HashUtilsTestUtilitiesConan(ConanFile):
    name = "HashUtilsTestUtilities"
    description = "Test utilities for C++ Hash Utilities"
    url = "https://github.com/systelab/cpp-hash-utils"
    homepage = "https://github.com/systelab/cpp-hash-utils"
    author = "CSW <csw@werfen.com>"
    topics = ("conan", "hash", "utils", "test")
    license = "MIT"
    generators = "cmake_find_package"
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "*, !build*, !*.yml, !*.md, !ci, !.git*"

    def requirements(self):
        self.requires("gtest/1.10.0")

        if ("%s" % self.version) == "None":
            channel = os.environ['CHANNEL'] if "CHANNEL" in os.environ else "stable"
            self.requires(f"HashUtils/{os.environ['VERSION']}@systelab/{channel}")
        else:
            self.requires(f"HashUtils/{self.version}@systelab/{self.channel}")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")
        self.copy("*.so*", dst="bin", src="lib")

    def package(self):
        self.copy("*.h", dst="include/HashUtilsTestUtilities", keep_path=True)
        self.copy("*HashUtilsTestUtilities.lib", dst="lib", keep_path=False)
        self.copy("*HashUtilsTestUtilities.pdb", dst="lib", keep_path=False)
        self.copy("*HashUtilsTestUtilities.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
