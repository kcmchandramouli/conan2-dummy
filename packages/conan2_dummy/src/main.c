#include "conan2_hello_dummy/hello_world.h"
#if (defined USE_CPLUSPLUS_FILES && (USE_CPLUSPLUS_FILES == 1))
#include "conan2_hello_dummy/hello_world.hpp"
#endif

int main() {
    print_hello_world_from_c();
#if (defined USE_CPLUSPLUS_FILES && (USE_CPLUSPLUS_FILES == 1))
    print_hello_world_from_cpp();
#endif
    return 0;
}
