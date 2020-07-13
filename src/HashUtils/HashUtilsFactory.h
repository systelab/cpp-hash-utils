#pragma once

#include "IHashUtilsFactory.h"


namespace systelab { namespace hash {

	class HashUtilsFactory : public IHashUtilsFactory
	{
	public:
		HashUtilsFactory();
		virtual ~HashUtilsFactory();

		std::unique_ptr<IHashService> buildSHA256HashService() const override;
		std::unique_ptr<IHashService> buildMD5HashService() const override;
	};

}}

