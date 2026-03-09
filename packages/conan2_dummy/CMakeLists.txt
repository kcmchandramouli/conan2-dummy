
cmake_minimum_required(VERSION 3.24)

project(conan2_dummy)

set(SRC_FOLDER "src")
set(INC_FOLDER "include")

if (USE_CPLUSPLUS_FILES)
   set(_SRCS src/conan2_dummy.c src/conan2_dummy.cpp)
   set(_INCS include/conan2_hello_dummy/hello_world.h include/conan2_hello_dummy/hello_world.hpp)
   add_definitions(-DUSE_CPLUSPLUS_FILES=1)
else ()
   set(_SRCS src/conan2_dummy.c)
   set(_INCS include/conan2_hello_dummy/hello_world.h)
endif ()

add_executable(${PROJECT_NAME} "src/main.c")

add_library(${PROJECT_NAME}_lib STATIC ${_SRCS})

target_include_directories(${PROJECT_NAME}_lib PUBLIC "include")

target_link_libraries(${PROJECT_NAME} PRIVATE ${PROJECT_NAME}_lib)

install(TARGETS conan2_dummy DESTINATION "."
        RUNTIME DESTINATION bin
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
        )

message(STATUS "CMAKE_C_COMPILER_ID=${CMAKE_C_COMPILER_ID}")
# Only add Clang linker options if HIGHTEC toolchains
if(CMAKE_C_COMPILER_ID STREQUAL "Clang")
    target_link_options(${PROJECT_NAME} PRIVATE
        -Wl,-Map=${PROJECT_NAME}.map
        -Wl,--gc-sections
        -Wl,--cref
    )
endif()

if(CMAKE_C_COMPILER_ID STREQUAL "gcc")
   add_test(
      NAME check_output
      COMMAND ${PROJECT_NAME}
   )
   if (USE_CPLUSPLUS_FILES)
      set_property(
                     TEST check_output
                     PROPERTY PASS_REGULAR_EXPRESSION "Hello World from C!" "Hello World from C++!"
                  )
   else ()
      set_property(
                     TEST check_output
                     PROPERTY PASS_REGULAR_EXPRESSION "Hello World from C!"
                  )
   endif ()
endif()
