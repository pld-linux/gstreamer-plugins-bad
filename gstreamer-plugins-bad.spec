# TODO:
# new plugins:
# - ivorbis (BR: tremor-devel, CVS versions only, http://www.xiph.org/vorbis/)
# - theoradec (BR: libtheora-exp, http://people.xiph.org/~tterribe/doc/libtheora-exp/)
# - system libmodplug?
#
# Conditional build:
%bcond_without	cdaudio		# don't build cdaudio plugin
%bcond_without	directfb	# don't build directfb videosink plugin
%bcond_without	dts		# don't build DTS plugin
%bcond_without	faad		# don't build faad plugin
%bcond_without	gsm		# don't build gsm plugin
%bcond_without	jack		# don't build JACK audio plugin
%bcond_without	ladspa		# don't build ladspa plugin
%bcond_without	mjpegtools	# don't build mpeg2enc plugin
%bcond_without	mms		# don't build mms plugin
%bcond_without	musepack	# don't build musepack plugin
%bcond_without	neon		# don't build neonhttpsrc plugin
%bcond_without	sdl		# don't build sdl plugin
%bcond_without	swfdec		# don't build swfdec plugin
%bcond_without	spc		# don't build spc plugin
%bcond_without	wavpack		# don't build wavpack plugin
%bcond_without	xvid		# don't build XviD plugin
%bcond_with	amr		# build amrwb plugin
%bcond_with	divx4linux	# build divx4linux plugins
#
%define		gstname		gst-plugins-bad
%define		gst_major_ver	0.10
%define		gst_req_ver	0.10.10.1
#
Summary:	Bad GStreamer Streaming-media framework plugins
Summary(pl.UTF-8):	Złe wtyczki do środowiska obróbki strumieni GStreamer
Name:		gstreamer-plugins-bad
Version:	0.10.4
Release:	5
License:	LPL
Group:		Libraries
Source0:	http://gstreamer.freedesktop.org/src/gst-plugins-bad/%{gstname}-%{version}.tar.bz2
# Source0-md5:	2e57395cdf72733477fb328f1fa3f053
Patch0:		%{name}-bashish.patch
Patch1:		%{name}-libdts.patch
Patch2:		%{name}-divx4linux.patch
Patch3:		%{name}-soundtouch.patch
Patch4:		%{name}-amrwb.patch
Patch5:		%{name}-faad.patch
Patch6:		%{name}-link.patch
URL:		http://gstreamer.freedesktop.org/
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake >= 1.6
BuildRequires:	glib2-devel >= 1:2.12.0
BuildRequires:	gstreamer-devel >= %{gst_req_ver}
BuildRequires:	gstreamer-plugins-base-devel >= %{gst_req_ver}
BuildRequires:	gtk-doc >= 1.6
BuildRequires:	liboil-devel >= 0.3.6
BuildRequires:	libtool >= 1.4
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	python-PyXML
BuildRequires:	rpmbuild(macros) >= 1.98
##
## plugins
##
%{?with_directfb:BuildRequires:	DirectFB-devel >= 1:0.9.24}
BuildRequires:	OpenGL-devel
%{?with_sdl:BuildRequires:	SDL-devel >= 0.11}
BuildRequires:	alsa-lib-devel >= 0.9.1
%{?with_amr:BuildRequires:	amrwb-devel}
BuildRequires:	bzip2-devel
%{?with_divx4linux:BuildRequires:	divx4linux-devel >= 1:5.05.20030428}
BuildRequires:	faac-devel
%{?with_faad:BuildRequires:	faad2-devel >= 2.0-2}
%{?with_jack:BuildRequires:	jack-audio-connection-kit-devel >= 0.99.10}
%{?with_ladspa:BuildRequires:	ladspa-devel >= 1.12}
%{?with_cdaudio:BuildRequires:	libcdaudio-devel}
%{?with_dts:BuildRequires:	libdts-devel}
%{?with_gsm:BuildRequires:	libgsm-devel}
%{?with_mms:BuildRequires:	libmms-devel >= 0.2}
%{?with_musepack:BuildRequires:	libmpcdec-devel >= 1.2}
BuildRequires:	libmusicbrainz-devel >= 2.1.0
%{?with_spc:BuildRequires:	libopenspc-devel >= 0.3.99}
# for modplug and libSoundTouch
BuildRequires:	libstdc++-devel
%{?with_mjpegtools:BuildRequires:	mjpegtools-devel >= 1.8.0-0.2}
%{?with_mjpegtools:BuildRequires:	mjpegtools-devel < 1.9.0}
%{?with_neon:BuildRequires:	neon-devel >= 0.26}
BuildRequires:	soundtouch-devel >= 1.3.1
%{?with_swfdec:BuildRequires:	swfdec-devel >= 0.3.6}
%{?with_wavpack:BuildRequires:	wavpack-devel >= 4.40.0}
BuildRequires:	xorg-lib-libX11-devel
%{?with_xvid:BuildRequires:	xvid-devel >= 1.0.0}
Requires:	gstreamer >= %{gst_req_ver}
Requires:	gstreamer-plugins-base >= %{gst_req_ver}
Obsoletes:	gstreamer-quicktime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		gstlibdir 	%{_libdir}/gstreamer-%{gst_major_ver}

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

