#pragma once

#include <string>


namespace systelab { namespace hash_utils {

	class IHashService
	{
	public:
		virtual ~IHashService() = default;

		virtual std::string computeHash(const std::string& value) const = 0;
	};

}}
