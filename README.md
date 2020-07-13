[![Build Status](https://travis-ci.org/systelab/cpp-hash-utils.svg?branch=master)](https://travis-ci.org/systelab/cpp-hash-utils)
[![Build status](https://ci.appveyor.com/api/projects/status/p9wc1exxkvx3yavt?svg=true)](https://ci.appveyor.com/project/systelab/cpp-hash-utils)
[![codecov](https://codecov.io/gh/systelab/cpp-hash-utils/branch/master/graph/badge.svg)](https://codecov.io/gh/systelab/cpp-hash-utils)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/492f2b284cd149018ec9dd54a45d53df)](https://www.codacy.com/app/systelab/cpp-hash-utils?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=systelab/cpp-hash-utils&amp;utm_campaign=Badge_Grade)
[![Download](https://api.bintray.com/packages/systelab/conan/HashUtils:systelab/images/download.svg)](https://bintray.com/systelab/conan/HashUtils:systelab/_latestVersion)


# C++ utilities for Hashes

This repository offers a set of utilities to generate hashes using the most popular algorithms. They are implemented based on [OpenSSL](https://www.openssl.org/) library, but offering a much simpler interface.

## Supported hash functions

* [SHA-256](https://en.wikipedia.org/wiki/SHA-2)
* [MD5](https://en.wikipedia.org/wiki/MD5)

## Setup

### Build from sources

Prerequisites:
  - [Git](https://git-scm.com/)
  - [Conan](https://conan.io/)
  - [CMake](https://cmake.org/)
  - [Visual Studio](https://visualstudio.microsoft.com/) (only on Windows)
  - [GCC](https://gcc.gnu.org/) (only on Linux)

Build library with the following steps:
  1. Clone this repository in a local drive
  2. Make a build directory (i.e. `build/`)
  3. Install `conan` dependencies in the build directory
  4. Run `cmake` in the build directory to configure build targets
  5. Use `Visual Studio` (on Windows) or `make` (on Linux) to build the library

#### Windows

In order to build the application on Windows for the `Release` configuration, run the following commands ($VSINSTALLPATH is the path where Visual Studio has been installed):

``` bash
> git clone https://github.com/systelab/cpp-hash-utils
> md build && cd build
> conan remote add systelab-bintray https://api.bintray.com/conan/systelab/conan
> conan install .. -s build_type=Release -s compiler.toolset=v142 -s arch=x86_64
> cmake .. -G "Visual Studio 16 2019" -A x64
> "$VSINSTALLPATH/devenv.com" HashUtils.sln /build "Release" /PROJECT "HashUtils"
```

However, if you want to `Debug` the source code, you will need these commands:

``` bash
> git clone https://github.com/systelab/cpp-hash-utils
> md build && cd build
> conan remote add systelab-bintray https://api.bintray.com/conan/systelab/conan
> conan install .. -s build_type=Debug -s compiler.toolset=v142 -s arch=x86_64
> cmake .. -G "Visual Studio 16 2019" -A x64
> "$VSINSTALLPATH/devenv.com" HashUtils.sln /build "Debug" /PROJECT "HashUtils"
```

#### Linux
``` bash
> git clone https://github.com/systelab/cpp-hash-utils
> mkdir build && cd build
> conan install ..
> cmake .. -DCMAKE_BUILD_TYPE=[Debug | Coverage | Release]
> make
```

### Download using Conan

  1. Create/update your `conanfile.txt` to add this library as follows:

```
[requires]
HashUtils/1.0.0@systelab/stable

[generators]
cmake
```

  2. Integrate Conan into CMake by adding the following code into your `CMakeLists.txt`:

```cmake
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()
```

  3. Link against `${CONAN_LIBS}` when configuring your executables in CMake:

```cmake
set(MY_PROJECT MyProject)
add_executable(${MY_PROJECT} main.cpp)
target_link_libraries(${MY_PROJECT} ${CONAN_LIBS})
```

## Usage

Create an instance of the `systelab::hash::HashUtilsFactory` class to build the services that support the hash algorithms:

```cpp
#include "HashUtils/HashUtilsFactory"
#include "HashUtils/IHashService.h"

systelab::hash::HashUtilsFactory hashUtilsFactory;
```

### SHA-256

The SHA-256 hash of an string value can be computed as follows:

```cpp
std::string hash = hashUtilsFactory.buildSHA256HashService()->computeHash("Value to be hashed");
```

### MD5

The MD5 hash of an string value can be computed in analogous manner:

```cpp
std::string hash = hashUtilsFactory.buildMD5HashService()->computeHash("Value to be hashed");
```