##
## Plugins
##

%package -n gstreamer-aac
Summary:	GStreamer plugin for AAC audio encoding and decoding
Summary(pl.UTF-8):	Wtyczka do GStreamera do kodowania i dekodowania plików audio AAC
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gst_req_ver}

%description -n gstreamer-aac
GStreamer plugin for AAC audio encoding and decoding.

%description -n gstreamer-aac -l pl.UTF-8
Wtyczka do GStreamera do kodowania i dekodowania plików audio AAC.

%package -n gstreamer-amrwb
Summary:	GStreamer plugin for AMR-WB audio encoding and decoding
Summary(pl.UTF-8):	Wtyczka GStreamera do kodowania i dekodowania dźwięku w formacie AMR-WB
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}

%description -n gstreamer-amrwb
GStreamer plugin for AMR-WB audio encoding and decoding.

%description -n gstreamer-amrwb -l pl.UTF-8
Wtyczka GStreamera do kodowania i dekodowania dźwięku w formacie
AMR-WB.

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

%package -n gstreamer-audiosink-alsaspdif
Summary:	GStreamer ALSA plugin for S/PDIF output
Summary(pl.UTF-8):	Wtyczka ALSA GStreamera do wyjścia S/PDIF
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gst_req_ver}
Provides:	gstreamer-audiosink = %{version}

%description -n gstreamer-audiosink-alsaspdif
GStreamer ALSA plugin for S/PDIF output.

%description -n gstreamer-audiosink-alsaspdif -l pl.UTF-8
Wtyczka ALSA GStreamera do wyjścia S/PDIF.

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

%package -n gstreamer-divx
Summary:	GStreamer divx plugin
Summary(pl.UTF-8):	Wtyczka divx do GStreamera
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gst_req_ver}

%description -n gstreamer-divx
GStreamer divx plugin.

%description -n gstreamer-divx -l pl.UTF-8
Wtyczka divx do GStreamera.

%package -n gstreamer-dts
Summary:	GStreamer DTS plugin
Summary(pl.UTF-8):	Wtyczka DTS do GStreamera
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gst_req_ver}

%description -n gstreamer-dts
Plugin for DTS Coherent Acoustics support.

%description -n gstreamer-dts -l pl.UTF-8
Wtyczka do GStreamera obsługująca DTS Coherent Acoustics.

%package -n gstreamer-gsm
Summary:	GStreamer plugin for GSM lossy audio format
Summary(pl.UTF-8):	Wtyczka do GStreamera obsługująca stratny format dźwięku GSM
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gst_req_ver}

%description -n gstreamer-gsm
Output plugin for GStreamer to convert to GSM lossy audio format.

%description -n gstreamer-gsm -l pl.UTF-8
Wtyczka wyjścia dźwięku GSteamera konwertująca do stratnego formatu
GSM.

%package -n gstreamer-imagesink-gl
Summary:	GStreamer plugin for outputing to OpenGL
Summary(pl.UTF-8):	Wtyczka wyjścia OpenGL do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}
Provides:	gstreamer-imagesink = %{version}

%description -n gstreamer-imagesink-gl
GStreamer plugin for outputing to OpenGL.

%description -n gstreamer-imagesink-gl -l pl.UTF-8
Wtyczka wyjścia OpenGL do GStreamera.

%package -n gstreamer-jack
Summary:	GStreamer plugin for the JACK Sound Server
Summary(pl.UTF-8):	Wtyczka serwera dźwięku JACK dla GStreamera
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gst_req_ver}
Provides:	gstreamer-audiosink = %{version}

