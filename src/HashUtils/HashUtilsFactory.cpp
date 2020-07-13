#include "HashUtilsFactory.h"

#include "MD5HashService.h"
#include "SHA256HashService.h"


namespace systelab { namespace hash {

	HashUtilsFactory::HashUtilsFactory() = default;
	HashUtilsFactory::~HashUtilsFactory() = default;

	std::unique_ptr<IHashService> HashUtilsFactory::buildSHA256HashService() const
	{
		return std::make_unique<SHA256HashService>();
	}

	std::unique_ptr<IHashService> HashUtilsFactory::buildMD5HashService() const
	{
		return std::make_unique<MD5HashService>();
	}

}}
