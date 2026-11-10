from conan import ConanFile
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout
from conan.tools.files import copy
import os

class HashUtilsTestConan(ConanFile):
    required_conan_version = ">=2.0.0"
    settings = "os", "compiler", "build_type", "arch"
    def layout(self):
        cmake_layout(self)

    def requirements(self):
        self.requires(self.tested_reference_str)

    def generate(self):
        CMakeDeps(self).generate()
        CMakeToolchain(self).generate()
        for dependency in self.dependencies.values():
            for bindir in dependency.cpp_info.bindirs:
                copy(self, "*.dll", bindir, os.path.join(self.build_folder, "bin", str(self.settings.build_type)))
            for libdir in dependency.cpp_info.libdirs:
                copy(self, "*.dll", libdir, os.path.join(self.build_folder, "bin", str(self.settings.build_type)))
                copy(self, "*.dylib*", libdir, os.path.join(self.build_folder, "bin"))
                copy(self, "*.so*", libdir, os.path.join(self.build_folder, "bin"))

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        cmake = CMake(self)
        cmake.test()
