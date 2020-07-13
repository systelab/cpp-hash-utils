#pragma once

#include "IHashService.h"


namespace systelab { namespace hash {

	class SHA256HashService : public IHashService
	{
	public:
		SHA256HashService();
		virtual ~SHA256HashService();

		std::string computeHash(const std::string& value) const override;
	};

}}
