# TODO:
# - new plugins:
#   - ivorbisdec (BR: tremor-devel, CVS versions only, http://www.xiph.org/vorbis/)
#
# Conditional build:
%bcond_without	cdaudio		# don't build cdaudio plugin
%bcond_without	dirac		# don't build Dirac plugin
%bcond_without	directfb	# don't build directfb videosink plugin
%bcond_without	dts		# don't build DTS plugin
%bcond_without	faad		# don't build faad plugin
%bcond_without	gsm		# don't build gsm plugin
%bcond_without	ladspa		# don't build ladspa plugin
%bcond_without	mjpegtools	# don't build mpeg2enc plugin
%bcond_without	mms		# don't build mms plugin
%bcond_without	musepack	# don't build musepack plugin
%bcond_without	neon		# don't build neonhttpsrc plugin
%bcond_without	ofa		# don't build OFA plugin
%bcond_without	sdl		# don't build sdl plugin
%bcond_with	swfdec		# swfdec plugin
%bcond_without	spc		# don't build spc plugin
%bcond_without	wavpack		# don't build wavpack plugin
%bcond_without	xvid		# don't build XviD plugin
%bcond_with	amr		# build amrwb plugin
%bcond_with	divx4linux	# build divx4linux plugins
%bcond_without	vdpau		# build without VDPAU

%define		gstname		gst-plugins-bad
%define		gst_major_ver	0.10
%define		gst_req_ver	0.10.32
%define		gstpb_req_ver	0.10.32
%include	/usr/lib/rpm/macros.gstreamer
Summary:	Bad GStreamer Streaming-media framework plugins
Summary(pl.UTF-8):	Złe wtyczki do środowiska obróbki strumieni GStreamer
Name:		gstreamer-plugins-bad
Version:	0.10.21
Release:	2
License:	LGPL v2+
Group:		Libraries
Source0:	http://gstreamer.freedesktop.org/src/gst-plugins-bad/%{gstname}-%{version}.tar.bz2
# Source0-md5:	f501336ab1d18d2565f47c36ce653a82
Patch0:		%{name}-bashish.patch
Patch1:		%{name}-libdts.patch
Patch2:		%{name}-divx4linux.patch
Patch4:		%{name}-timidity.patch
Patch5:		%{name}-nas.patch
URL:		http://gstreamer.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.10
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel >= 0.17
# 2.22 for all, gio-2.26 for gsettings
BuildRequires:	glib2-devel >= 1:2.26
BuildRequires:	gstreamer-devel >= %{gst_req_ver}
BuildRequires:	gstreamer-plugins-base-devel >= %{gstpb_req_ver}
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	gtk-doc >= 1.6
BuildRequires:	libtool >= 1.4
BuildRequires:	orc-devel >= 0.4.7
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	python >= 2.1
BuildRequires:	rpmbuild(macros) >= 1.98
BuildRequires:	xorg-lib-libX11-devel
##
## plugins
##
%{?with_directfb:BuildRequires:	DirectFB-devel >= 1:0.9.24}
%{?with_sdl:BuildRequires:	SDL-devel}
BuildRequires:	alsa-lib-devel >= 0.9.1
%{?with_amr:BuildRequires:	amrwb-devel}
BuildRequires:	bzip2-devel
BuildRequires:	cairo-devel
BuildRequires:	celt-devel >= 0.8.0
%{?with_dirac:BuildRequires:	dirac-devel >= 0.10}
%{?with_divx4linux:BuildRequires:	divx4linux-devel >= 1:5.05.20030428}
BuildRequires:	exempi-devel >= 1.99.5
BuildRequires:	faac-devel
%{?with_faad:BuildRequires:	faad2-devel >= 2.0-2}
BuildRequires:	flite-devel
BuildRequires:	game-music-emu-devel >= 0.5.5
# when becomes available...
#BuildRequires:	game-music-emu-devel >= 0.5.6
BuildRequires:	gmyth-devel >= 0.7
BuildRequires:	jasper-devel
%{?with_ladspa:BuildRequires:	ladspa-devel >= 1.12}
BuildRequires:	libass-devel >= 0.9.4
%{?with_cdaudio:BuildRequires:	libcdaudio-devel}
BuildRequires:	libdc1394-devel >= 2.0.0
%{?with_dts:BuildRequires:	libdts-devel}
BuildRequires:	libdvdnav-devel >= 4.1.2
BuildRequires:	libdvdread-devel >= 4.1.2
BuildRequires:	libexif-devel >= 0.6.16
%{?with_gsm:BuildRequires:	libgsm-devel}
BuildRequires:	libiptcdata-devel >= 1.0.2
BuildRequires:	libkate-devel >= 0.1.7
BuildRequires:	liblrdf-devel
BuildRequires:	libmimic-devel >= 1.0
%{?with_mms:BuildRequires:	libmms-devel >= 0.4}
BuildRequires:	libmodplug-devel
%{?with_musepack:BuildRequires:	libmpcdec-devel >= 1.2}
BuildRequires:	libmusicbrainz-devel >= 2.1.0
%{?with_ofa:BuildRequires:	libofa-devel >= 0.9.3}
%{?with_spc:BuildRequires:	libopenspc-devel >= 0.3.99}
BuildRequires:	libpng-devel >= 2:1.2.0
BuildRequires:	librsvg-devel >= 2.14
# for modplug and libSoundTouch
BuildRequires:	libstdc++-devel
BuildRequires:	libsndfile-devel >= 1.0.16
BuildRequires:	libtheora-devel >= 1.0
BuildRequires:	libtiger-devel >= 0.3.2
BuildRequires:	libtimidity-devel
BuildRequires:	libvpx-devel
BuildRequires:	libx264-devel >= 0.1.2
%{?with_mjpegtools:BuildRequires:	mjpegtools-devel >= 1.9.0}
BuildRequires:	nas-devel
%{?with_neon:BuildRequires:	neon-devel >= 0.27.0}
# TODO
#BuildRequires:	opencv-devel >= 2.0.0
BuildRequires:	openssl-devel >= 0.9.5
BuildRequires:	schroedinger-devel >= 1.0.7
BuildRequires:	slv2-devel >= 0.6.6
BuildRequires:	soundtouch-devel >= 1.4
%if %{with swfdec}
BuildRequires:	swfdec-devel < 0.4.0
BuildRequires:	swfdec-devel >= 0.3.6
%endif
%{?with_vdpau:BuildRequires:	libvdpau-devel}
BuildRequires:	twolame-devel
BuildRequires:	wildmidi-devel
BuildRequires:	xorg-lib-libX11-devel
%{?with_xvid:BuildRequires:	xvid-devel >= 1.0.0}
BuildRequires:	zbar-devel >= 0.9
Requires:	glib2 >= 1:2.22
Requires:	gstreamer >= %{gst_req_ver}
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}
Requires:	orc >= 0.4.7
Obsoletes:	gstreamer-quicktime
Obsoletes:	gstreamer-vcd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		gstlibdir 	%{_libdir}/gstreamer-%{gst_major_ver}
%define		gstdatadir 	%{_datadir}/gstreamer-%{gst_major_ver}

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

