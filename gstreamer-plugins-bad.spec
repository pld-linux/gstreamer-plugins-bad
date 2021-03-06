# TODO:
# - nvenc (BR: cuda >= 6.5, nvEncodeAPI.h >= 5.0, -lnvidia-encode)
# - nvdec (BR: libnvcuvid)
# - OpenSLES (when available on pure Linux, not Android)
#
# Conditional build:
%bcond_without	amr		# amrwbenc output plugin
%bcond_without	bs2b		# bs2b headphone stereo improvement plugin
%bcond_without	bluez		# Bluez plugin
%bcond_without	chromaprint	# chromaprint fingerprint plugin
%bcond_without	dc1394		# dc1394 input plugin
%bcond_without	directfb	# DirectFB videosink plugin
%bcond_without	dts		# DTS audio decoder plugin
%bcond_without	egl		# EGL support in GL output + wayland and wpe elements
%bcond_without	faad		# faad audio decoder plugin
%bcond_without	gles		# GLESv2 support in GL output
%bcond_with	gnustep		# Cocoa support using GNUstep [unsupported since 1.4.5]
%bcond_without	gsm		# gsm audio decoder/encoder plugin
%bcond_without	kate		# Kate text streams plugin
%bcond_without	ladspa		# LADSPA plugins bridge plugin
%bcond_without	libde265	# libde265 H.265 decoder plugin
%bcond_without	lv2		# LV2 plugins bridge plugin
%bcond_without	mfx		# Intel MediaSDK (MFX) plugin
%bcond_without	mjpegtools	# mpeg2enc video encoder plugin
%bcond_without	mms		# mms streaming plugin
%bcond_without	musepack	# musepack audio decoder plugin
%bcond_without	neon		# neonhttpsrc HTTP client plugin
%bcond_without	ofa		# OFA fingerprint plugin
%bcond_without	openal		# OpenAL audiosink plugin
%bcond_with	opencv		# OpenCV effects plugin
%bcond_without	openexr		# OpenEXR EXR decoder plugin
%bcond_without	openh264	# OpenH264 encoder/decoder
%bcond_without	openni2		# OpenNI2 device source plugin
%bcond_without	librsvg		# RSVG SVG decoder/overlay plugin
%bcond_without	sbc		# SBC bluetooth audio codec plugin
%bcond_without	sndfile		# sndfile audio files encoder/decoder plugin
%bcond_without	srtp		# SRTP decoder/encoder plugin
%bcond_without	tinyalsa	# ALSA audiosink using tinyalsa library
%bcond_without	uvch264		# uvch264 cameras plugin
%bcond_without	vdpau		# VDPAU decoder/videopostprocess/videosink plugin
%bcond_without	vulkan		# Vulkan videosink/upload plugin
%bcond_without	wayland		# Wayland videosink plugin, Wayland EGL support, Wayland support in Vulkan plugin
%bcond_without	wpe		# WebKit based web browser plugin
%bcond_without	wildmidi	# wildmidi MIDI files decoder plugin
%bcond_without	x265		# x265 H.265 encoder plugin
%bcond_with	yadif		# YADIF deinterlacing filter plugin
%bcond_without	zvbi		# zvbi-based teletext plugin
%bcond_without	examples	# examples build

%if %{without egl}
%undefine with_wayland
%undefine with_wpe
%endif

%define		gstname		gst-plugins-bad
%define		gstmver		1.0
%define		gst_ver		1.16.3
%define		gstpb_ver	1.16.3
Summary:	Bad GStreamer Streaming-media framework plugins
Summary(pl.UTF-8):	Złe wtyczki do środowiska obróbki strumieni GStreamer
Name:		gstreamer-plugins-bad
Version:	1.16.3
Release:	5
License:	LGPL v2+
Group:		Libraries
Source0:	https://gstreamer.freedesktop.org/src/gst-plugins-bad/%{gstname}-%{version}.tar.xz
# Source0-md5:	8969ea1aec3411c13d0e7dd27ccaaef1
Patch0:		%{name}-libdts.patch
Patch1:		%{name}-mfx.patch
Patch2:		%{name}-neon.patch
URL:		https://gstreamer.freedesktop.org/
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.14
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gobject-introspection-devel >= 1.31.1
BuildRequires:	gstreamer-devel >= %{gst_ver}
BuildRequires:	gstreamer-gl-devel >= %{gst_ver}
BuildRequires:	gstreamer-plugins-base-devel >= %{gstpb_ver}
BuildRequires:	gtk-doc >= 1.12
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	orc-devel >= 0.4.17
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	python >= 2.1
BuildRequires:	rpmbuild(macros) >= 1.98
BuildRequires:	xorg-lib-libX11-devel
%if %{with examples}
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	clutter-devel >= 1.8
BuildRequires:	gtk+3-devel >= 3.4
BuildRequires:	xorg-lib-libXcomposite-devel
%endif
##
## plugins
##
%{?with_directfb:BuildRequires:	DirectFB-devel >= 1:0.9.24}
%{?with_egl:BuildRequires:	EGL-devel}
%{?with_openal:BuildRequires:	OpenAL-devel >= 1.14}
%{?with_openexr:BuildRequires:	OpenEXR-devel}
%{?with_gles:BuildRequires:	OpenGLESv2-devel}
%{?with_openni2:BuildRequires:	OpenNI2-devel >= 0.26}
%{?with_vulkan:BuildRequires:	Vulkan-Loader-devel}
BuildRequires:	alsa-lib-devel >= 0.9.1
BuildRequires:	aom-devel
%{?with_bluez:BuildRequires:	bluez-libs-devel >= 5.0}
BuildRequires:	bzip2-devel
%{?with_librsvg:BuildRequires:	cairo-devel}
BuildRequires:	curl-devel >= 7.35.0
BuildRequires:	dssim-devel
BuildRequires:	exempi-devel >= 1.99.5
BuildRequires:	faac-devel
%{?with_faad:BuildRequires:	faad2-devel >= 2.7}
BuildRequires:	fdk-aac-devel >= 0.1.4
BuildRequires:	flite-devel
BuildRequires:	fluidsynth-devel >= 1.0
BuildRequires:	game-music-emu-devel >= 0.5.6
BuildRequires:	gnutls-devel >= 2.11.3
%if %{with gnustep}
BuildRequires:	gnustep-base-devel
BuildRequires:	gnustep-gui-devel
%endif
BuildRequires:	graphene-devel >= 1.4.0
%{?with_ladspa:BuildRequires:	ladspa-devel >= 1.12}
BuildRequires:	lcms2-devel >= 2.7
BuildRequires:	libass-devel >= 0.10.2
%{?with_bs2b:BuildRequires:	libbs2b-devel >= 3.1.0}
%{?with_chromaprint:BuildRequires:	libchromaprint-devel}
%{?with_dc1394:BuildRequires:	libdc1394-devel >= 2.0.0}
%{?with_libde265:BuildRequires:	libde265-devel >= 0.9}
BuildRequires:	libdrm-devel >= 2.4.55
%{?with_dts:BuildRequires:	libdts-devel}
BuildRequires:	libdvdnav-devel >= 4.1.2
BuildRequires:	libdvdread-devel >= 4.1.2
BuildRequires:	libexif-devel >= 1:0.6.16
%{?with_gsm:BuildRequires:	libgsm-devel}
BuildRequires:	libiptcdata-devel >= 1.0.2
BuildRequires:	libjpeg-devel
%{?with_kate:BuildRequires:	libkate-devel >= 0.1.7}
BuildRequires:	liblrdf-devel
%{?with_mms:BuildRequires:	libmms-devel >= 0.4}
BuildRequires:	libmodplug-devel
BuildRequires:	libnice-devel >= 0.1.14
%{?with_ofa:BuildRequires:	libofa-devel >= 0.9.3}
BuildRequires:	libopenmpt-devel
BuildRequires:	libpng-devel >= 2:1.2.0
%{?with_librsvg:BuildRequires:	librsvg-devel >= 1:2.36.2}
BuildRequires:	librtmp-devel
BuildRequires:	libssh2-devel >= 1.4.3
# for decklink, modplug, soundtouch
%{?with_sndfile:BuildRequires:	libsndfile-devel >= 1.0.16}
# or srtp, libsrtp2 is preferred
%{?with_srtp:BuildRequires:	libsrtp2-devel >= 2.1.0}
BuildRequires:	libstdc++-devel
BuildRequires:	libtheora-devel >= 1.0
%{?with_kate:BuildRequires:	libtiger-devel >= 0.3.2}
%{?with_uvch264:BuildRequires:	libusb-devel >= 1.0}
BuildRequires:	libusrsctp-devel
%{?with_mfx:BuildRequires:	libva-drm-devel}
%{?with_vdpau:BuildRequires:	libvdpau-devel}
BuildRequires:	libvpx-devel
BuildRequires:	libwebp-devel >= 0.2.1
%{?with_x265:BuildRequires:	libx265-devel}
%{?with_vulkan:BuildRequires:	libxcb-devel >= 1.10}
BuildRequires:	libxml2-devel >= 1:2.9.2
%{?with_lv2:BuildRequires:	lilv-devel >= 0.22}
%{?with_mfx:BuildRequires:	mfx_dispatch-devel}
%{?with_mjpegtools:BuildRequires:	mjpegtools-devel >= 2.0.0}
%{?with_musepack:BuildRequires:	libmpcdec-devel}
%{?with_neon:BuildRequires:	neon-devel >= 0.27.0}
# for hls, could also use libgcrypt>=1.2.0 or openssl
BuildRequires:	nettle-devel
%if %{with opencv}
BuildRequires:	opencv-devel >= 1:3.0.0
BuildRequires:	opencv-devel < 1:4.2.0
%endif
%{?with_openh264:BuildRequires:	openh264-devel >= 1.3.0}
# or openjpeg >= 1.5, openjpeg2 is preferred
BuildRequires:	openjpeg2-devel >= 2.1
# for dtls
BuildRequires:	openssl-devel >= 1.0.1
BuildRequires:	opus-devel >= 0.9.4
BuildRequires:	pango-devel >= 1:1.22.0
%{?with_sbc:BuildRequires:	sbc-devel >= 1.0}
BuildRequires:	soundtouch-devel >= 1.4
BuildRequires:	spandsp-devel >= 1:0.0.6
BuildRequires:	srt-devel
%{?with_tinyalsa:BuildRequires:	tinyalsa-devel}
%{?with_uvch264:BuildRequires:	udev-glib-devel}
BuildRequires:	vo-aacenc-devel >= 0.1.0
%{?with_amr:BuildRequires:	vo-amrwbenc-devel >= 0.1.0}
# wayland-client, wayland-cursor, wayland-scanner
%{?with_wayland:BuildRequires:	wayland-devel >= 1.11.0}
%{?with_wayland:BuildRequires:	wayland-protocols >= 1.15}
BuildRequires:	webrtc-audio-processing-devel < 0.4
BuildRequires:	webrtc-audio-processing-devel >= 0.2
%{?with_wildmidi:BuildRequires:	wildmidi-devel >= 0.4}
%{?with_wpe:BuildRequires:	wpe-webkit-devel >= 2.24}
%{?with_wpe:BuildRequires:	wpebackend-fdo-devel >= 1.0}
BuildRequires:	xorg-lib-libX11-devel
%{?with_wpe:BuildRequires:	xorg-lib-libxkbcommon-devel}
BuildRequires:	zbar-devel >= 0.9
%{?with_zvbi:BuildRequires:	zvbi-devel >= 0.2}
Requires:	glib2 >= 1:2.40.0
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	libxml2 >= 1:2.8
Requires:	orc >= 0.4.17
Obsoletes:	gstreamer-cdaudio < 1.0
Obsoletes:	gstreamer-quicktime < 0.10
Obsoletes:	gstreamer-schroedinger < 1.14
Obsoletes:	gstreamer-vcd < 0.10
Conflicts:	openwebrtc < 0.3.0-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		gstlibdir	%{_libdir}/gstreamer-%{gstmver}
%define		gstdatadir	%{_datadir}/gstreamer-%{gstmver}

