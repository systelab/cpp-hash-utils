cmake_minimum_required(VERSION 3.2)

project(HashUtilsPackageTestProject)

# Configure environment
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/../cmake ${CMAKE_BINARY_DIR})
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

# Find external dependencies
find_package(HashUtils)

# Configure test package project
set(HASH_UTILS_PACKAGE_TEST_PROJECT HashUtilsPackageTest)
add_executable(${HASH_UTILS_PACKAGE_TEST_PROJECT} HashUtilsExample.cpp)
target_link_libraries(${HASH_UTILS_PACKAGE_TEST_PROJECT} HashUtils::HashUtils)

# Register tests
enable_testing()
add_test(NAME HashUtilsPackageTest COMMAND ${HASH_UTILS_PACKAGE_TEST_PROJECT})
