cmake_minimum_required(VERSION 3.2)

project(HashUtilsTestUtilities)

# Configure environment
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR} ${CMAKE_CURRENT_SOURCE_DIR}/cmake)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

# Add project folder into includes
set(CMAKE_INCLUDE_CURRENT_DIR ON)

# Find external dependencies
find_package(HashUtils)

set(GTEST_PACKAGE_NAME gtest)
find_package(${GTEST_PACKAGE_NAME})
if (NOT TARGET ${GTEST_PACKAGE_NAME}::${GTEST_PACKAGE_NAME})
    set(GTEST_PACKAGE_NAME GTest)
    find_package(${GTEST_PACKAGE_NAME})
endif()

# Configure hash utils test utilities project
set(HASH_UTILS_TEST_UTILITIES_PROJECT HashUtilsTestUtilities)
file(GLOB_RECURSE HASH_UTILS_TEST_UTILITIES_PROJECT_SRC "*.cpp")
file(GLOB_RECURSE HASH_UTILS_TEST_UTILITIES_PROJECT_HDR "*.h")

set(EXCLUDE_DIR test_package)
foreach (TMP_PATH ${HASH_UTILS_TEST_UTILITIES_PROJECT_SRC})
    string (FIND ${TMP_PATH} ${EXCLUDE_DIR} EXCLUDE_DIR_FOUND)
    if (NOT ${EXCLUDE_DIR_FOUND} EQUAL -1)
        list (REMOVE_ITEM HASH_UTILS_TEST_UTILITIES_PROJECT_SRC ${TMP_PATH})
    endif ()
endforeach(TMP_PATH)

foreach (TMP_PATH ${HASH_UTILS_TEST_UTILITIES_PROJECT_HDR})
    string (FIND ${TMP_PATH} ${EXCLUDE_DIR} EXCLUDE_DIR_FOUND)
    if (NOT ${EXCLUDE_DIR_FOUND} EQUAL -1)
        list (REMOVE_ITEM HASH_UTILS_TEST_UTILITIES_PROJECT_HDR ${TMP_PATH})
    endif ()
endforeach(TMP_PATH)

add_library(${HASH_UTILS_TEST_UTILITIES_PROJECT} STATIC ${HASH_UTILS_TEST_UTILITIES_PROJECT_SRC} ${HASH_UTILS_TEST_UTILITIES_PROJECT_HDR})
target_link_libraries(${HASH_UTILS_TEST_UTILITIES_PROJECT} HashUtils::HashUtils ${GTEST_PACKAGE_NAME}::${GTEST_PACKAGE_NAME})

# Configure source groups
foreach(FILE ${HASH_UTILS_TEST_UTILITIES_PROJECT_SRC} ${HASH_UTILS_TEST_UTILITIES_PROJECT_HDR})
    get_filename_component(PARENT_DIR "${FILE}" DIRECTORY)
    string(REPLACE "${CMAKE_CURRENT_SOURCE_DIR}" "" GROUP "${PARENT_DIR}")
    string(REPLACE "/" "\\" GROUP "${GROUP}")

    if ("${FILE}" MATCHES ".*\\.cpp")
       set(GROUP "Source Files${GROUP}")
    elseif("${FILE}" MATCHES ".*\\.h")
       set(GROUP "Header Files${GROUP}")
    endif()

    source_group("${GROUP}" FILES "${FILE}")
endforeach()
