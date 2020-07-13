#pragma once

#include "IHashService.h"


namespace systelab { namespace hash {

	class MD5HashService : public IHashService
	{
	public:
		MD5HashService();
		virtual ~MD5HashService();

		std::string computeHash(const std::string& value) const override;
	};

}}
