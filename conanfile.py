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
	exports_sources = "*, !build*, !*.yml, !*.md, !ci, !.git*"

	def configure(self):
		self.options["openssl"].shared = True

	def requirements(self):
		self.requires("zlib/1.2.13#13c96f538b52e1600c40b88994de240f", override=True)
		self.requires("openssl/3.0.12#1670458f93ec138c3bb6afc65a1cd667")
		self.requires("gtest/1.14.0#4372c5aed2b4018ed9f9da3e218d18b3", private=True)

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
