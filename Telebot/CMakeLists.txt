cmake_minimum_required(VERSION 3.15)
project(MyBot)

set(CMAKE_CXX_STANDARD 20)

# Define directories
set(SOURCE_DIR ${CMAKE_SOURCE_DIR}/src)
set(INCLUDE_DIR ${CMAKE_SOURCE_DIR}/include)
set(BIN_DIR ${CMAKE_BINARY_DIR}/bin)

# Collect source files
file(GLOB_RECURSE SOURCES ${SOURCE_DIR}/*.cpp)
file(GLOB_RECURSE HEADERS ${INCLUDE_DIR}/*.hpp)

# Set the output directory for the binary
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${BIN_DIR})

# Add the executable
add_executable(${PROJECT_NAME} ${SOURCES} ${HEADERS})

# Add include directories
target_include_directories(${PROJECT_NAME} PRIVATE ${INCLUDE_DIR} SYSTEM/usr/local/include SYSTEM/usr/include)

# Link libraries
target_link_libraries(${PROJECT_NAME} PRIVATE TgBot boost_system ssl crypto pthread mysqlcppconn)

# Add definitions to address the Boost bind warning
target_compile_definitions(${PROJECT_NAME} PRIVATE
    BOOST_BIND_GLOBAL_PLACEHOLDERS
)