%description -n gstreamer-jack
Plugin for the JACK professional sound server.

%description -n gstreamer-jack -l pl.UTF-8
Wtyczka dla profesjonalnego serwera dźwięku JACK.

%package -n gstreamer-ladspa
Summary:	GStreamer wrapper for LADSPA plugins
Summary(pl.UTF-8):	Wrapper do wtyczek LADSPA dla GStreamera
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gst_req_ver}

%description -n gstreamer-ladspa
Plugin which wraps LADSPA plugins for use by GStreamer applications.

%description -n gstreamer-ladspa -l pl.UTF-8
Wtyczka pozwalająca na używanie wtyczek LADSPA przez aplikacje
GStreamera.

%package -n gstreamer-mjpegtools
Summary:	GStreamer mpeg2enc plugin
Summary(pl.UTF-8):	Wtyczka mpeg2enc do GStreamera
Group:		Libraries

%description -n gstreamer-mjpegtools
GStreamer mpeg2enc plugin (based on mjpegtools libraries).

%description -n gstreamer-mjpegtools -l pl.UTF-8
Wtyczka mpeg2enc do GStreamera (oparta na bibliotekach mjpegtools).

%package -n gstreamer-mms
Summary:	GStreamer mms plugin
Summary(pl.UTF-8):	Wtyczka mms do GStreamera
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gst_req_ver}

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

%package -n gstreamer-musicbrainz
Summary:	GStreamer musicbrainz plugin
Summary(pl.UTF-8):	Wtyczka musicbrainz do GStreamera
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gst_req_ver}

%description -n gstreamer-musicbrainz
GStreamer musicbrainz plugin - a TRM signature producer.

%description -n gstreamer-musicbrainz -l pl.UTF-8
Wtyczka musicbrainz do GStreamera, tworząca sygnatury TRM.

%package -n gstreamer-neon
Summary:	GStreamer neon HTTP source plugin
Summary(pl.UTF-8):	Wtyczka źródła HTTP neon do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}

%description -n gstreamer-neon
GStreamer neon HTTP source plugin.

%description -n gstreamer-neon -l pl.UTF-8
Wtyczka źródła HTTP neon do GStreamera.

%package -n gstreamer-soundtouch
Summary:	GStreamer soundtouch plugin
Summary(pl.UTF-8):	Wtyczka soundtouch do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}

%description -n gstreamer-soundtouch
GStreamer soundtouch source plugin - audio pitch controller.

%description -n gstreamer-soundtouch -l pl.UTF-8
Wtyczka soundtouch do GStreamera, sterująca wysokością dźwięku.

%package -n gstreamer-spc
Summary:	GStreamer SPC plugin
Summary(pl.UTF-8):	Wtyczka SPC dla GStreamera
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gst_req_ver}
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
Requires:	gstreamer-plugins-base >= %{gst_req_ver}
Requires:	swfdec >= 0.3.6

%description -n gstreamer-swfdec
Plugin for rendering Flash animations using swfdec library.

%description -n gstreamer-swfdec -l pl.UTF-8
Wtyczka renderująca animacje flash w oparciu o bibliotekę swfdec.

%package -n gstreamer-videosink-sdl
Summary:	GStreamer plugin for outputing to SDL
Summary(pl.UTF-8):	Wtyczka wyjścia SDL do GStreamera
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gst_req_ver}
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
Requires:	gstreamer-plugins-base >= %{gst_req_ver}
Provides:	gstreamer-videosink = %{version}

%description -n gstreamer-videosink-directfb
GStreamer DirectFB output plugin.

%description -n gstreamer-videosink-directfb -l pl.UTF-8
Wtyczka wyjścia obrazu DirectFB do GStreamera.

%package -n gstreamer-wavpack
Summary:	GStreamer plugin for Wavpack lossless audio format
Summary(pl.UTF-8):	Wtyczka do GStreamera obsługująca bezstratny format dźwięku Wavpack
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}

%description -n gstreamer-wavpack
Plugin for lossless Wavpack audio format.

%description -n gstreamer-wavpack -l pl.UTF-8
Wtyczka obsługująca bezstratny format dźwięku Wavpack.

%package -n gstreamer-xvid
Summary:	GStreamer xvid decoder plugin
Summary(pl.UTF-8):	Wtyczka do GStreamera dekodująca przy użyciu biblioteki xvid
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gst_req_ver}