%description devel
Header files and API documentation for gstapp library.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja API biblioteki gstapp.

## Plugins ##

%package -n gstreamer-aac
Summary:	GStreamer plugin for AAC audio encoding and decoding
Summary(pl.UTF-8):	Wtyczka do GStreamera do kodowania i dekodowania plików audio AAC
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}

%description -n gstreamer-aac
GStreamer plugin for AAC audio encoding and decoding.

%description -n gstreamer-aac -l pl.UTF-8
Wtyczka do GStreamera do kodowania i dekodowania plików audio AAC.

%package -n gstreamer-amrwbenc
Summary:	GStreamer plugin for AMR-WB audio encoding
Summary(pl.UTF-8):	Wtyczka GStreamera do kodowania dźwięku w formacie AMR-WB
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}

%description -n gstreamer-amrwbenc
GStreamer plugin for AMR-WB audio encoding.

%description -n gstreamer-amrwbenc -l pl.UTF-8
Wtyczka GStreamera do kodowania dźwięku w formacie AMR-WB.

%package -n gstreamer-ass
Summary:	GStreamer plugin for ASS/SSA subtitles rendering
Summary(pl.UTF-8):	Wtyczka do GStreamera do renderowania napisów ASS/SSA
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}
Requires:	libass >= 0.9.4

%description -n gstreamer-ass
GStreamer plugin for ASS/SSA subtitles rendering.

%description -n gstreamer-ass -l pl.UTF-8
Wtyczka do GStreamera do renderowania napisów ASS/SSA.

%package -n gstreamer-audio-effects-bad
Summary:	Bad GStreamer audio effects plugins
Summary(pl.UTF-8):	Złe wtyczki efektów dźwiękowych do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}
Obsoletes:	gstreamer-audio-effects

%description -n gstreamer-audio-effects-bad
Bad GStreamer audio effects plugins.

%description -n gstreamer-audio-effects-bad -l pl.UTF-8
Złe wtyczki efektów dźwiękowych do GStreamera.

%package -n gstreamer-audiosink-nas
Summary:	GStreamer NAS audio output plugin
Summary(pl.UTF-8):	Wtyczka wyjścia dźwięku NAS dla GStreamera
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}
Provides:	gstreamer-audiosink = %{version}
Obsoletes:	gstreamer-nas