%description
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related. Its plugin-based architecture means
that new data types or processing capabilities can be added simply by
installing new plugins.

%description -l pl.UTF-8
GStreamer to środowisko obróbki danych strumieniowych, bazujące na
grafie filtrów operujących na danych medialnych. Aplikacje używające
tej biblioteki mogą robić wszystko od przetwarzania dźwięku w czasie
rzeczywistym, do odtwarzania filmów i czegokolwiek innego związego z
mediami. Architektura bazująca na wtyczkach pozwala na łatwe dodawanie
nowych typów danych lub możliwości obróbki.

%package devel
Summary:	Header files and API documentation for gstapp library
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja API biblioteki gstapp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gstreamer-devel >= %{gst_ver}

%description devel
Header files and API documentation for gstapp library.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja API biblioteki gstapp.

## Plugins ##

%package -n gstreamer-aac
Summary:	GStreamer plugin for AAC audio encoding and decoding
Summary(pl.UTF-8):	Wtyczka dla GStreamera do kodowania i dekodowania plików audio AAC
Group:		Libraries
Requires:	faad2-libs >= 2.7
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}

%description -n gstreamer-aac
GStreamer plugin for AAC audio encoding and decoding.

%description -n gstreamer-aac -l pl.UTF-8
Wtyczka GStreamera do kodowania i dekodowania plików audio AAC.

%package -n gstreamer-amrwbenc
Summary:	GStreamer plugin for AMR-WB audio encoding
Summary(pl.UTF-8):	Wtyczka GStreamera do kodowania dźwięku w formacie AMR-WB
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	vo-amrwbenc >= 0.1.0

%description -n gstreamer-amrwbenc
GStreamer plugin for AMR-WB audio encoding, using VisualOn library.

%description -n gstreamer-amrwbenc -l pl.UTF-8
Wtyczka GStreamera do kodowania dźwięku w formacie AMR-WB,
wykorzystująca bibliotekę VisualOn.

%package -n gstreamer-ass
Summary:	GStreamer plugin for ASS/SSA subtitles rendering
Summary(pl.UTF-8):	Wtyczka GStreamera do renderowania napisów ASS/SSA
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	libass >= 0.10.2

%description -n gstreamer-ass
GStreamer plugin for ASS/SSA subtitles rendering.

%description -n gstreamer-ass -l pl.UTF-8
Wtyczka GStreamera do renderowania napisów ASS/SSA.

%package -n gstreamer-audio-effects-bad
Summary:	Bad GStreamer audio effects plugins
Summary(pl.UTF-8):	Złe wtyczki efektów dźwiękowych dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Obsoletes:	gstreamer-audio-effects < 0.10

%description -n gstreamer-audio-effects-bad
Bad GStreamer audio effects plugins.

%description -n gstreamer-audio-effects-bad -l pl.UTF-8
Złe wtyczki efektów dźwiękowych dla GStreamera.

%package -n gstreamer-audiosink-tinyalsa
Summary:	GStreamer ALSA audio output plugin using tinyalsa library
Summary(pl.UTF-8):	Wtyczka wyjścia dźwięku ALSA dla GStreamera, wykorzystująca bibliotekę tinyalsa
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Provides:	gstreamer-audiosink = %{version}

%description -n gstreamer-audiosink-tinyalsa
GStreamer ALSA audio output plugin using tinyalsa library.

%description -n gstreamer-audiosink-tinyalsa -l pl.UTF-8
Wtyczka wyjścia dźwięku ALSA dla GStreamera, wykorzystująca bibliotekę
tinyalsa.

%package -n gstreamer-aom
Summary:	GStreamer AOM plugin
Summary(pl.UTF-8):	Wtyczka AOM dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}

%description -n gstreamer-aom
GStreamer AV1 encoder/decoder plugin based on AOM library.

%description -n gstreamer-aom -l pl.UTF-8
Oparta na bibliotece AOM wtyczka GStreamera kodująca/dekodująca format
AV1.

%package -n gstreamer-bs2b
Summary:	GStreamer bs2b plugin
Summary(pl.UTF-8):	Wtyczka bs2b dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	libbs2b >= 3.1.0

%description -n gstreamer-bs2b
GStreamer plugin to improve headphone listening of stereo audio
records using the b2sb library.

