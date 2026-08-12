{

	# Natron openfx-misc, pinned to the commits currently pinned as
	# submodules in the openfx-misc repository, so that the plugin
	# sources are guaranteed to compile against the SDK and supportext
	# trees we build them against.
	"downloads" : [

		"https://github.com/NatronGitHub/openfx/archive/2303ff811bee3ffe085287602f684fe5fe5357e0.tar.gz",
		"https://github.com/NatronGitHub/openfx-misc/archive/0abd46b5a8cbc98fa24579042129460d0aa87b8f.tar.gz",
		"https://github.com/NatronGitHub/openfx-supportext/archive/2485505dbe55885ee92ca9f164e7732a85856a13.tar.gz",

	],

	"url" : "https://github.com/NatronGitHub/openfx-misc",

	"license" : None,

	# The openfx-misc build is only supported on Linux.
	"enabled" : False,

	"platform:linux" : {

		"enabled" : True,

		"commands" : [

			# The first download (the OpenFX SDK, whose Examples include
			# the BasicGain and BoxBlur plugins) is the working directory.
			"mv ../openfx-misc-* ../openfx-misc",
			"mv ../openfx-supportext-* ../openfx-supportext",

			# OpenFX SDK Examples : BasicGain (uk.co.thefoundry.BasicGainPlugin), BoxBlur, Invert, etc.
			"make -C Examples -j {jobs} DEBUGNAME=release DEBUGFLAG=-O3",

			# openfx-misc plugins. Misc bundle (net.sf.openfx.*), Shadertoy, and
			# the individual plugin bundles (ColorBars, Despill, Invert, GodRays, ...).
			# CImg plugins are skipped (HAVE_CIMG=0) as they are not required and
			# compile slowly.
			"make -C ../openfx-misc -j {jobs} DEBUGNAME=release DEBUGFLAG=-O3 HAVE_CIMG=0 OFXPATH=\"$(pwd)\" OFXSEXTPATH=\"$(pwd)/../openfx-supportext\"",
			"make -C ../openfx-misc -j {jobs} nomulti DEBUGNAME=release DEBUGFLAG=-O3 HAVE_CIMG=0 OFXPATH=\"$(pwd)\" OFXSEXTPATH=\"$(pwd)/../openfx-supportext\"",

			# Install the .ofx.bundle directories into the build directory.
			"mkdir -p {buildDir}/ofxPlugins",
			"cp -r Examples/*/Linux-64-release/*.ofx.bundle {buildDir}/ofxPlugins/",
			"cp -r ../openfx-misc/*/Linux-64-release/*.ofx.bundle {buildDir}/ofxPlugins/",

			# The openfx-misc plugins are GPL-2.0 licensed.
			"mkdir -p {buildDir}/doc/licenses/OfxMiscPlugins",
			"cp ../openfx-misc/LICENSE {buildDir}/doc/licenses/OfxMiscPlugins/",

		],

	},

	"manifest" : [

		"ofxPlugins",

	],

}