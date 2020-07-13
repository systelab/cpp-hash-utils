#pragma once

#include "HashUtils/IHashUtilsFactory.h"
#include "HashUtils/IHashService.h"


namespace systelab { namespace hash { namespace test_utility {

	class MockHashUtilsFactory : public IHashUtilsFactory
	{
	public:
		MockHashUtilsFactory();
		virtual ~MockHashUtilsFactory();

		// Token handling services
		MOCK_CONST_METHOD0(buildSHA256HashServiceProxy, IHashService*());
		std::unique_ptr<IHashService> buildSHA256HashService() const override
		{
			return std::unique_ptr<IHashService>(buildSHA256HashServiceProxy());
		}

		MOCK_CONST_METHOD0(buildMD5HashServiceProxy, IHashService* ());
		std::unique_ptr<IHashService> buildMD5HashService() const override
		{
			return std::unique_ptr<IHashService>(buildMD5HashServiceProxy());
		}
	};

}}}