%description -n gstreamer-audiosink-nas
GStreamer NAS audio output plugin.

%description -n gstreamer-audiosink-nas -l pl.UTF-8
Wtyczka wyjścia dźwięku NAS dla GStreamera.

%package -n gstreamer-cdaudio
Summary:	GStreamer plugin for CD audio input using libcdaudio
Summary(pl.UTF-8):	Wtyczka do GStreamera odtwarzająca płyty CD-Audio przy użyciu libcdaudio
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}

%description -n gstreamer-cdaudio
Plugin for playing audio tracks using libcdaudio under GStreamer.

%description -n gstreamer-cdaudio -l pl.UTF-8
Wtyczka do odtwarzania ścieżek dźwiękowych pod GStreamerem za pomocą
libcdaudio.

%package -n gstreamer-celt
Summary:	GStreamer Celt audio codec plugin
Summary(pl.UTF-8):	Wtyczka kodeka dźwięku Celt do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}
Requires:	celt >= 0.8.0

%description -n gstreamer-celt
GStreamer Celt audio encoder and decoder plugin.

%description -n gstreamer-celt -l pl.UTF-8
Wtyczka GStreamera kodująca i dekodująca dźwięk w formacie Celt.

%package -n gstreamer-dc1394
Summary:	GStreamer 1394 IIDC (Firewire digital cameras) video source plugin
Summary(pl.UTF-8):	Wtyczka źródła obrazu 1394 IIDC (z kamer cyfrowych Firewire) do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}

%description -n gstreamer-dc1394
GStreamer 1394 IIDC (Firewire digital cameras) video source plugin.

%description -n gstreamer-dc1394 -l pl.UTF-8
Wtyczka źródła obrazu 1394 IIDC (z kamer cyfrowych Firewire) do
GStreamera.

%package -n gstreamer-dirac
Summary:	GStreamer Dirac plugin
Summary(pl.UTF-8):	Wtyczka Dirac do GStreamera
Group:		Libraries
Requires:	dirac >= 0.10
Requires:	gstreamer >= %{gst_req_ver}

%description -n gstreamer-dirac
GStreamer Dirac video decoder/encoder plugin.

%description -n gstreamer-dirac -l pl.UTF-8
Wtyczka dekodująca i kodująca obraz Dirac do GStreamera.

%package -n gstreamer-divx
Summary:	GStreamer divx plugin
Summary(pl.UTF-8):	Wtyczka divx do GStreamera
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}

%description -n gstreamer-divx
GStreamer divx plugin.

%description -n gstreamer-divx -l pl.UTF-8
Wtyczka divx do GStreamera.

%package -n gstreamer-dts
Summary:	GStreamer DTS plugin
Summary(pl.UTF-8):	Wtyczka DTS do GStreamera
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}

%description -n gstreamer-dts
Plugin for DTS Coherent Acoustics support.

%description -n gstreamer-dts -l pl.UTF-8
Wtyczka do GStreamera obsługująca DTS Coherent Acoustics.

%package -n gstreamer-flite
Summary:	GStreamer Flite plugin
Summary(pl.UTF-8):	Wtyczka Flite do GStreamera
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}

%description -n gstreamer-flite
Plugin for Flite support.

%description -n gstreamer-flite -l pl.UTF-8
Wtyczka do GStreamera obsługująca Flite.

%package -n gstreamer-gme
Summary:	GStreamer GME Audio Decoder plugin
Summary(pl.UTF-8):	Wtyczka dekodująca GME do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}

%description -n gstreamer-gme
GStreamer GME Audio Decoder plugin.

%description -n gstreamer-gme -l pl.UTF-8
Wtyczka dekodująca GME do GStreamera.

%package -n gstreamer-gsettings
Summary:	GStreamer GSettings plugin
Summary(pl.UTF-8):	Wtyczka GSettings do GStreamera
Group:		Libraries
Requires:	glib2 >= 1:2.26
Requires:	gstreamer >= %{gst_req_ver}

%description -n gstreamer-gsettings
GStreamer GSettings plugin.

%description -n gstreamer-gsettings -l pl.UTF-8
Wtyczka GSettings do GStreamera.

%package -n gstreamer-gsm
Summary:	GStreamer plugin for GSM lossy audio format
Summary(pl.UTF-8):	Wtyczka do GStreamera obsługująca stratny format dźwięku GSM
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}

%description -n gstreamer-gsm
Output plugin for GStreamer to convert to GSM lossy audio format.

%description -n gstreamer-gsm -l pl.UTF-8
Wtyczka wyjścia dźwięku GSteamera konwertująca do stratnego formatu
GSM.

