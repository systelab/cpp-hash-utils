from conan import ConanFile
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout
from conan.tools.files import collect_libs, copy
import os


class HashUtilsConan(ConanFile):
	required_conan_version = ">=2.0.0"
	name = "hash-utils"
	description = "C++ utilities to compute hashes based on OpenSSL"
	url = "https://github.com/systelab/cpp-hash-utils"
	homepage = "https://github.com/systelab/cpp-hash-utils"
	author = "CSW <csw@werfen.com>"
	topics = ("conan", "hash", "utilities", "openssl", "wrapper")
	license = "MIT"
	settings = "os", "compiler", "build_type", "arch"
	exports_sources = "*, !build*, !*.yml, !*.md, !ci, !.git*"

	def layout(self):
		cmake_layout(self)

	def configure(self):
		self.options["openssl"].shared = True

	def requirements(self):
		self.requires("openssl/3.0.19")
		self.requires("gtest/1.14.0", visible=False)

	def generate(self):
		CMakeDeps(self).generate()
		CMakeToolchain(self).generate()
		for dependency in self.dependencies.values():
			for bindir in dependency.cpp_info.bindirs:
				copy(self, "*.dll", bindir, os.path.join(self.build_folder, "bin", str(self.settings.build_type)))
			for libdir in dependency.cpp_info.libdirs:
				copy(self, "*.dylib*", libdir, os.path.join(self.build_folder, "bin"))
				copy(self, "*.so*", libdir, os.path.join(self.build_folder, "bin"))

	def build(self):
		cmake = CMake(self)
		cmake.configure()
		cmake.build()

	def package(self):
		copy(self, "IHashService.h", dst=os.path.join(self.package_folder, "include", "HashUtils"), src=os.path.join(self.source_folder, "src", "HashUtils"))
		copy(self, "IHashUtilsFactory.h", dst=os.path.join(self.package_folder, "include", "HashUtils"), src=os.path.join(self.source_folder, "src", "HashUtils"))
		copy(self, "HashUtilsFactory.h", dst=os.path.join(self.package_folder, "include", "HashUtils"), src=os.path.join(self.source_folder, "src", "HashUtils"))
		copy(self, "*HashUtils.lib", dst=os.path.join(self.package_folder, "lib"), src=self.build_folder, keep_path=False)
		copy(self, "*HashUtils.pdb", dst=os.path.join(self.package_folder, "lib"), src=self.build_folder, keep_path=False)
		copy(self, "*HashUtils.a", dst=os.path.join(self.package_folder, "lib"), src=self.build_folder, keep_path=False)

	def package_info(self):
		self.cpp_info.libs = collect_libs(self)
		self.cpp_info.set_property("cmake_file_name", "HashUtils")
		self.cpp_info.set_property("cmake_target_name", "HashUtils::HashUtils")
