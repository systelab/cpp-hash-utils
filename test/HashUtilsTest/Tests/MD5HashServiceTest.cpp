#include "stdafx.h"
#include "HashUtils/MD5HashService.h"


using namespace testing;

namespace systelab { namespace hash_utils { namespace unit_test {

	namespace {
		struct MD5HashServiceTestData
		{
			std::string value;
			std::string expectedHash;
		};
		
		// Test data generated using webpage: https://emn178.github.io/online-tools/md5.html
		std::vector<MD5HashServiceTestData> testData = {
			{
				"Patata",
				"a13fd093dfc1c13bce337ceca8ddf3c0"
			},
			{
				"SuperSecretKey",
				"3a2a537576392c0fa9974fe3e73f0678"
			},
			{
				"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque sed",
				"7879b4544ba3e58d06e1bd078936d12d"
			},
			{
				"Vader: Obiwan never told you what happened to your father.\n"
				"Luke: He told me enough; he told me you killed him!\n"
				"Vader: No. I am your father.",
				"b0c0414fd4b89b8127f590435844b01a"
			}
		};
	}

	class MD5HashServiceTest : public testing::TestWithParam<MD5HashServiceTestData>
	{
	public:
		void SetUp()
		{
			m_hashService = std::make_unique<MD5HashService>();
		}

	protected:
		std::unique_ptr<IHashService> m_hashService;
	};


	TEST_P(MD5HashServiceTest, testComputeHashReturnsExpectedValue)
	{
		ASSERT_EQ(GetParam().expectedHash, m_hashService->computeHash(GetParam().value));
	}

#pragma warning (push)
#pragma warning (disable : 4996)
	INSTANTIATE_TEST_CASE_P(Test, MD5HashServiceTest, testing::ValuesIn(testData));
#pragma warning (pop)

}}}
