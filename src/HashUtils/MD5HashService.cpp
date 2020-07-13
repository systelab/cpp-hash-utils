#include "MD5HashService.h"

#include <iomanip>
#include <sstream>

#include <openssl/md5.h>


namespace systelab { namespace hash_utils {

	MD5HashService::MD5HashService() = default;
	MD5HashService::~MD5HashService() = default;

	std::string MD5HashService::computeHash(const std::string& value) const
	{
		unsigned char hash[MD5_DIGEST_LENGTH];
		MD5((unsigned char*) value.c_str(), value.size(), hash);

		std::stringstream ss;
		for (int i = 0; i < MD5_DIGEST_LENGTH; i++)
		{
			ss << std::hex << std::setw(2) << std::setfill('0') << (int) hash[i];
		}

		return ss.str();
	}

}}