%description -n gstreamer-bs2b -l pl.UTF-8
Wtyczka GStreamera poprawiająca odsłuchiwanie nagrań stereofonicznych
przez słuchawki przy użyciu biblioteki bs2b.

%package -n gstreamer-bluez
Summary:	GStreamer plugin for Bluez-based bluetooth support
Summary(pl.UTF-8):	Wtyczka GStreamera do obsługi bluetooth w oparciu o Bluez
Group:		Libraries
Requires:	bluez-libs >= 5.0
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Obsoletes:	gstreamer-bluetooth < 1.2

%description -n gstreamer-bluez
GStreamer plugin for Bluez-based bluetooth support.

%description -n gstreamer-bluez -l pl.UTF-8
Wtyczka GStreamera do obsługi bluetooth w oparciu o Bluez.

%package -n gstreamer-chromaprint
Summary:	GStreamer Chromaprint audio fingerprinting plugin
Summary(pl.UTF-8):	Wtyczka Chromaprint do odcisków identyfikacyjnych dźwięku dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}

%description -n gstreamer-chromaprint
GStreamer Chromaprint audio fingerprinting plugin.

%description -n gstreamer-chromaprint -l pl.UTF-8
Wtyczka GStreamera wykonująca odciski identyfikacyjne dźwięku przy
użyciu biblioteki Chromaprint.

%package -n gstreamer-closedcaption
Summary:	GStreamer Closedcaption plugin
Summary(pl.UTF-8):	Wtyczka Closedcaption dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	pango >= 1:1.22.0

%description -n gstreamer-closedcaption
Plugin for Closedcaption support.

%description -n gstreamer-closedcaption -l pl.UTF-8
Wtyczka GStreamera obsługująca Closedcaption.

%package -n gstreamer-curl
Summary:	GStreamer cURL network sink plugin
Summary(pl.UTF-8):	Wtyczka wyjścia sieciowego cURL dla GStreamera
Group:		Libraries
Requires:	curl-libs >= 7.35.0
Requires:	gstreamer >= %{gst_ver}
Requires:	libssh2 >= 1.4.3

%description -n gstreamer-curl
GStreamer network sink plugin that uses libcurl as a client to upload
data to a server (e.g. HTTP or FTP).

%description -n gstreamer-curl -l pl.UTF-8
Wtyczka wyjścia sieciowego GStreamera wykorzystująca libcurl jako
klienta do wysyłania danych na serwer (np. HTTP lub FTP).

%package -n gstreamer-dc1394
Summary:	GStreamer 1394 IIDC (Firewire digital cameras) video source plugin
Summary(pl.UTF-8):	Wtyczka źródła obrazu 1394 IIDC (z kamer cyfrowych Firewire) dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}

%description -n gstreamer-dc1394
GStreamer 1394 IIDC (Firewire digital cameras) video source plugin.

%description -n gstreamer-dc1394 -l pl.UTF-8
Wtyczka źródła obrazu 1394 IIDC (z kamer cyfrowych Firewire) do
GStreamera.

%package -n gstreamer-dtls
Summary:	GStreamer DTLS decoder and encoder plugin
Summary(pl.UTF-8):	Wtyczka kodera i dekodera DTLS dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	openssl >= 1.0.1

%description -n gstreamer-dtls
GStreamer DTLS decoder and encoder plugin.

%description -n gstreamer-dtls -l pl.UTF-8
Wtyczka kodera i dekodera DTLS dla GStreamera.

%package -n gstreamer-dts
Summary:	GStreamer DTS plugin
Summary(pl.UTF-8):	Wtyczka DTS dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}

%description -n gstreamer-dts
Plugin for DTS Coherent Acoustics support.

%description -n gstreamer-dts -l pl.UTF-8
Wtyczka GStreamera obsługująca DTS Coherent Acoustics.

%package -n gstreamer-fdkaac
Summary:	GStreamer FDK-AAC plugin
Summary(pl.UTF-8):	Wtyczka FDK-AAC dla GStreamera
Group:		Libraries
Requires:	fdk-aac >= 0.1.4
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}

%description -n gstreamer-fdkaac
GStreamer FDK AAC audio decoder/encoder plugin.

%description -n gstreamer-fdkaac -l pl.UTF-8
Wtyczka GStreamera do kodowania i dekodowania dźwięku FDK AAC.

%package -n gstreamer-flite
Summary:	GStreamer Flite plugin
Summary(pl.UTF-8):	Wtyczka Flite dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}

%description -n gstreamer-flite
Plugin for Flite support.

%description -n gstreamer-flite -l pl.UTF-8
Wtyczka GStreamera obsługująca Flite.

%package -n gstreamer-fluidsynth
Summary:	GStreamer FluidSynth MIDI plugin
Summary(pl.UTF-8):	Wtyczka FluidSynth MIDI dla GStreamera
Group:		Libraries
# for generic gstmidi plugin
Requires:	%{name} = %{version}-%{release}
Requires:	fluidsynth >= 1.0
Requires:	gstreamer >= %{gst_ver}

%description -n gstreamer-fluidsynth
GStreamer FluidSynth MIDI plugin.

%description -n gstreamer-fluidsynth -l pl.UTF-8
Wtyczka FluidSynth MIDI dla GStreamera.

%package -n gstreamer-gme
Summary:	GStreamer GME Audio Decoder plugin
Summary(pl.UTF-8):	Wtyczka GStreamera dekodująca dźwięk GME
Group:		Libraries
Requires:	game-music-emu >= 0.5.6
Requires:	gstreamer >= %{gst_ver}
Obsoletes:	gstreamer-nsf < 1.6
Obsoletes:	gstreamer-spc < 1.16.0

%description -n gstreamer-gme
GStreamer GME Audio Decoder plugin.

%description -n gstreamer-gme -l pl.UTF-8
Wtyczka GStreamera dekodująca dźwięk GME.

%package -n gstreamer-gsettings
Summary:	GStreamer GSettings plugin
Summary(pl.UTF-8):	Wtyczka GSettings dla GStreamera
Group:		Libraries
Requires:	glib2 >= 1:2.40.0
Requires:	gstreamer >= %{gst_ver}

%description -n gstreamer-gsettings
GStreamer GSettings plugin.

%description -n gstreamer-gsettings -l pl.UTF-8
Wtyczka GSettings dla GStreamera.

%package -n gstreamer-gsm
Summary:	GStreamer plugin for GSM lossy audio format
Summary(pl.UTF-8):	Wtyczka GStreamera obsługująca stratny format dźwięku GSM
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}

%description -n gstreamer-gsm
Output plugin for GStreamer to convert to GSM lossy audio format.

%description -n gstreamer-gsm -l pl.UTF-8
Wtyczka wyjścia dźwięku GSteamera konwertująca do stratnego formatu
GSM.

%package -n gstreamer-iqa
Summary:	GStreamer analyzer plugin to provide various Image Quality Assessment metrics
Summary(pl.UTF-8):	Wtyczka analizująca GStreamera zapewniająca różne wskaźniki oceny jakości obrazu
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}

%description -n gstreamer-iqa
GStreamer analyzer plugin to provide various Image Quality Assessment
metrics.

%description -n gstreamer-iqa -l pl.UTF-8
Wtyczka analizująca GStreamera zapewniająca różne wskaźniki oceny
jakości obrazu.

%package -n gstreamer-kate
Summary:	GStreamer plugin for Kate text streams
Summary(pl.UTF-8):	Wtyczka obsługująca strumienie tekstowe Kate dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	libkate >= 0.1.7
Requires:	libtiger >= 0.3.2

%description -n gstreamer-kate
GStreamer plugin for Kate text streams.

%description -n gstreamer-kate -l pl.UTF-8
Wtyczka obsługująca strumienie tekstowe Kate dla GStreamera.

%package -n gstreamer-videosink-kms
Summary:	GStreamer KMS output plugin
Summary(pl.UTF-8):	Wtyczka wyjścia obrazu KMS dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	libdrm >= 2.4.55
Provides:	gstreamer-videosink = %{version}

%description -n gstreamer-videosink-kms
GStreamer KMS output plugin.

%description -n gstreamer-videosink-kms -l pl.UTF-8
Wtyczka wyjścia obrazu KMS dla GStreamera.

