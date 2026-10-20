from conan import ConanFile
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout
from conan.tools.files import collect_libs, copy
import os


class HashUtilsTestUtilitiesConan(ConanFile):
	required_conan_version = ">=2.0.0"
	name = "hash-utils-test-utilities"
	description = "Test utilities for C++ Hash Utilities"
	url = "https://github.com/systelab/cpp-hash-utils"
	homepage = "https://github.com/systelab/cpp-hash-utils"
	author = "CSW <csw@werfen.com>"
	topics = ("conan", "hash", "utils", "test")
	license = "MIT"
	settings = "os", "compiler", "build_type", "arch"
	exports_sources = "*, !build*, !*.yml, !*.md, !ci, !.git*"

	def layout(self):
		cmake_layout(self)

	def requirements(self):
		self.requires("gtest/1.14.0")

		if ("%s" % self.version) == "None":
			version = "0.0.0"
			self.requires(f"hash-utils/{version}")
		else:
			self.requires(f"hash-utils/{self.version}")

	def generate(self):
		CMakeDeps(self).generate()
		CMakeToolchain(self).generate()
		for dependency in self.dependencies.values():
			for bindir in dependency.cpp_info.bindirs:
				copy(self, "*.dll", bindir, os.path.join(self.build_folder, "bin"))
			for libdir in dependency.cpp_info.libdirs:
				copy(self, "*.dylib*", libdir, os.path.join(self.build_folder, "bin"))
				copy(self, "*.so*", libdir, os.path.join(self.build_folder, "bin"))

	def build(self):
		cmake = CMake(self)
		cmake.configure()
		cmake.build()

	def package(self):
		copy(self, "*.h", dst=os.path.join(self.package_folder, "include", "HashUtilsTestUtilities"), src=self.source_folder)
		copy(self, "*HashUtilsTestUtilities.lib", dst=os.path.join(self.package_folder, "lib"), src=self.build_folder, keep_path=False)
		copy(self, "*HashUtilsTestUtilities.pdb", dst=os.path.join(self.package_folder, "lib"), src=self.build_folder, keep_path=False)
		copy(self, "*HashUtilsTestUtilities.a", dst=os.path.join(self.package_folder, "lib"), src=self.build_folder, keep_path=False)

	def package_info(self):
		self.cpp_info.libs = collect_libs(self)
		self.cpp_info.set_property("cmake_file_name", "HashUtilsTestUtilities")
		self.cpp_info.set_property("cmake_target_name", "HashUtilsTestUtilities::HashUtilsTestUtilities")
