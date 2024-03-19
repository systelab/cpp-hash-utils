#include "MD5HashService.h"

#include <iomanip>
#include <sstream>

#include <openssl/md5.h>
#include <openssl/evp.h>


namespace systelab { namespace hash {

	MD5HashService::MD5HashService() = default;
	MD5HashService::~MD5HashService() = default;

	std::string MD5HashService::computeHash(const std::string& value) const
	{
		unsigned char hash[MD5_DIGEST_LENGTH];
		EVP_Digest(value.c_str(), value.size(), hash, nullptr, EVP_md5(), nullptr);

		std::stringstream ss;
		for (int i = 0; i < MD5_DIGEST_LENGTH; i++)
		{
			ss << std::hex << std::setw(2) << std::setfill('0') << (int) hash[i];
		}

		return ss.str();
	}

}}
