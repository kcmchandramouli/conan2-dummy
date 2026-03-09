"""Conanfile for Conan2 Dummy Project to test the different toolchains."""

from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, CMakeDeps, cmake_layout


class Conan2Dummy(ConanFile):
    """Conan2 Dummy Project to test the different toolchains."""

    name = "conan2_dummy"
    version = "1.0.0"
    settings = "os", "arch", "build_type", "compiler"
    license = "ZF"
    url = (
        "**************"
    )
    description = "Conan dummy repository"
    exports_sources = (
        "CMakeLists.txt",
        "src/*",
        "include/*",
    )

    
    def layout(self):
        # Standardize folders; ensures CMake uses the correct source dir in cache
        cmake_layout(self)

    def generate(self):
        """Run the generators for the project."""
        deps = CMakeDeps(self)
        deps.generate()

        toolchain = CMakeToolchain(self, "Ninja")
        toolchain.variables["USE_CPLUSPLUS_FILES"] = (
            str(self.settings.compiler) == "gcc"  # pylint: disable=no-member
        )
        toolchain.generate()

    def build(self):
        """Build the project using CMake."""
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        """Package the project using CMake."""
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        # Name of the built library if applicable
        self.cpp_info.libs = ["conan2_dummy"]