%package -n gstreamer-kate
Summary:	GStreamer plugin for Kate text streams
Summary(pl.UTF-8):	Wtyczka obsługująca strumienie tekstowe Kate dla GStreamera
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}
Requires:	libkate >= 0.1.7
Requires:	libtiger >= 0.3.2

%description -n gstreamer-kate
GStreamer plugin for Kate text streams.

%description -n gstreamer-kate -l pl.UTF-8
Wtyczka obsługująca strumienie tekstowe Kate dla GStreamera.

%package -n gstreamer-ladspa
Summary:	GStreamer wrapper for LADSPA plugins
Summary(pl.UTF-8):	Wrapper do wtyczek LADSPA dla GStreamera
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}

%description -n gstreamer-ladspa
Plugin which wraps LADSPA plugins for use by GStreamer applications.

%description -n gstreamer-ladspa -l pl.UTF-8
Wtyczka pozwalająca na używanie wtyczek LADSPA przez aplikacje
GStreamera.

%package -n gstreamer-lv2
Summary:	GStreamer wrapper for LV2 plugins
Summary(pl.UTF-8):	Wrapper do wtyczek LV2 dla GStreamera
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}
Requires:	slv2 >= 0.6.6

%description -n gstreamer-lv2
Plugin which wraps LV2 plugins for use by GStreamer applications.

%description -n gstreamer-lv2 -l pl.UTF-8
Wtyczka pozwalająca na używanie wtyczek LV2 przez aplikacje
GStreamera.

%package -n gstreamer-mimic
Summary:	GStreamer Mimic video decoding/encoding plugin
Summary(pl.UTF-8):	Wtyczka kodująca/dekodująca obraz Mimic do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}

%description -n gstreamer-mimic
GStreamer Mimic video decoding/encoding plugin.

%description -n gstreamer-mimic -l pl.UTF-8
Wtyczka kodująca/dekodująca obraz Mimic do GStreamera.

%package -n gstreamer-mjpegtools
Summary:	GStreamer mpeg2enc plugin
Summary(pl.UTF-8):	Wtyczka mpeg2enc do GStreamera
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}

%description -n gstreamer-mjpegtools
GStreamer mpeg2enc plugin (based on mjpegtools libraries).

%description -n gstreamer-mjpegtools -l pl.UTF-8
Wtyczka mpeg2enc do GStreamera (oparta na bibliotekach mjpegtools).

%package -n gstreamer-mms
Summary:	GStreamer mms plugin
Summary(pl.UTF-8):	Wtyczka mms do GStreamera
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}
Requires:	libmms >= 0.4

%description -n gstreamer-mms
GStreamer mms plugin.

%description -n gstreamer-mms -l pl.UTF-8
Wtyczka mms do GStreamera.

%package -n gstreamer-musepack
Summary:	GStreamer musepack plugin
Summary(pl.UTF-8):	Wtyczka musepack do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}

%description -n gstreamer-musepack
GStreamer musepack plugin.

%description -n gstreamer-musepack -l pl.UTF-8
Wtyczka musepack do GStreamera.

%package -n gstreamer-mythtv
Summary:	GStreamer MythTV plugin
Summary(pl.UTF-8):	Wtyczka MythTV do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}

%description -n gstreamer-mythtv
GStreamer MythTV plugin.

%description -n gstreamer-mythtv -l pl.UTF-8
Wtyczka MythTV do GStreamera.

%package -n gstreamer-musicbrainz
Summary:	GStreamer musicbrainz plugin
Summary(pl.UTF-8):	Wtyczka musicbrainz do GStreamera
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}

%description -n gstreamer-musicbrainz
GStreamer musicbrainz plugin - a TRM signature producer.

%description -n gstreamer-musicbrainz -l pl.UTF-8
Wtyczka musicbrainz do GStreamera, tworząca sygnatury TRM.

%package -n gstreamer-neon
Summary:	GStreamer neon HTTP source plugin
Summary(pl.UTF-8):	Wtyczka źródła HTTP neon do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}
Requires:	neon >= 0.27.0

%description -n gstreamer-neon
GStreamer neon HTTP source plugin.

%description -n gstreamer-neon -l pl.UTF-8
Wtyczka źródła HTTP neon do GStreamera.

%package -n gstreamer-ofa
Summary:	GStreamer OFA fingerprint plugin
Summary(pl.UTF-8):	Wtyczka odcisków OFA do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}
Requires:	libofa >= 0.9.3

%description -n gstreamer-ofa
GStreamer OFA plugin to calculate MusicIP fingerprints from audio
files.

%description -n gstreamer-ofa -l pl.UTF-8
Wtyczka OFA do GStreamera służąca do obliczania odcisków MusicIP
plików dźwiękowych.

