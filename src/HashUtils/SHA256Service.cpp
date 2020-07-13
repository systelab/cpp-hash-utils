#include "SHA256Service.h"

#include <iomanip>
#include <sstream>

#include <openssl/sha.h>


namespace systelab { namespace hash_utils {

	SHA256Service::SHA256Service() = default;
	SHA256Service::~SHA256Service() = default;

	std::string SHA256Service::computeHash(const std::string& value) const
	{
		unsigned char hash[SHA256_DIGEST_LENGTH];
		SHA256_CTX sha256;
		SHA256_Init(&sha256);
		SHA256_Update(&sha256, value.c_str(), value.size());
		SHA256_Final(hash, &sha256);

		std::stringstream ss;
		for (int i = 0; i < SHA256_DIGEST_LENGTH; i++)
		{
			ss << std::hex << std::setw(2) << std::setfill('0') << (int) hash[i];
		}

		return ss.str();
	}

}}
