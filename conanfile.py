from conans import ConanFile, CMake, tools


class HashUtilsConan(ConanFile):
	name = "HashUtils"
	description = "C++ utilities to compute hashes based on OpenSSL"
	url = "https://github.com/systelab/cpp-hash-utils"
	homepage = "https://github.com/systelab/cpp-hash-utils"
	author = "CSW <csw@werfen.com>"
	topics = ("conan", "hash", "utilities", "openssl", "wrapper")
	license = "MIT"
	generators = "cmake_find_package"
	settings = "os", "compiler", "build_type", "arch"
	options = {"openssl": ["1.0.2n", "1.0.2s", "1.1.1g"], "gtest": ["1.7.0", "1.8.1", "1.10.0"]}
	default_options = {"openssl": "1.1.1g", "gtest": "1.10.0"}
	exports_sources = "*, !build*, !*.yml, !*.md, !ci, !.git*"

	def configure(self):
		self.options["openssl"].shared = True

	def requirements(self):
		self.requires("openssl/1.1.1w#2d78cf15871a2cd0bc206c3d560cf741")
		self.requires("gtest/1.10.0", private=True)

	def build(self):
		cmake = CMake(self)
		cmake.configure()
		cmake.build()

	def imports(self):
		self.copy("*.dll", dst=("bin/%s" % self.settings.build_type), src="bin")
		self.copy("*.dylib*", dst="bin", src="lib")
		self.copy("*.so*", dst="bin", src="lib")

	def package(self):
		self.copy("IHashService.h", dst="include/HashUtils", src="src/HashUtils")
		self.copy("IHashUtilsFactory.h", dst="include/HashUtils", src="src/HashUtils")
		self.copy("HashUtilsFactory.h", dst="include/HashUtils", src="src/HashUtils")
		self.copy("*HashUtils.lib", dst="lib", keep_path=False)
		self.copy("*HashUtils.pdb", dst="lib", keep_path=False)
		self.copy("*HashUtils.a", dst="lib", keep_path=False)

	def package_info(self):
		self.cpp_info.libs = tools.collect_libs(self)
