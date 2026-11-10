{
	"enabled" : False,

	"platform:linux" : {

		"enabled" : True,

	},

	"downloads" : [

		"https://github.com/AcademySoftwareFoundation/openfx/archive/refs/tags/OFX_Release_1.5s.tar.gz",

	],

	"url" : "https://openfx.readthedocs.io",

	"license" : "LICENSE.md",

	"commands" : [

		"mkdir -p {buildDir}/include/openfx/HostSupport",
		"cp include/*.h {buildDir}/include/openfx/",
		"cp include/*.ocio {buildDir}/include/openfx/",
		"cp HostSupport/include/*.h {buildDir}/include/openfx/HostSupport/",

	],

	"manifest" : [

		"include/openfx",

	],

}
