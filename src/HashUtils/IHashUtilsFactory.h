#pragma once

#include <memory>


namespace systelab { namespace hash {

	class IHashService;

	class IHashUtilsFactory
	{
	public:
		virtual ~IHashUtilsFactory() = default;

		virtual std::unique_ptr<IHashService> buildSHA256HashService() const = 0;
		virtual std::unique_ptr<IHashService> buildMD5HashService() const = 0;
	};

}}