%package -n gstreamer-resindvd
Summary:	GStreamer Resin DVD playback plugin
Summary(pl.UTF-8):	Wtyczka odtwarzania Resin DVD do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}

%description -n gstreamer-resindvd
GStreamer Resin DVD playback plugin.

%description -n gstreamer-resindvd -l pl.UTF-8
Wtyczka odtwarzania Resin DVD do GStreamera.

%package -n gstreamer-schroedinger
Summary:	Schroedinger plugin for GStreamer
Summary(pl.UTF-8):	Wtyczka Schroedinger do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}
Requires:	schroedinger >= 1.0.7

%description -n gstreamer-schroedinger
Schroedinger plugin for GStreamer.

%description -n gstreamer-schroedinger -l pl.UTF-8
Wtyczka Schroedinger do GStreamera.

%package -n gstreamer-soundtouch
Summary:	GStreamer soundtouch plugin
Summary(pl.UTF-8):	Wtyczka soundtouch do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}
Requires:	soundtouch >= 1.4

%description -n gstreamer-soundtouch
GStreamer soundtouch source plugin - audio pitch controller.

%description -n gstreamer-soundtouch -l pl.UTF-8
Wtyczka soundtouch do GStreamera, sterująca wysokością dźwięku.

%package -n gstreamer-sndfile
Summary:	GStreamer sndfile plugin
Summary(pl.UTF-8):	Wtyczka sndfile do GStreamera
Group:		Libraries
# for locales
Requires:	%{name} = %{version}-%{release}
Requires:	gstreamer >= %{gst_req_ver}
Requires:	libsndfile >= 1.0.16

%description -n gstreamer-sndfile
GStreamer sndfile source plugin.

%description -n gstreamer-sndfile -l pl.UTF-8
Wtyczka sndfile do GStreamera.

%package -n gstreamer-spc
Summary:	GStreamer SPC plugin
Summary(pl.UTF-8):	Wtyczka SPC dla GStreamera
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}
Requires:	libopenspc >= 0.3.99

%description -n gstreamer-spc
GStreamer Plugin for playing SPC files using OpenSPC library.

%description -n gstreamer-spc -l pl.UTF-8
Wtyczka GStreamera odtwarzająca pliki SPC przy użyciu biblioteki
OpenSPC.

%package -n gstreamer-swfdec
Summary:	GStreamer Flash redering plugin
Summary(pl.UTF-8):	Wtyczka renderująca animacje flash dla GStreamera
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}
Requires:	swfdec >= 0.3.6

%description -n gstreamer-swfdec
Plugin for rendering Flash animations using swfdec library.

%description -n gstreamer-swfdec -l pl.UTF-8
Wtyczka renderująca animacje flash w oparciu o bibliotekę swfdec.

%package -n gstreamer-timidity
Summary:	timidity plugin for GStreamer
Summary(pl.UTF-8):	Wtyczka timidity do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}

%description -n gstreamer-timidity
timidity plugin for GStreamer.

%description -n gstreamer-timidity -l pl.UTF-8
Wtyczka timidity do GStreamera.

%package -n gstreamer-videosink-sdl
Summary:	GStreamer plugin for outputing to SDL
Summary(pl.UTF-8):	Wtyczka wyjścia SDL do GStreamera
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}
Provides:	gstreamer-videosink = %{version}
Obsoletes:	gstreamer-SDL

%description -n gstreamer-videosink-sdl
Plugin for sending output to the Simple Direct Media architecture.
(http://www.libsdl.org/). Usefull for fullscreen playback.

%description -n gstreamer-videosink-sdl -l pl.UTF-8
Wtyczka przekazująca wyjście do architektury SDL. Użyteczna do
odtwarzania na pełnym ekranie.

%package -n gstreamer-videosink-directfb
Summary:	GStreamer DirectFB output plugin
Summary(pl.UTF-8):	Wtyczka wyjścia obrazu DirectFB do GStreamera
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}
Provides:	gstreamer-videosink = %{version}

%description -n gstreamer-videosink-directfb
GStreamer DirectFB output plugin.

%description -n gstreamer-videosink-directfb -l pl.UTF-8
Wtyczka wyjścia obrazu DirectFB do GStreamera.

%package -n gstreamer-vp8
Summary:	GStreamer VP8 encoding and decoding plugin
Summary(pl.UTF-8):	Wtyczka kodująca i dekodująca VP8 dla GStreamera
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}

%description -n gstreamer-vp8
GStreamer VP8 encoding and decoding plugin.

%description -n gstreamer-vp8 -l pl.UTF-8
Wtyczka kodująca i dekodująca VP8 dla GStreamera.

%package -n gstreamer-wildmidi
Summary:	wildmidi plugin for GStreamer
Summary(pl.UTF-8):	Wtyczka wildmidi do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}