%package -n gstreamer-ladspa
Summary:	GStreamer wrapper for LADSPA plugins
Summary(pl.UTF-8):	Wrapper do wtyczek LADSPA dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}

%description -n gstreamer-ladspa
Plugin which wraps LADSPA plugins for use by GStreamer applications.

%description -n gstreamer-ladspa -l pl.UTF-8
Wtyczka pozwalająca na używanie wtyczek LADSPA przez aplikacje
GStreamera.

%package -n gstreamer-libde265
Summary:	GStreamer libde265 H.265 decoder plugin
Summary(pl.UTF-8):	Wtyczka dekodera H.265 libde265 dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	libde265 >= 0.9

%description -n gstreamer-libde265
GStreamer libde265 plugin - H.265 decoder.

%description -n gstreamer-libde265 -l pl.UTF-8
Wtyczka libde265 dla GStreamera - dekoder H.265.

%package -n gstreamer-lv2
Summary:	GStreamer wrapper for LV2 plugins
Summary(pl.UTF-8):	Wrapper do wtyczek LV2 dla GStreamera
Group:		Libraries
# for libgstsignalprocessor
Requires:	%{name} = %{version}-%{release}
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	lilv >= 0.22

%description -n gstreamer-lv2
Plugin which wraps LV2 plugins for use by GStreamer applications.

%description -n gstreamer-lv2 -l pl.UTF-8
Wtyczka pozwalająca na używanie wtyczek LV2 przez aplikacje
GStreamera.

%package -n gstreamer-mjpegtools
Summary:	GStreamer mpeg2enc plugin
Summary(pl.UTF-8):	Wtyczka mpeg2enc dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	mjpegtools-libs >= 2.0.0

%description -n gstreamer-mjpegtools
GStreamer mpeg2enc plugin (based on mjpegtools libraries).

%description -n gstreamer-mjpegtools -l pl.UTF-8
Wtyczka mpeg2enc dla GStreamera (oparta na bibliotekach mjpegtools).

%package -n gstreamer-mms
Summary:	GStreamer mms plugin
Summary(pl.UTF-8):	Wtyczka mms dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	libmms >= 0.4

%description -n gstreamer-mms
GStreamer mms plugin.

%description -n gstreamer-mms -l pl.UTF-8
Wtyczka mms dla GStreamera.

%package -n gstreamer-msdk
Summary:	Intel MediaSDK (MFX) plugin for GStreamer
Summary(pl.UTF-8):	Wtyczka MediaSDK (MFX) dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}

%description -n gstreamer-msdk
GStreamer video decoder/encoder based on Intel MediaSDK (MFX) library.

%description -n gstreamer-msdk -l pl.UTF-8
Wtyczka kodera/dekodera obrazu GStreamera oparta na bibliotece Intel
MediaSDK (MFX).

%package -n gstreamer-musepack
Summary:	GStreamer musepack plugin
Summary(pl.UTF-8):	Wtyczka musepack dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}

%description -n gstreamer-musepack
GStreamer musepack plugin.

%description -n gstreamer-musepack -l pl.UTF-8
Wtyczka musepack dla GStreamera.

%package -n gstreamer-neon
Summary:	GStreamer neon HTTP source plugin
Summary(pl.UTF-8):	Wtyczka źródła HTTP neon dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	neon >= 0.27.0

%description -n gstreamer-neon
GStreamer neon HTTP source plugin.

%description -n gstreamer-neon -l pl.UTF-8
Wtyczka źródła HTTP neon dla GStreamera.

%package -n gstreamer-ofa
Summary:	GStreamer OFA fingerprint plugin
Summary(pl.UTF-8):	Wtyczka odcisków OFA dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	libofa >= 0.9.3

%description -n gstreamer-ofa
GStreamer OFA plugin to calculate MusicIP fingerprints from audio
files.

%description -n gstreamer-ofa -l pl.UTF-8
Wtyczka OFA dla GStreamera, służąca do obliczania odcisków MusicIP
plików dźwiękowych.

%package -n gstreamer-openal
Summary:	GStreamer OpenAL audio input/output plugin
Summary(pl.UTF-8):	Wtyczka wejścia/wyjścia dźwięku OpenAL dla GStreamera
Group:		Libraries
Requires:	OpenAL >= 1.14
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Provides:	gstreamer-audiosink = %{version}

%description -n gstreamer-openal
GStreamer OpenAL support plugin, providing audio sink and source.

%description -n gstreamer-openal -l pl.UTF-8
Wtyczka GStreamera obsługująca OpenAL, zapewniająca wyjście i źródło
dźwięku.

%package -n gstreamer-opencv
Summary:	GStreamer OpenCV plugin
Summary(pl.UTF-8):	Wtyczka OpenCV dla GStreamera
Group:		Libraries
# for locales
Requires:	%{name} = %{version}-%{release}
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-opencv-libs = %{version}-%{release}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}

%description -n gstreamer-opencv
GStreamer OpenCV plugin. It contains the following elements:
facedetect, faceblur, edgedetect, cvsobel, cvsmooth, cvlaplace,
cverode, cvequalizehist, cvdilate, textwrite, templatematch,
pyramidsegment.

%description -n gstreamer-opencv -l pl.UTF-8
Wtyczka OpenCV dla GStreamera. Zawiera następujące elementy:
facedetect, faceblur, edgedetect, cvsobel, cvsmooth, cvlaplace,
cverode, cvequalizehist, cvdilate, textwrite, templatematch,
pyramidsegment.

%package -n gstreamer-opencv-libs
Summary:	GStreamer OpenCV shared library
Summary(pl.UTF-8):	Biblioteka współdzielona GStreamer OpenCV
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	opencv >= 1:2.3.0

%description -n gstreamer-opencv-libs
GStreamer OpenCV shared library.

%description -n gstreamer-opencv-libs -l pl.UTF-8
Biblioteka współdzielona GStreamer OpenCV.

%package -n gstreamer-opencv-devel
Summary:	Header files for GStreamer OpenCV library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki GStreamer OpenCV
Group:		Development/Libraries
Requires:	gstreamer-devel >= %{gst_ver}
Requires:	gstreamer-opencv-libs = %{version}-%{release}
Requires:	gstreamer-plugins-base-devel >= %{gstpb_ver}

%description -n gstreamer-opencv-devel
Header files for GStreamer OpenCV library.

%description -n gstreamer-opencv-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki GStreamer OpenCV.

%package -n gstreamer-openexr
Summary:	GStreamer OpenEXR plugin
Summary(pl.UTF-8):	Wtyczka OpenEXR dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}

%description -n gstreamer-openexr
GStreamer OpenEXR plugin - OpenEXR-based EXR streams decoder.

%description -n gstreamer-openexr -l pl.UTF-8
Wtyczka OpenEXR dla GStreamera - dekoder strumieni EXR oparty na
bibliotece OpenEXR.

%package -n gstreamer-openh264
Summary:	GStreamer OpenH264 encoder/decoder plugin
Summary(pl.UTF-8):	Wtyczka kodera/dekodera OpenH264 dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	openh264 >= 1.3.0

%description -n gstreamer-openh264
GStreamer OpenH264 plugin - H.264 encoder/decoder.

%description -n gstreamer-openh264 -l pl.UTF-8
Wtyczka OpenH264 dla GStreamera - koder/dekoder H.264.

%package -n gstreamer-openjpeg
Summary:	GStreamer OpenJPEG plugin
Summary(pl.UTF-8):	Wtyczka OpenJPEG dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Obsoletes:	gstreamer-jasper < 1.0

%description -n gstreamer-openjpeg
GStreamer OpenJPEG plugin - OpenJPEG-based JPEG2000 decoder/encoder.

%description -n gstreamer-openjpeg -l pl.UTF-8
Wtyczka OpenJPEG dla GStreamera - koder/dekoder JPEG2000 oparty na
bibliotece OpenJPEG.

%package -n gstreamer-openmpt
Summary:	GStreamer OpenMPT plugin
Summary(pl.UTF-8):	Wtyczka OpenMPT dla GStreamera
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}

%description -n gstreamer-openmpt
GStreamer OpenMPT module player plugin.

%description -n gstreamer-openmpt -l pl.UTF-8
Wtyczka GStreamera OpenMPT do odtwarzania modułów.

