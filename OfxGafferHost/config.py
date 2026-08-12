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

	"dependencies" : [ "OpenFX", "Expat" ],

	"commands" : [

		"cp -f HostSupport/include/*.h {buildDir}/include/openfx/HostSupport/ &&"
			" g++ -O3 -std=c++17 -fPIC -shared -fvisibility=default"
			" -DOFX_SUPPORTS_OPENGLRENDER -DOFX_SUPPORTS_PARAMETRIC"
			" -I{buildDir}/include/openfx -I{buildDir}/include/openfx/HostSupport -I{buildDir}/include"
			" HostSupport/src/ofxhBinary.cpp HostSupport/src/ofxhClip.cpp HostSupport/src/ofxhHost.cpp"
			" HostSupport/src/ofxhImageEffect.cpp HostSupport/src/ofxhImageEffectAPI.cpp HostSupport/src/ofxhInteract.cpp"
			" HostSupport/src/ofxhMemory.cpp HostSupport/src/ofxhParam.cpp HostSupport/src/ofxhPluginAPICache.cpp"
			" HostSupport/src/ofxhPluginCache.cpp HostSupport/src/ofxhPropertySuite.cpp HostSupport/src/ofxhUtilities.cpp"
			" -L{buildDir}/lib -lexpat -ldl -o {buildDir}/lib/libOfxGafferHost.so",

	],

	"manifest" : [

		"lib/libOfxGafferHost.so",

	],

}
