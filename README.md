Conan recipe for Remotery
=========================


This recipe is a source recipe. It is meant to be used like this

```
    conan_cmake_run_target(
        REQUIRES
            remotery/e4ae3baacd@firefalcom/stable
        BASIC_SETUP CMAKE_TARGETS
        BUILD missing
        )

    find_file(REMOTERY_C_PATH NAMES Remotery.c
        HINTS ${CONAN_SRC_DIRS_REMOTERY}
        ${CONAN_SRC_DIRS_REMOTERY_DEBUG} #:TODO: use expression to select one of those two
        ${CONAN_SRC_DIRS_REMOTERY_RELEASE}
        ${CONAN_BUILD_MODULES_PATHS}/src
        NO_DEFAULT_PATH
        REQUIRED
        )


    target_sources(my_target PRIVATE ${REMOTERY_C_PATH})
    target_link_libraries(my_target PUBLIC CONAN_PKG::remotery)
```