%package -n gstreamer-openni2
Summary:	GStreamer OpenNI2 video input plugin
Summary(pl.UTF-8):	Wtyczka wejścia obrazu OpenNI2 dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}

%description -n gstreamer-openni2
GStreamer OpenNI2 plugin to extract readings from an OpenNI supported
device (Kinect etc.).

%description -n gstreamer-openni2 -l pl.UTF-8
Wtyczka OpenNI2 dla GStreamera, pobierająca odczyty z urządzeń
obsługiwanych przez bibliotekę OpenNI (np. Kinect).

%package -n gstreamer-opusparse
Summary:	GStreamer OPUS audio decoder/encoder plugin
Summary(pl.UTF-8):	Wtyczka kodera/dekodera dźwięku OPUS dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	opus >= 0.9.4
Obsoletes:	gstreamer-celt < 1.2

%description -n gstreamer-opusparse
GStreamer OPUS audio decoder/encoder plugin.

%description -n gstreamer-opusparse -l pl.UTF-8
Wtyczka GStreamera kodująca/dekodująca dźwięk w formacie OPUS.

%package -n gstreamer-resindvd
Summary:	GStreamer Resin DVD playback plugin
Summary(pl.UTF-8):	Wtyczka odtwarzania Resin DVD dla GStreamera
Group:		Libraries
# for locales
Requires:	%{name} = %{version}-%{release}
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}

%description -n gstreamer-resindvd
GStreamer Resin DVD playback plugin.

%description -n gstreamer-resindvd -l pl.UTF-8
Wtyczka odtwarzania Resin DVD dla GStreamera.

%package -n gstreamer-rsvg
Summary:	GStreamer plugin for decoding SVG images
Summary(pl.UTF-8):	Wtyczka GStreamera do dekodowania obrazów SVG
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	librsvg >= 1:2.36.2

%description -n gstreamer-rsvg
GStreamer plugin for decoding SVG images.

%description -n gstreamer-rsvg -l pl.UTF-8
Wtyczka GStreamera do dekodowania obrazów SVG.

%package -n gstreamer-rtmp
Summary:	RTMP stream input plugin for GStreamer
Summary(pl.UTF-8):	Wtyczka strumieni wejściowych RTMP dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Conflicts:	gstreamer-plugins-bad < 0.10.22

%description -n gstreamer-rtmp
GStreamer plugin that reads data from a local or remote location
specified by an URI, using any protocol supported by the RTMP library,
i.e. rtmp, rtmpt, rtmps, rtmpe, rtmpfp, rtmpte and rtmpts.

%description -n gstreamer-rtmp -l pl.UTF-8
Wtyczka GStreamera czytająca dane z lokalnego lub zdalnego miejsca
określonego URI przy użyciu dowolnego protokołu obsługiwanego przez
bibliotekę RTMP: rtmp, rtmpt, rtmps, rtmpe, rtmpfp, rtmpte lub rtmpts.

%package -n gstreamer-sbc
Summary:	GStreamer SBC plugin
Summary(pl.UTF-8):	Wtyczka SBC dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	sbc >= 1.0

%description -n gstreamer-sbc
SBC bluetooth audio codec plugin for GStreamer.

%description -n gstreamer-sbc -l pl.UTF-8
Wtyczka kodeka dźwięku bluetooth SBC dla GStreamera.

%package -n gstreamer-sctp
Summary:	GStreamer plugin for encoding/decoding SCTP
Summary(pl.UTF-8):	Wtyczka GStremaera do kodowania/dekodowania SCTP
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}

%description -n gstreamer-sctp
GStreamer plugin for encoding/decoding SCTP.

%description -n gstreamer-sctp -l pl.UTF-8
Wtyczka GStremaera do kodowania/dekodowania SCTP.

%package -n gstreamer-sndfile
Summary:	GStreamer sndfile plugin
Summary(pl.UTF-8):	Wtyczka sndfile dla GStreamera
Group:		Libraries
# for locales
Requires:	%{name} = %{version}-%{release}
Requires:	gstreamer >= %{gst_ver}
Requires:	libsndfile >= 1.0.16

%description -n gstreamer-sndfile
GStreamer sndfile source plugin.

%description -n gstreamer-sndfile -l pl.UTF-8
Wtyczka sndfile dla GStreamera.

%package -n gstreamer-soundtouch
Summary:	GStreamer soundtouch plugin
Summary(pl.UTF-8):	Wtyczka soundtouch dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	soundtouch >= 1.4

%description -n gstreamer-soundtouch
GStreamer soundtouch source plugin - audio pitch controller.

%description -n gstreamer-soundtouch -l pl.UTF-8
Wtyczka soundtouch dla GStreamera, sterująca wysokością dźwięku.

%package -n gstreamer-spandsp
Summary:	GStreamer SpanDSP plugin
Summary(pl.UTF-8):	Wtyczka SpanDSP dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	spandsp >= 0.0.6

%description -n gstreamer-spandsp
GStreamer SpanDSP plugin - audio effect that allows packet loss
concealment.

%description -n gstreamer-spandsp -l pl.UTF-8
Wtyczka SpanDSP dla GStreamera - efekt dźwiękowy umożliwiający
ukrywanie strat pakietów.

%package -n gstreamer-srt
Summary:	GStreamer SRT plugin
Summary(pl.UTF-8):	Wtyczka SRT dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}

%description -n gstreamer-srt
GStreamer sink plugin to transfer data via SRT.

%description -n gstreamer-srt -l pl.UTF-8
Wtyczka GStreamera do przesyłania danych przez SRT.

%package -n gstreamer-srtp
Summary:	GStreamer plugin for encoding/decoding SRTP
Summary(pl.UTF-8):	Wtyczka GStremaera do kodowania/dekodowania SRTP
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	libsrtp2-devel >= 2.1.0

%description -n gstreamer-srtp
GStreamer plugin for encoding/decoding SRTP.

%description -n gstreamer-srtp -l pl.UTF-8
Wtyczka GStremaera do kodowania/dekodowania SRTP.

%package -n gstreamer-teletextdec
Summary:	teletext plugin for GStreamer
Summary(pl.UTF-8):	Wtyczka teletext dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}

%description -n gstreamer-teletextdec
Teletext decoder plugin for GStreamer.

%description -n gstreamer-teletextdec -l pl.UTF-8
Wtyczka GStreamera dekodująca teletekst.

%package -n gstreamer-ttml
Summary:	GStreamer TTML subtitles plugin
Summary(pl.UTF-8):	Wtyczka podpisów TTML dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	libxml2 >= 1:2.9.2
Requires:	pango >= 1:1.22.0

%description -n gstreamer-ttml
GStreamer TTML subtitles plugin.

%description -n gstreamer-ttml -l pl.UTF-8
Wtyczka podpisów TTML dla GStreamera.

%package -n gstreamer-uvch264
Summary:	GStreamer plugin for UVC compliant H264 encoding cameras
Summary(pl.UTF-8):	Wtyczka GStreamera do kamer kodujących w H264 zgodnych z UVC
Group:		Libraries
# for libgstbasecamerabin
Requires:	%{name} = %{version}-%{release}
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}

%description -n gstreamer-uvch264
GStreamer plugin for UVC compliant H264 encoding cameras.

%description -n gstreamer-uvch264 -l pl.UTF-8
Wtyczka GStreamera do kamer kodujących w H264 zgodnych z UVC.

%package -n gstreamer-vdpau
Summary:	GStreamer VDPAU plugin
Summary(pl.UTF-8):	Wtyczka GStreamera VDPAU
Group:		Libraries
# for libgstcodecparsers
Requires:	%{name} = %{version}-%{release}
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
# videosink commented out in gstvdpau.c?
#Provides:	gstreamer-videosink = %{version}

%description -n gstreamer-vdpau
GStreamer VDPAU plugin. It currently implements MPEG decoding.

%description -n gstreamer-vdpau -l pl.UTF-8
Wtyczka GStreamera VDPAU. Obecnie ma zaimplementowane dekodowanie
obrazu MPEG.

%package -n gstreamer-videosink-directfb
Summary:	GStreamer DirectFB output plugin
Summary(pl.UTF-8):	Wtyczka wyjścia obrazu DirectFB dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Provides:	gstreamer-videosink = %{version}