%description -n gstreamer-xvid
GStreamer xvid decoder plugin.

%description -n gstreamer-xvid -l pl.UTF-8
Wtyczka do GStreamera dekodująca przy użyciu biblioteki xvid.

%prep
%setup -q -n %{gstname}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4 -I common/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_cdaudio:--disable-cdaudio} \
	%{!?with_divx4linux:--disable-divx} \
	%{!?with_dts:--disable-dts} \
	%{!?with_faad:--disable-faad} \
	%{!?with_gsm:--disable-gsm} \
	%{!?with_jack:--disable-jack} \
	%{!?with_ladspa:--disable-ladspa} \
	%{!?with_mms:--disable-libmms} \
	%{!?with_mjpegtools:--disable-mpeg2enc} \
	%{!?with_musepack:--disable-musepack} \
	%{!?with_neon:--disable-neon} \
	%{!?with_sdl:--disable-sdl} \
	%{!?with_sdl:--disable-sdltest} \
	%{!?with_spc:--disable-spc} \
	%{!?with_swfdec:--disable-swfdec} \
	%{!?with_wavpack:--disable-wavpack} \
	%{!?with_xvid:--disable-xvid} \
	--disable-static \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# We don't need plugins' *.la files
rm -f $RPM_BUILD_ROOT%{gstlibdir}/*.la

%find_lang %{gstname}-%{gst_major_ver}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{gstname}-%{gst_major_ver}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README RELEASE
%attr(755,root,root) %{gstlibdir}/libgstbz2.so
%attr(755,root,root) %{gstlibdir}/libgstcdxaparse.so
%attr(755,root,root) %{gstlibdir}/libgstdeinterlace.so
%attr(755,root,root) %{gstlibdir}/libgstdvbsrc.so
%attr(755,root,root) %{gstlibdir}/libgstfilter.so
%attr(755,root,root) %{gstlibdir}/libgstfreeze.so
%attr(755,root,root) %{gstlibdir}/libgsth264parse.so
%attr(755,root,root) %{gstlibdir}/libgstmodplug.so
%attr(755,root,root) %{gstlibdir}/libgstmultifile.so
%attr(755,root,root) %{gstlibdir}/libgstnsf.so
%attr(755,root,root) %{gstlibdir}/libgstnuvdemux.so
%attr(755,root,root) %{gstlibdir}/libgstqtdemux.so
%attr(755,root,root) %{gstlibdir}/libgstreplaygain.so
%attr(755,root,root) %{gstlibdir}/libgstrfbsrc.so
%attr(755,root,root) %{gstlibdir}/libgstspectrum.so
%attr(755,root,root) %{gstlibdir}/libgsttta.so
%attr(755,root,root) %{gstlibdir}/libgstvideocrop.so
%attr(755,root,root) %{gstlibdir}/libgstvideoparse.so
%attr(755,root,root) %{gstlibdir}/libgstxingheader.so
%attr(755,root,root) %{gstlibdir}/libgsty4menc.so
%{_gtkdocdir}/gst-plugins-bad-plugins-*

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
%files -n gstreamer-amrwb
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstamrwb.so
%endif

%files -n gstreamer-audio-effects-bad
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstspeed.so

%files -n gstreamer-audiosink-alsaspdif
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstalsaspdif.so

%if %{with cdaudio}
%files -n gstreamer-cdaudio
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstcdaudio.so
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

%if %{with gsm}
%files -n gstreamer-gsm
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstgsm.so
%endif

%files -n gstreamer-imagesink-gl
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstglimagesink.so

%if %{with jack}
%files -n gstreamer-jack
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstjack.so
%endif

%if %{with ladspa}
%files -n gstreamer-ladspa
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstladspa.so
%endif

%if %{with mjpegtools}
%files -n gstreamer-mjpegtools
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstmpeg2enc.so
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

%if %{with neon}
%files -n gstreamer-neon
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstneonhttpsrc.so
%endif

%files -n gstreamer-soundtouch
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstpitch.so

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

%if %{with sdl}
%files -n gstreamer-videosink-sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstsdlvideosink.so
%endif

%if %{with directfb}
%files -n gstreamer-videosink-directfb
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstdfbvideosink.so
%endif

%if %{with wavpack}
%files -n gstreamer-wavpack
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstwavpack.so
%endif

%if %{with xvid}
%files -n gstreamer-xvid
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstxvid.so
%endif
