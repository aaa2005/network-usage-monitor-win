cmake_minimum_required(VERSION 3.14)
project(net_usage)

set(CMAKE_CXX_STANDARD 17)


add_subdirectory(extern/pybind11)


# Add your source code
add_library(netusage MODULE src/module.cpp)

# Link pybind11
target_link_libraries(netusage PRIVATE pybind11::module)

# Set output dir (optional)
set_target_properties(netusage PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/bin"
    OUTPUT_NAME "netusage"       # The Python import name
    PREFIX ""                     # Important: removes the 'lib' prefix
    SUFFIX ".pyd"                # For Windows Python extension
)