%description -n gstreamer-videosink-directfb
GStreamer DirectFB output plugin.

%description -n gstreamer-videosink-directfb -l pl.UTF-8
Wtyczka wyjścia obrazu DirectFB dla GStreamera.

%package -n gstreamer-videosink-wayland
Summary:	GStreamer plugin for outputing to Wayland
Summary(pl.UTF-8):	Wtyczka wyjścia Wayland dla GStreamera
Group:		Libraries
# for libgstgl
Requires:	%{name} = %{version}-%{release}
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	libdrm >= 2.4.55
Requires:	wayland >= 1.11.0
Provides:	gstreamer-videosink = %{version}

%description -n gstreamer-videosink-wayland
Plugin for sending output to the Wayland architecture.

%description -n gstreamer-videosink-wayland -l pl.UTF-8
Wtyczka przekazująca wyjście do architektury Wayland.

%package -n gstreamer-voaacenc
Summary:	AAC encoder plugin for GStreamer
Summary(pl.UTF-8):	Wtyczka kodera dźwięku AAC dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	vo-aacenc >= 0.1.0

%description -n gstreamer-voaacenc
AAC audio encoder plugin for GStreamer using VisualOn library.

%description -n gstreamer-voaacenc -l pl.UTF-8
Wtyczka kodera dźwięku AAC dla GStreamera, wykorzystująca bibliotekę
VisualOn.

%package -n gstreamer-vulkan
Summary:	GStreamer Vulkan plugin
Summary(pl.UTF-8):	Wtyczka GStreamera Vulkan
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	libxcb >= 1.10
Provides:	gstreamer-videosink = %{version}

%description -n gstreamer-vulkan
GStreamer Vulkan video sink and filter (uploader) plugin.

%description -n gstreamer-vulkan -l pl.UTF-8
Wtyczka GStreamera Vulkan - wyjście i filtr obrazu.

%package -n gstreamer-webp
Summary:	GStreamer plugin for decoding WebP images
Summary(pl.UTF-8):	Wtyczka GStreamera do dekodowania obrazów WebP
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	libwebp >= 0.2.1

%description -n gstreamer-webp
GStreamer plugin for decoding WebP images.

%description -n gstreamer-webp -l pl.UTF-8
Wtyczka GStreamera do dekodowania obrazów WebP.

%package -n gstreamer-webrtc
Summary:	WebRTC plugin for GStreamer
Summary(pl.UTF-8):	Wtyczka WebRTC dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	libnice >= 0.1.14

%description -n gstreamer-webrtc
WebRTC plugin for GStreamer.

%description -n gstreamer-webrtc -l pl.UTF-8
Wtyczka WebRTC dla GStreamera.

%package -n gstreamer-webrtcdsp
Summary:	WebRTC Audio Processing plugin for GStreamer
Summary(pl.UTF-8):	Wtyczka WebRTC Audio Processing dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	webrtc-audio-processing >= 0.2

%description -n gstreamer-webrtcdsp
WebRTC Audio Processing plugin for GStreamer.

%description -n gstreamer-webrtcdsp -l pl.UTF-8
Wtyczka WebRTC Audio Processing dla GStreamera.

%package -n gstreamer-wildmidi
Summary:	wildmidi plugin for GStreamer
Summary(pl.UTF-8):	Wtyczka wildmidi dla GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	wildmidi >= 0.4

%description -n gstreamer-wildmidi
wildmidi plugin for GStreamer.

%description -n gstreamer-wildmidi -l pl.UTF-8
Wtyczka wildmidi dla GStreamera.

%package -n gstreamer-wpe
Summary:	GStreamer WPE (WebKit web browser) source plugin
Summary(pl.UTF-8):	Wtyczka GStreamera ze źródłem WPE (przeglądarki WWW opartej na WebKicie)
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	wpe-webkit >= 2.24
Requires:	wpebackend-fdo >= 1.0

%description -n gstreamer-wpe
GStreamer WPE (WebKit web browser) source plugin.

%description -n gstreamer-wpe -l pl.UTF-8
Wtyczka GStreamera ze źródłem WPE (przeglądarki WWW opartej na
WebKicie).

%package -n gstreamer-x265
Summary:	GStreamer x265 encoder plugin
Summary(pl.UTF-8):	Wtyczka GStreamera kodująca przy użyciu biblioteki x265
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}

%description -n gstreamer-x265
GStreamer x265 encoder plugin.

%description -n gstreamer-x265 -l pl.UTF-8
Wtyczka GStreamera kodująca przy użyciu biblioteki x265.

%package -n gstreamer-zbar
Summary:	GStreamer ZBar barcode scanner plugin
Summary(pl.UTF-8):	Wtyczka GStreamera skanująca kody kreskowe
Group:		Libraries
Requires:	gstreamer >= %{gst_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_ver}
Requires:	zbar >= 0.9

%description -n gstreamer-zbar
GStreamer ZBar barcode scanner plugin.

%description -n gstreamer-zbar -l pl.UTF-8
Wtyczka GStreamera skanująca kody kreskowe.

