{

	# Natron openfx-misc, pinned to the commits currently pinned as
	# submodules in the openfx-misc repository, so that the plugin
	# sources are guaranteed to compile against the SDK and supportext
	# trees we build them against.
	"downloads" : [

		"https://github.com/NatronGitHub/openfx/archive/2303ff811bee3ffe085287602f684fe5fe5357e0.tar.gz",
		"https://github.com/NatronGitHub/openfx-misc/archive/0abd46b5a8cbc98fa24579042129460d0aa87b8f.tar.gz",
		"https://github.com/NatronGitHub/openfx-supportext/archive/2485505dbe55885ee92ca9f164e7732a85856a13.tar.gz",
		# CImg header (single file library) for the CImg plugins. Pinned to
		# a 2024 tag contemporary with the openfx-misc pin above.
		"https://github.com/GreycLab/CImg/archive/refs/tags/v.3.3.2.tar.gz",

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

			# CImg.h is expected next to the CImg plugins ("locally-downloaded").
			"cp ../CImg-*/CImg.h ../openfx-misc/CImg/CImg.h",

			# OpenFX SDK Examples : BasicGain (uk.co.thefoundry.BasicGainPlugin), BoxBlur, Invert, etc.
			"make -C Examples -j {jobs} DEBUGNAME=release DEBUGFLAG=-O3",

			# openfx-misc plugins. Misc bundle (net.sf.openfx.*), Shadertoy, the
			# CImg plugins (net.sf.cimg.*) and the individual plugin bundles
			# (ColorBars, Despill, Invert, GodRays, ...). CImg translation units
			# are heavy; keep job counts modest on small machines.
			"make -C ../openfx-misc -j {jobs} DEBUGNAME=release DEBUGFLAG=-O3 OFXPATH=\"$(pwd)\" OFXSEXTPATH=\"$(pwd)/../openfx-supportext\"",
			"make -C ../openfx-misc -j {jobs} nomulti DEBUGNAME=release DEBUGFLAG=-O3 OFXPATH=\"$(pwd)\" OFXSEXTPATH=\"$(pwd)/../openfx-supportext\"",

			# Install the .ofx.bundle directories into the build directory.
			# (CImg plugins sit two levels deep and need their own glob.)
			"mkdir -p {buildDir}/ofxPlugins",
			"cp -r Examples/*/Linux-64-release/*.ofx.bundle {buildDir}/ofxPlugins/",
			"cp -r ../openfx-misc/*/Linux-64-release/*.ofx.bundle {buildDir}/ofxPlugins/",
			"cp -r ../openfx-misc/CImg/*/Linux-64-release/*.ofx.bundle {buildDir}/ofxPlugins/",

			# The openfx-misc plugins are GPL-2.0 licensed. CImg is CeCILL.
			"mkdir -p {buildDir}/doc/licenses/OfxMiscPlugins",
			"cp ../openfx-misc/LICENSE {buildDir}/doc/licenses/OfxMiscPlugins/",
			"cp ../CImg-*/Licence_CeCILL_V2-en.txt {buildDir}/doc/licenses/OfxMiscPlugins/CImg-Licence_CeCILL_V2-en.txt",

		],

	},

	"manifest" : [

		"ofxPlugins",

	],

}