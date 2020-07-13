#pragma once

#include "IHashService.h"


namespace systelab { namespace hash_utils {

	class SHA256Service : public IHashService
	{
	public:
		SHA256Service();
		virtual ~SHA256Service();

		std::string computeHash(const std::string& value) const override;
	};

}}
