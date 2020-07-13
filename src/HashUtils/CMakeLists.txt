cmake_minimum_required(VERSION 3.2)

# Find external dependencides
find_package(OpenSSL)

# Add project folder into includes
set(CMAKE_INCLUDE_CURRENT_DIR ON)

# Configure HashUtils static library
set(HASH_UTILS HashUtils)
file(GLOB_RECURSE HASH_UTILS_SRC "*.cpp")
file(GLOB_RECURSE HASH_UTILS_HDR "*.h")
add_library(${HASH_UTILS} STATIC ${HASH_UTILS_SRC} ${HASH_UTILS_HDR})
target_link_libraries(${HASH_UTILS} OpenSSL::OpenSSL)

#Configure source groups
foreach(FILE ${HASH_UTILS_SRC} ${HASH_UTILS_HDR}) 
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