%description -n gstreamer-wildmidi
wildmidi plugin for GStreamer.

%description -n gstreamer-wildmidi -l pl.UTF-8
Wtyczka wildmidi do GStreamera.

%package -n gstreamer-xvid
Summary:	GStreamer xvid decoder plugin
Summary(pl.UTF-8):	Wtyczka do GStreamera dekodująca przy użyciu biblioteki xvid
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}

%description -n gstreamer-xvid
GStreamer xvid decoder plugin.

%description -n gstreamer-xvid -l pl.UTF-8
Wtyczka do GStreamera dekodująca przy użyciu biblioteki xvid.

%package -n gstreamer-zbar
Summary:	GStreamer ZBar barcode scanner plugin
Summary(pl.UTF-8):	Wtyczka do GStreamera skanująca kody kreskowe
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gstpb_req_ver}
Requires:	zbar >= 0.9

%description -n gstreamer-zbar
GStreamer ZBar barcode scanner plugin.

%description -n gstreamer-zbar -l pl.UTF-8
Wtyczka do GStreamera skanująca kody kreskowe.

%prep
%setup -q -n %{gstname}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch4 -p1
%patch5 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4 -I common/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_amr:--disable-amrwb} \
	%{!?with_cdaudio:--disable-cdaudio} \
	%{!?with_divx4linux:--disable-divx} \
	%{!?with_dirac:--disable-dirac} \
	%{!?with_dts:--disable-dts} \
	%{!?with_faad:--disable-faad} \
	%{!?with_gsm:--disable-gsm} \
	%{!?with_ladspa:--disable-ladspa} \
	%{!?with_mms:--disable-libmms} \
	%{!?with_mjpegtools:--disable-mpeg2enc} \
	%{!?with_musepack:--disable-musepack} \
	%{!?with_neon:--disable-neon} \
	%{!?with_ofa:--disable-ofa} \
	%{!?with_sdl:--disable-sdl} \
	%{!?with_sdl:--disable-sdltest} \
	%{!?with_spc:--disable-spc} \
	%{!?with_swfdec:--disable-swfdec} \
	%{!?with_xvid:--disable-xvid} \
	--disable-silent-rules \
	--disable-static \
	--enable-experimental \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# We don't need plugins' *.la files
