#pragma once

#include <string>


namespace systelab { namespace hash {

	class IHashService
	{
	public:
		virtual ~IHashService() = default;

		virtual std::string computeHash(const std::string& value) const = 0;
	};

}}
