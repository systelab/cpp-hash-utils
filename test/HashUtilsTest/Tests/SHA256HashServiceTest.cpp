#include "stdafx.h"
#include "HashUtils/SHA256HashService.h"


using namespace testing;

namespace systelab { namespace hash_utils { namespace unit_test {

	namespace {
		struct SHA256HashServiceTestData
		{
			std::string value;
			std::string expectedHash;
		};
		
		// Test data generated using webpage: https://emn178.github.io/online-tools/sha256.html
		std::vector<SHA256HashServiceTestData> testData = {
			{
				"Patata",
				"0cae58ab02970f792b8b75150604a4bfa70b7fc6c40026f684a67aaeedffe8d1"
			},
			{
				"SuperSecretKey",
				"6cc817ae9bdb9d11aa0358ac7c80887ba9c41cf3f30684b690aafaa0d73c05ed"
			},
			{
				"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque sed",
				"db0fa5c852b1f0791472fb9411973186e47f6c343d88ff1737f4f831375561f6"
			},
			{
				"Vader: Obiwan never told you what happened to your father.\n"
				"Luke: He told me enough; he told me you killed him!\n"
				"Vader: No. I am your father.",
				"41eedcbf1ed327853fb695567a2f878142dcde371302162f239749017627b358"
			}
		};
	}

	class SHA256HashServiceTest : public testing::TestWithParam<SHA256HashServiceTestData>
	{
	public:
		void SetUp()
		{
			m_hashService = std::make_unique<SHA256HashService>();
		}

	protected:
		std::unique_ptr<IHashService> m_hashService;
	};


	TEST_P(SHA256HashServiceTest, testComputeHashReturnsExpectedValue)
	{
		ASSERT_EQ(GetParam().expectedHash, m_hashService->computeHash(GetParam().value));
	}

#pragma warning (push)
#pragma warning (disable : 4996)
	INSTANTIATE_TEST_CASE_P(Test, SHA256HashServiceTest, testing::ValuesIn(testData));
#pragma warning (pop)

}}}
