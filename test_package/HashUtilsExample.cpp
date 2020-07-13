#include "HashUtils/HashUtilsFactory.h"
#include "HashUtils/IHashService.h"

#include <iostream>
#include <memory>


int main(int argc, char *argv[])
{
	auto hashService = systelab::hash::HashUtilsFactory().buildSHA256HashService();

	std::string input = "This is a super-secret to be hashed";
	std::string output = hashService->computeHash(input);

	std::cout << "Input: " << input << std::endl;
	std::cout << "Output: " << output << std::endl;

    return 0;
}
