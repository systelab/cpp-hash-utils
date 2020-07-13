#include "HashUtils/SHA256Service.h"

#include <iostream>
#include <memory>


int main(int argc, char *argv[])
{
    std::unique_ptr<systelab::hash_utils::IHashService> hashService = std::make_unique<systelab::hash_utils::SHA256Service>();

	std::string input = "This is a super-secret to be hashed";
	std::string output = hashService->computeHash(input);

	std::cout << "Input: " << input << std::endl;
	std::cout << "Output: " << output << std::endl;

    return 0;
}
