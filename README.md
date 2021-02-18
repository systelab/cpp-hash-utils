[![Build Status](https://travis-ci.org/systelab/cpp-hash-utils.svg?branch=master)](https://travis-ci.org/systelab/cpp-hash-utils)
[![Build status](https://ci.appveyor.com/api/projects/status/p9wc1exxkvx3yavt?svg=true)](https://ci.appveyor.com/project/systelab/cpp-hash-utils)
[![codecov](https://codecov.io/gh/systelab/cpp-hash-utils/branch/master/graph/badge.svg)](https://codecov.io/gh/systelab/cpp-hash-utils)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/492f2b284cd149018ec9dd54a45d53df)](https://www.codacy.com/app/systelab/cpp-hash-utils?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=systelab/cpp-hash-utils&amp;utm_campaign=Badge_Grade)


# C++ Utilities for Hashes

This repository offers a set of utilities to generate hashes using the most popular algorithms. They are implemented based on [OpenSSL](https://www.openssl.org/) library, but offering a much simpler interface.

## Supported hash functions

* [SHA-256](https://en.wikipedia.org/wiki/SHA-2)
* [MD5](https://en.wikipedia.org/wiki/MD5)


## Setup

### Download using Conan

This library is designed to be installed by making use of [Conan](https://conan.io/) package manager. So, you just need to add the following requirement into your Conan recipe:

```python
def requirements(self):
   self.requires("HashUtils/1.0.0@systelab/stable")
```

> Version number of this code snipped is set just as an example. Replace it for the desired package version to retrieve.

As this package is not available on the conan-center, you will also need to configure a remote repository before installing dependencies:

```bash
conan remote add systelab-public https://systelab.jfrog.io/artifactory/api/conan/cpp-conan-production-local
```

See Conan [documentation](https://docs.conan.io/en/latest/) for further details on how to integrate this package with your build system.

### Build from sources

See [BUILD.md](BUILD.md) document for details.


## Usage

Create an instance of the `systelab::hash::HashUtilsFactory` class to build the services that implement the supported the hash algorithms:

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

