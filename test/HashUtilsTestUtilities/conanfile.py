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
    options = {"openssl": ["1.0.2n", "1.0.2s", "1.1.1g"], "gtest": ["1.7.0", "1.8.1", "1.10.0"]}
    default_options = {"openssl":"1.1.1g", "gtest":"1.10.0"}
    exports_sources = "*"

    def configure(self):
        self.options["HashUtils"].gtest = self.options.gtest
        self.options["HashUtils"].openssl = self.options.openssl

    def requirements(self):
        if self.options.gtest == "1.7.0":
            self.requires("gtest/1.7.0@systelab/stable")
        elif self.options.gtest == "1.8.1":
            self.requires("gtest/1.8.1")
        else:
            self.requires("gtest/1.10.0")

        if ("%s" % self.version) == "None":
            self.requires("HashUtils/%s@systelab/stable" % os.environ['VERSION'])
        else:
            self.requires("HashUtils/%s@systelab/stable" % self.version)

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
