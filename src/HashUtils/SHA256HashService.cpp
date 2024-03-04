#include "SHA256HashService.h"

#include <iomanip>
#include <sstream>

#include <openssl/sha.h>
#include <openssl/evp.h>


namespace systelab { namespace hash {

	SHA256HashService::SHA256HashService() = default;
	SHA256HashService::~SHA256HashService() = default;

	std::string SHA256HashService::computeHash(const std::string& value) const
	{
		unsigned char hash[SHA256_DIGEST_LENGTH];
		EVP_Digest(value.c_str(), value.size(), hash, nullptr, EVP_sha256(), nullptr);

		std::stringstream ss;
		for (int i = 0; i < SHA256_DIGEST_LENGTH; i++)
		{
			ss << std::hex << std::setw(2) << std::setfill('0') << (int) hash[i];
		}

		return ss.str();
	}

}}
