cmake_minimum_required(VERSION 2.8.8)
project(opentaxi)
# include(FindLibSigCXX)
message("compiler : ${CMAKE_CXX_COMPILER}")
include_directories(/usr/include/sigc++-2.0 /usr/lib/x86_64-linux-gnu/sigc++-2.0/include)
add_definitions("-std=c++11")
set(LIBS sigc-2.0 simgrid)

add_executable(testing pingpong.cpp)
target_link_libraries(testing sigc-2.0 ${LIBS})

add_executable(chord chord.cpp node.cpp)
target_link_libraries(chord sigc-2.0 ${LIBS})

# add_subdirectory(chord-c)