%{__rm} $RPM_BUILD_ROOT%{gstlibdir}/*.la

%find_lang %{gstname}-%{gst_major_ver}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{gstname}-%{gst_major_ver}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README RELEASE
%attr(755,root,root) %{_libdir}/libgstbasecamerabinsrc-%{gst_major_ver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstbasecamerabinsrc-%{gst_major_ver}.so.0
%attr(755,root,root) %{_libdir}/libgstbasevideo-%{gst_major_ver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstbasevideo-%{gst_major_ver}.so.0
%attr(755,root,root) %{_libdir}/libgstphotography-%{gst_major_ver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstphotography-%{gst_major_ver}.so.0
%attr(755,root,root) %{_libdir}/libgstsignalprocessor-0.10.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstsignalprocessor-0.10.so.0
%if %{with vdpau}
%attr(755,root,root) %{_libdir}/libgstvdp-%{gst_major_ver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgstvdp-%{gst_major_ver}.so.0
%endif
%attr(755,root,root) %{gstlibdir}/libgstadpcmdec.so
%attr(755,root,root) %{gstlibdir}/libgstadpcmenc.so
%attr(755,root,root) %{gstlibdir}/libgstasfmux.so
%attr(755,root,root) %{gstlibdir}/libgstaudioparsersbad.so
%attr(755,root,root) %{gstlibdir}/libgstautoconvert.so
%attr(755,root,root) %{gstlibdir}/libgstaiff.so
%attr(755,root,root) %{gstlibdir}/libgstapexsink.so
%attr(755,root,root) %{gstlibdir}/libgstbayer.so
%attr(755,root,root) %{gstlibdir}/libgstbz2.so
%attr(755,root,root) %{gstlibdir}/libgstcamerabin.so
%attr(755,root,root) %{gstlibdir}/libgstcamerabin2.so
%attr(755,root,root) %{gstlibdir}/libgstcoloreffects.so
%attr(755,root,root) %{gstlibdir}/libgstcolorspace.so
%attr(755,root,root) %{gstlibdir}/libgstcdxaparse.so
%attr(755,root,root) %{gstlibdir}/libgstcog.so
%attr(755,root,root) %{gstlibdir}/libgstdataurisrc.so
%attr(755,root,root) %{gstlibdir}/libgstdccp.so
%attr(755,root,root) %{gstlibdir}/libgstdtmf.so
%attr(755,root,root) %{gstlibdir}/libgstdebugutilsbad.so
%attr(755,root,root) %{gstlibdir}/libgstdvb.so
%attr(755,root,root) %{gstlibdir}/libgstdvbsuboverlay.so
%attr(755,root,root) %{gstlibdir}/libgstdvdspu.so
%attr(755,root,root) %{gstlibdir}/libgstfbdevsink.so
%attr(755,root,root) %{gstlibdir}/libgstfestival.so
%attr(755,root,root) %{gstlibdir}/libgstfreeze.so
%attr(755,root,root) %{gstlibdir}/libgstfrei0r.so
%attr(755,root,root) %{gstlibdir}/libgstgaudieffects.so
%attr(755,root,root) %{gstlibdir}/libgstgeometrictransform.so
%attr(755,root,root) %{gstlibdir}/libgsth264parse.so
%attr(755,root,root) %{gstlibdir}/libgsthdvparse.so
%attr(755,root,root) %{gstlibdir}/libgstid3tag.so
%attr(755,root,root) %{gstlibdir}/libgstinterlace.so
%attr(755,root,root) %{gstlibdir}/libgstinvtelecine.so
%attr(755,root,root) %{gstlibdir}/libgstivfparse.so
%attr(755,root,root) %{gstlibdir}/libgstjp2k.so
%attr(755,root,root) %{gstlibdir}/libgstjp2kdecimator.so
%attr(755,root,root) %{gstlibdir}/libgstjpegformat.so
%attr(755,root,root) %{gstlibdir}/libgstlegacyresample.so
%attr(755,root,root) %{gstlibdir}/libgstliveadder.so
%attr(755,root,root) %{gstlibdir}/libgstmodplug.so
%attr(755,root,root) %{gstlibdir}/libgstmpeg4videoparse.so
%attr(755,root,root) %{gstlibdir}/libgstmpegdemux.so
%attr(755,root,root) %{gstlibdir}/libgstmpegpsmux.so
%attr(755,root,root) %{gstlibdir}/libgstmpegtsmux.so
%attr(755,root,root) %{gstlibdir}/libgstmpegvideoparse.so
%attr(755,root,root) %{gstlibdir}/libgstmve.so
%attr(755,root,root) %{gstlibdir}/libgstmxf.so
%attr(755,root,root) %{gstlibdir}/libgstnsf.so
%attr(755,root,root) %{gstlibdir}/libgstnuvdemux.so
%attr(755,root,root) %{gstlibdir}/libgstpcapparse.so
%attr(755,root,root) %{gstlibdir}/libgstpnm.so
%attr(755,root,root) %{gstlibdir}/libgstqtmux.so
%attr(755,root,root) %{gstlibdir}/libgstrawparse.so
%ifarch %{ix86} %{x8664}
%attr(755,root,root) %{gstlibdir}/libgstreal.so
%endif
%attr(755,root,root) %{gstlibdir}/libgstrfbsrc.so
%attr(755,root,root) %{gstlibdir}/libgstrsvg.so
%attr(755,root,root) %{gstlibdir}/libgstrtmp.so
%attr(755,root,root) %{gstlibdir}/libgstrtpmux.so
%attr(755,root,root) %{gstlibdir}/libgstscaletempoplugin.so
%attr(755,root,root) %{gstlibdir}/libgstsdpelem.so
%attr(755,root,root) %{gstlibdir}/libgstsegmentclip.so
%attr(755,root,root) %{gstlibdir}/libgstshm.so
%attr(755,root,root) %{gstlibdir}/libgstsiren.so
%attr(755,root,root) %{gstlibdir}/libgststereo.so
%attr(755,root,root) %{gstlibdir}/libgstsubenc.so
%attr(755,root,root) %{gstlibdir}/libgsttta.so
%attr(755,root,root) %{gstlibdir}/libgstvcdsrc.so
%if %{with vdpau}
%attr(755,root,root) %{gstlibdir}/libgstvdpau.so
%endif
%attr(755,root,root) %{gstlibdir}/libgstvideomaxrate.so
%attr(755,root,root) %{gstlibdir}/libgstvideosignal.so
%attr(755,root,root) %{gstlibdir}/libgstvideomeasure.so
%attr(755,root,root) %{gstlibdir}/libgstvmnc.so
%attr(755,root,root) %{gstlibdir}/libgsty4mdec.so
%{_gtkdocdir}/gst-plugins-bad-plugins-0.10

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgstbasecamerabinsrc-%{gst_major_ver}.so
%attr(755,root,root) %{_libdir}/libgstbasevideo-%{gst_major_ver}.so
%attr(755,root,root) %{_libdir}/libgstphotography-%{gst_major_ver}.so
%attr(755,root,root) %{_libdir}/libgstsignalprocessor-%{gst_major_ver}.so
%{_libdir}/libgstbasecamerabinsrc-%{gst_major_ver}.la
%{_libdir}/libgstbasevideo-%{gst_major_ver}.la
%{_libdir}/libgstphotography-%{gst_major_ver}.la
%{_libdir}/libgstsignalprocessor-%{gst_major_ver}.la
%{_includedir}/gstreamer-0.10/gst/basecamerabinsrc
%{_includedir}/gstreamer-0.10/gst/interfaces/photography-enumtypes.h
%{_includedir}/gstreamer-0.10/gst/interfaces/photography.h
%{_includedir}/gstreamer-0.10/gst/signalprocessor
%{_includedir}/gstreamer-0.10/gst/video/gstbasevideocodec.h
%{_includedir}/gstreamer-0.10/gst/video/gstbasevideodecoder.h
%{_includedir}/gstreamer-0.10/gst/video/gstbasevideoencoder.h
%{_includedir}/gstreamer-0.10/gst/video/gstbasevideoparse.h
%{_includedir}/gstreamer-0.10/gst/video/gstbasevideoutils.h
%if %{with vdpau}
%attr(755,root,root) %{_libdir}/libgstvdp-%{gst_major_ver}.so
%{_libdir}/libgstvdp-%{gst_major_ver}.la
%{_includedir}/gstreamer-0.10/gst/vdpau
%endif
%{_pkgconfigdir}/gstreamer-plugins-bad-%{gst_major_ver}.pc

##
## Plugins
##

%if %{with faad}
%files -n gstreamer-aac
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstfaac.so
%attr(755,root,root) %{gstlibdir}/libgstfaad.so
%endif

%if %{with amr}
%files -n gstreamer-amrwbenc
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstamrwbenc.so
# dirs should belong to gstreamer or gstreamer-pb?
%dir %{gstdatadir}
%dir %{gstdatadir}/presets
%{gstdatadir}/presets/GstAmrwbEnc.prs
%endif

%files -n gstreamer-ass
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstassrender.so

%files -n gstreamer-audio-effects-bad
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstspeed.so

%files -n gstreamer-audiosink-nas
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstnassink.so

%if %{with cdaudio}
%files -n gstreamer-cdaudio
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstcdaudio.so
%endif

%files -n gstreamer-celt
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstcelt.so

%files -n gstreamer-dc1394
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstdc1394.so

%if %{with dirac}
%files -n gstreamer-dirac
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstdirac.so
%endif

%if %{with divx4linux}
%files -n gstreamer-divx
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstdivxdec.so
%attr(755,root,root) %{gstlibdir}/libgstdivxenc.so
%endif

%if %{with dts}
%files -n gstreamer-dts
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstdtsdec.so
%endif

%files -n gstreamer-flite
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstflite.so

%files -n gstreamer-gme
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstgme.so

%files -n gstreamer-gsettings
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstgsettingselements.so
%{_datadir}/glib-2.0/schemas/org.freedesktop.gstreamer-0.10.default-elements.gschema.xml

%if %{with gsm}
%files -n gstreamer-gsm
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstgsm.so
%endif

%files -n gstreamer-kate
%defattr(644,root,root,755)
%doc ext/kate/README
%attr(755,root,root) %{gstlibdir}/libgstkate.so

%if %{with ladspa}
%files -n gstreamer-ladspa
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstladspa.so
%endif

%files -n gstreamer-lv2
%defattr(644,root,root,755)
%doc ext/lv2/README
%attr(755,root,root) %{gstlibdir}/libgstlv2.so

%files -n gstreamer-mimic
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstmimic.so

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

%if %{with musepack}
%files -n gstreamer-musepack
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstmusepack.so
%endif

%files -n gstreamer-musicbrainz
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgsttrm.so

%files -n gstreamer-mythtv
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstmythtvsrc.so

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

%files -n gstreamer-resindvd
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libresindvd.so

%files -n gstreamer-schroedinger
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstschro.so

%files -n gstreamer-soundtouch
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstsoundtouch.so

%files -n gstreamer-sndfile
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstsndfile.so

%if %{with spc}
%files -n gstreamer-spc
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstspc.so
%endif

%if %{with swfdec}
%files -n gstreamer-swfdec
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstswfdec.so
%endif

%files -n gstreamer-timidity
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgsttimidity.so

%files -n gstreamer-vp8
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstvp8.so

%if %{with sdl}
%files -n gstreamer-videosink-sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstsdl.so
%endif

%if %{with directfb}
%files -n gstreamer-videosink-directfb
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstdfbvideosink.so
%endif

%%files -n gstreamer-wildmidi
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstwildmidi.so

%if %{with xvid}
%files -n gstreamer-xvid
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstxvid.so
%endif

%files -n gstreamer-zbar
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstzbar.so
