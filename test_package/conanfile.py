from conans import ConanFile, CMake

class HashUtilsTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake_find_package"
    options = {"openssl": ["1.0.2n", "1.0.2s", "1.1.1g"], "gtest": ["1.7.0", "1.8.1", "1.10.0"]}
    default_options = {"openssl":"1.1.1g", "gtest":"1.10.0"}

    def configure(self):
        self.options["HashUtils"].openssl = self.options.openssl
        self.options["HashUtils"].gtest = self.options.gtest

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")
        self.copy('*.so*', dst='bin', src='lib')

    def test(self):
        cmake = CMake(self)
        cmake.test()
