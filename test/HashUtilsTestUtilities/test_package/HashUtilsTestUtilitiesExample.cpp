#define _SILENCE_TR1_NAMESPACE_DEPRECATION_WARNING  1

#include <gtest/gtest.h>
#include <gmock/gmock.h>
#include <iostream>

#include "HashUtilsTestUtilities/Mocks/MockHashService.h"


int main(int argc, char *argv[])
{
	systelab::hash::test_utility::MockHashService hashService;
    std::cout << "HashUtils test utilities work as expected" << std::endl;

    return 0;
}
