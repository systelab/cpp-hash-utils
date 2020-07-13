cmake_minimum_required(VERSION 3.2)

project(HashUtilsTestUtilitiesPackageTestProject)

# Configure environment
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/../cmake ${CMAKE_BINARY_DIR})
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

# Find tested package
find_package(HashUtilsTestUtilities)

# Configure test package project
set(HASH_UTILS_TEST_UTILITIES_PACKAGE_TEST_PROJECT HashUtilsTestUtilitiesPackageTest)
add_executable(${HASH_UTILS_TEST_UTILITIES_PACKAGE_TEST_PROJECT} HashUtilsTestUtilitiesExample.cpp)
target_link_libraries(${HASH_UTILS_TEST_UTILITIES_PACKAGE_TEST_PROJECT} HashUtilsTestUtilities::HashUtilsTestUtilities)

# Register test
enable_testing()
add_test(NAME HashUtilsTestUtilitiesPackageTest COMMAND ${HASH_UTILS_TEST_UTILITIES_PACKAGE_TEST_PROJECT})