%prep
%setup -q -n %{gstname}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4 -I common/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_bluez:--disable-bluez} \
	%{!?with_bs2b:--disable-bs2b} \
	%{!?with_gnustep:--disable-cocoa} \
	%{!?with_dts:--disable-dts} \
	%{!?with_egl:--disable-egl} \
	%{!?with_examples:--disable-examples} \
	%{!?with_faad:--disable-faad} \
	%{!?with_gles:--disable-gles2} \
	%{!?with_gsm:--disable-gsm} \
	%{!?with_ladspa:--disable-ladspa} \
	%{!?with_libde265:--disable-libde265} \
	%{!?with_mms:--disable-libmms} \
	%{!?with_mjpegtools:--disable-mpeg2enc} \
	%{!?with_musepack:--disable-musepack} \
	%{!?with_neon:--disable-neon} \
	%{!?with_ofa:--disable-ofa} \
	%{!?with_opencv:--disable-opencv} \
	%{!?with_openh264:--disable-openh264} \
	%{!?with_openni2:--disable-openni2} \
	%{!?with_zvbi:--disable-teletextdec} \
	%{!?with_tinyalsa:--disable-tinyalsa} \
	%{!?with_uvch264:--disable-uvch264} \
	%{!?with_amr:--disable-voamrwbenc} \
	%{!?with_vulkan:--disable-vulkan} \
	%{!?with_wayland:--disable-wayland} \
	%{!?with_x265:--disable-x265} \
	%{!?with_yadif:--disable-yadif} \
	--disable-silent-rules \
	--disable-static \
	--enable-experimental \
	--enable-gtk-doc \
	--with-egl-window-system=x11 \
	--with-gtk=3.0 \
	--with-html-dir=%{_gtkdocdir}

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# We don't need plugins' *.la files
%{__rm} $RPM_BUILD_ROOT%{gstlibdir}/*.la
# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgst*.la

%find_lang %{gstname}-%{gstmver}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	-n gstreamer-opencv-libs -p /sbin/ldconfig
%postun	-n gstreamer-opencv-libs -p /sbin/ldconfig

%files -f %{gstname}-%{gstmver}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README RELEASE
%attr(755,root,root) %{_libdir}/libgstadaptivedemux-%{gstmver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstadaptivedemux-%{gstmver}.so.0
%attr(755,root,root) %{_libdir}/libgstbadaudio-%{gstmver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstbadaudio-%{gstmver}.so.0
%attr(755,root,root) %{_libdir}/libgstbasecamerabinsrc-%{gstmver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstbasecamerabinsrc-%{gstmver}.so.0
%attr(755,root,root) %{_libdir}/libgstcodecparsers-%{gstmver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstcodecparsers-%{gstmver}.so.0
%attr(755,root,root) %{_libdir}/libgstinsertbin-%{gstmver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstinsertbin-%{gstmver}.so.0
%attr(755,root,root) %{_libdir}/libgstisoff-%{gstmver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstisoff-%{gstmver}.so.0
%attr(755,root,root) %{_libdir}/libgstmpegts-%{gstmver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstmpegts-%{gstmver}.so.0
%attr(755,root,root) %{_libdir}/libgstphotography-%{gstmver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstphotography-%{gstmver}.so.0
%attr(755,root,root) %{_libdir}/libgstplayer-%{gstmver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstplayer-%{gstmver}.so.0
%attr(755,root,root) %{_libdir}/libgstsctp-%{gstmver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstsctp-%{gstmver}.so.0
%attr(755,root,root) %{_libdir}/libgsturidownloader-%{gstmver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgsturidownloader-%{gstmver}.so.0
%attr(755,root,root) %{_libdir}/libgstwayland-%{gstmver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstwayland-%{gstmver}.so.0
%attr(755,root,root) %{_libdir}/libgstwebrtc-%{gstmver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstwebrtc-%{gstmver}.so.0
%{_libdir}/girepository-1.0/GstInsertBin-1.0.typelib
%{_libdir}/girepository-1.0/GstMpegts-1.0.typelib
%{_libdir}/girepository-1.0/GstPlayer-1.0.typelib
%{_libdir}/girepository-1.0/GstWebRTC-1.0.typelib
%attr(755,root,root) %{gstlibdir}/libgstaccurip.so
%attr(755,root,root) %{gstlibdir}/libgstadpcmdec.so
%attr(755,root,root) %{gstlibdir}/libgstadpcmenc.so
%attr(755,root,root) %{gstlibdir}/libgstaiff.so
%attr(755,root,root) %{gstlibdir}/libgstasfmux.so
%attr(755,root,root) %{gstlibdir}/libgstaudiobuffersplit.so
%attr(755,root,root) %{gstlibdir}/libgstaudiofxbad.so
%attr(755,root,root) %{gstlibdir}/libgstaudiolatency.so
%attr(755,root,root) %{gstlibdir}/libgstaudiomixmatrix.so
%attr(755,root,root) %{gstlibdir}/libgstaudiovisualizers.so
%attr(755,root,root) %{gstlibdir}/libgstautoconvert.so
%attr(755,root,root) %{gstlibdir}/libgstbayer.so
%attr(755,root,root) %{gstlibdir}/libgstbz2.so
%attr(755,root,root) %{gstlibdir}/libgstcamerabin.so
%attr(755,root,root) %{gstlibdir}/libgstcoloreffects.so
# R: lcms2
%attr(755,root,root) %{gstlibdir}/libgstcolormanagement.so
%attr(755,root,root) %{gstlibdir}/libgstdashdemux.so
%attr(755,root,root) %{gstlibdir}/libgstdebugutilsbad.so
%attr(755,root,root) %{gstlibdir}/libgstdecklink.so
%attr(755,root,root) %{gstlibdir}/libgstdvb.so
%attr(755,root,root) %{gstlibdir}/libgstdvbsuboverlay.so
%attr(755,root,root) %{gstlibdir}/libgstdvdspu.so
%attr(755,root,root) %{gstlibdir}/libgstfaceoverlay.so
%attr(755,root,root) %{gstlibdir}/libgstfbdevsink.so
%attr(755,root,root) %{gstlibdir}/libgstfestival.so
%attr(755,root,root) %{gstlibdir}/libgstfieldanalysis.so
%attr(755,root,root) %{gstlibdir}/libgstfreeverb.so
%attr(755,root,root) %{gstlibdir}/libgstfrei0r.so
%attr(755,root,root) %{gstlibdir}/libgstgaudieffects.so
%attr(755,root,root) %{gstlibdir}/libgstgdp.so
%attr(755,root,root) %{gstlibdir}/libgstgeometrictransform.so
# R: nettle
%attr(755,root,root) %{gstlibdir}/libgsthls.so
%attr(755,root,root) %{gstlibdir}/libgstid3tag.so
%attr(755,root,root) %{gstlibdir}/libgstinterlace.so
%attr(755,root,root) %{gstlibdir}/libgstinter.so
%attr(755,root,root) %{gstlibdir}/libgstipcpipeline.so
%attr(755,root,root) %{gstlibdir}/libgstivfparse.so
%attr(755,root,root) %{gstlibdir}/libgstivtc.so
%attr(755,root,root) %{gstlibdir}/libgstjp2kdecimator.so
%attr(755,root,root) %{gstlibdir}/libgstjpegformat.so
%attr(755,root,root) %{gstlibdir}/libgstlegacyrawparse.so
%attr(755,root,root) %{gstlibdir}/libgstmidi.so
# R: libmodplug
%attr(755,root,root) %{gstlibdir}/libgstmodplug.so
%attr(755,root,root) %{gstlibdir}/libgstmpegpsdemux.so
%attr(755,root,root) %{gstlibdir}/libgstmpegpsmux.so
%attr(755,root,root) %{gstlibdir}/libgstmpegtsdemux.so
%attr(755,root,root) %{gstlibdir}/libgstmpegtsmux.so
%attr(755,root,root) %{gstlibdir}/libgstmxf.so
%attr(755,root,root) %{gstlibdir}/libgstnetsim.so
%attr(755,root,root) %{gstlibdir}/libgstpcapparse.so
%attr(755,root,root) %{gstlibdir}/libgstpnm.so
%attr(755,root,root) %{gstlibdir}/libgstproxy.so
%attr(755,root,root) %{gstlibdir}/libgstremovesilence.so
%attr(755,root,root) %{gstlibdir}/libgstrfbsrc.so
%attr(755,root,root) %{gstlibdir}/libgstrtponvif.so
%attr(755,root,root) %{gstlibdir}/libgstsdpelem.so
%attr(755,root,root) %{gstlibdir}/libgstsegmentclip.so
%attr(755,root,root) %{gstlibdir}/libgstshm.so
%attr(755,root,root) %{gstlibdir}/libgstsiren.so
%attr(755,root,root) %{gstlibdir}/libgstsmooth.so
%attr(755,root,root) %{gstlibdir}/libgstsmoothstreaming.so
%attr(755,root,root) %{gstlibdir}/libgstsubenc.so
%attr(755,root,root) %{gstlibdir}/libgsttimecode.so
%attr(755,root,root) %{gstlibdir}/libgstvideofiltersbad.so
%attr(755,root,root) %{gstlibdir}/libgstvideoframe_audiolevel.so
%attr(755,root,root) %{gstlibdir}/libgstvideoparsersbad.so
%attr(755,root,root) %{gstlibdir}/libgstvideosignal.so
%attr(755,root,root) %{gstlibdir}/libgstvmnc.so
%attr(755,root,root) %{gstlibdir}/libgsty4mdec.so
%{?with_yadif:%attr(755,root,root) %{gstlibdir}/libgstyadif.so}
# dirs should belong to gstreamer or gstreamer-pb?
%dir %{gstdatadir}
%dir %{gstdatadir}/presets
%{gstdatadir}/presets/GstFreeverb.prs
%{_gtkdocdir}/gst-plugins-bad-plugins-%{gstmver}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgstadaptivedemux-%{gstmver}.so
%attr(755,root,root) %{_libdir}/libgstbadaudio-%{gstmver}.so
%attr(755,root,root) %{_libdir}/libgstbasecamerabinsrc-%{gstmver}.so
%attr(755,root,root) %{_libdir}/libgstcodecparsers-%{gstmver}.so
%attr(755,root,root) %{_libdir}/libgstinsertbin-%{gstmver}.so
%attr(755,root,root) %{_libdir}/libgstisoff-%{gstmver}.so
%attr(755,root,root) %{_libdir}/libgstmpegts-%{gstmver}.so
%attr(755,root,root) %{_libdir}/libgstphotography-%{gstmver}.so
%attr(755,root,root) %{_libdir}/libgstplayer-%{gstmver}.so
%attr(755,root,root) %{_libdir}/libgstsctp-%{gstmver}.so
%attr(755,root,root) %{_libdir}/libgsturidownloader-%{gstmver}.so
%attr(755,root,root) %{_libdir}/libgstwayland-%{gstmver}.so
%attr(755,root,root) %{_libdir}/libgstwebrtc-%{gstmver}.so
%{_includedir}/gstreamer-%{gstmver}/gst/audio/audio-bad-prelude.h
%{_includedir}/gstreamer-%{gstmver}/gst/audio/gstnonstreamaudiodecoder.h
%{_includedir}/gstreamer-%{gstmver}/gst/audio/gstplanaraudioadapter.h
%{_includedir}/gstreamer-%{gstmver}/gst/basecamerabinsrc
%{_includedir}/gstreamer-%{gstmver}/gst/codecparsers
%{_includedir}/gstreamer-%{gstmver}/gst/insertbin
%{_includedir}/gstreamer-%{gstmver}/gst/interfaces
%{_includedir}/gstreamer-%{gstmver}/gst/isoff
%{_includedir}/gstreamer-%{gstmver}/gst/mpegts
%{_includedir}/gstreamer-%{gstmver}/gst/player
%{_includedir}/gstreamer-%{gstmver}/gst/sctp
%{_includedir}/gstreamer-%{gstmver}/gst/uridownloader
%{_includedir}/gstreamer-%{gstmver}/gst/webrtc
%{_datadir}/gir-1.0/GstInsertBin-1.0.gir
%{_datadir}/gir-1.0/GstMpegts-1.0.gir
%{_datadir}/gir-1.0/GstPlayer-1.0.gir
%{_datadir}/gir-1.0/GstWebRTC-1.0.gir
%{_pkgconfigdir}/gstreamer-codecparsers-%{gstmver}.pc
%{_pkgconfigdir}/gstreamer-insertbin-%{gstmver}.pc
%{_pkgconfigdir}/gstreamer-mpegts-%{gstmver}.pc
%{_pkgconfigdir}/gstreamer-plugins-bad-%{gstmver}.pc
%{_pkgconfigdir}/gstreamer-bad-audio-%{gstmver}.pc
%{_pkgconfigdir}/gstreamer-player-%{gstmver}.pc
%{_pkgconfigdir}/gstreamer-sctp-%{gstmver}.pc
%{_pkgconfigdir}/gstreamer-webrtc-%{gstmver}.pc
%{_gtkdocdir}/gst-plugins-bad-libs-%{gstmver}

##
## Plugins
##

%if %{with faad}
%files -n gstreamer-aac
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstfaac.so
%attr(755,root,root) %{gstlibdir}/libgstfaad.so
%endif

%files -n gstreamer-aom
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstaom.so

%if %{with amr}
%files -n gstreamer-amrwbenc
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstvoamrwbenc.so
%{gstdatadir}/presets/GstVoAmrwbEnc.prs
%endif

%files -n gstreamer-ass
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstassrender.so

%files -n gstreamer-audio-effects-bad
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstspeed.so

%if %{with tinyalsa}
%files -n gstreamer-audiosink-tinyalsa
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgsttinyalsa.so
%endif

%if %{with bluez}
%files -n gstreamer-bluez
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstbluez.so
%endif

%if %{with bs2b}
%files -n gstreamer-bs2b
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstbs2b.so
%endif

%if %{with chromaprint}
%files -n gstreamer-chromaprint
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstchromaprint.so
%endif

%files -n gstreamer-closedcaption
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstclosedcaption.so

%files -n gstreamer-curl
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstcurl.so

%if %{with dc1394}
%files -n gstreamer-dc1394
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstdc1394.so
%endif

%files -n gstreamer-dtls
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstdtls.so

%if %{with dts}
%files -n gstreamer-dts
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstdtsdec.so
%endif

%files -n gstreamer-fdkaac
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstfdkaac.so

%files -n gstreamer-flite
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstflite.so

%files -n gstreamer-fluidsynth
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstfluidsynthmidi.so

%files -n gstreamer-gme
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstgme.so

# not ported to 1.0 yet
%if 0
%files -n gstreamer-gsettings
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstgsettingselements.so
%{_datadir}/glib-2.0/schemas/org.freedesktop.gstreamer-%{gstmver}.default-elements.gschema.xml
%endif

%if %{with gsm}
%files -n gstreamer-gsm
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstgsm.so
%endif

%files -n gstreamer-iqa
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstiqa.so

%if %{with kate}
%files -n gstreamer-kate
%defattr(644,root,root,755)
%doc ext/kate/README
%attr(755,root,root) %{gstlibdir}/libgstkate.so
%endif

%files -n gstreamer-videosink-kms
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstkms.so

%if %{with ladspa}
%files -n gstreamer-ladspa
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstladspa.so
%endif

%if %{with libde265}
%files -n gstreamer-libde265
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstde265.so
%endif

%if %{with lv2}
%files -n gstreamer-lv2
%defattr(644,root,root,755)
%doc ext/lv2/README
%attr(755,root,root) %{gstlibdir}/libgstlv2.so
%endif

%if %{with mjpegtools}
%files -n gstreamer-mjpegtools
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstmpeg2enc.so
%attr(755,root,root) %{gstlibdir}/libgstmplex.so
%endif

%if %{with mms}
%files -n gstreamer-mms
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstmms.so
%endif

%if %{with mfx}
%files -n gstreamer-msdk
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstmsdk.so
%endif

%if %{with musepack}
%files -n gstreamer-musepack
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstmusepack.so
%endif

%if %{with neon}
%files -n gstreamer-neon
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstneonhttpsrc.so
%endif

%if %{with ofa}
%files -n gstreamer-ofa
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstofa.so
%endif

%if %{with openal}
%files -n gstreamer-openal
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstopenal.so
%endif

%if %{with opencv}
%files -n gstreamer-opencv
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstopencv.so
# possibly common dir (but no other users so far)
%dir %{_datadir}/gst-plugins-bad
%dir %{_datadir}/gst-plugins-bad/1.0
%{_datadir}/gst-plugins-bad/1.0/opencv_haarcascades

%files -n gstreamer-opencv-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgstopencv-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstopencv-1.0.so.0

%files -n gstreamer-opencv-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgstopencv-1.0.so
%{_includedir}/gstreamer-1.0/gst/opencv
%endif

%if %{with openexr}
%files -n gstreamer-openexr
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstopenexr.so
%endif

%if %{with openh264}
%files -n gstreamer-openh264
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstopenh264.so
%endif

%files -n gstreamer-openjpeg
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstopenjpeg.so

%files -n gstreamer-openmpt
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstopenmpt.so

%if %{with openni2}
%files -n gstreamer-openni2
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstopenni2.so
%endif

%files -n gstreamer-opusparse
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstopusparse.so

%files -n gstreamer-resindvd
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstresindvd.so

%if %{with librsvg}
%files -n gstreamer-rsvg
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstrsvg.so
%endif

%files -n gstreamer-rtmp
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstrtmp.so

%if %{with sbc}
%files -n gstreamer-sbc
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstsbc.so
%endif

%files -n gstreamer-sctp
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstsctp.so

%if %{with sndfile}
%files -n gstreamer-sndfile
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstsndfile.so
%endif

%files -n gstreamer-soundtouch
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstsoundtouch.so

%files -n gstreamer-spandsp
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstspandsp.so

%files -n gstreamer-srt
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstsrt.so

%if %{with srtp}
%files -n gstreamer-srtp
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstsrtp.so
%endif

%if %{with zvbi}
%files -n gstreamer-teletextdec
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstteletext.so
%endif

%files -n gstreamer-ttml
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstttmlsubs.so

%if %{with uvch264}
%files -n gstreamer-uvch264
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstuvch264.so
%endif

%if %{with vdpau}
%files -n gstreamer-vdpau
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstvdpau.so
%endif

%if %{with directfb}
%files -n gstreamer-videosink-directfb
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstdfbvideosink.so
%endif

%if %{with wayland}
%files -n gstreamer-videosink-wayland
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstwaylandsink.so
%endif

%files -n gstreamer-voaacenc
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstvoaacenc.so

%if %{with vulkan}
%files -n gstreamer-vulkan
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstvulkan.so
%endif

%files -n gstreamer-webp
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstwebp.so

%files -n gstreamer-webrtc
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstwebrtc.so

%files -n gstreamer-webrtcdsp
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstwebrtcdsp.so

%if %{with wildmidi}
%files -n gstreamer-wildmidi
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstwildmidi.so
%endif

%if %{with wpe}
%files -n gstreamer-wpe
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstwpe.so
%endif

%if %{with x265}
%files -n gstreamer-x265
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstx265.so
%endif

%files -n gstreamer-zbar
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstzbar.so
