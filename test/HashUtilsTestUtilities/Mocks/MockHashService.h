#pragma once

#include "HashUtils/IHashService.h"


namespace systelab { namespace hash { namespace test_utility {

	class MockHashService : public IHashService
	{
	public:
		MockHashService();
		virtual ~MockHashService();

		MOCK_CONST_METHOD1(computeHash, std::string(const std::string&));
	};

}}}

