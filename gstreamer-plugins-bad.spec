# TODO:
# new plugins:
# - ivorbis (BR: tremor-devel, CVS versions only, http://www.xiph.org/vorbis/)
# - amrwb (needs external code in tree; but maybe use shared lib?)
# - theoradec (BR: libtheora-exp, http://people.xiph.org/~tterribe/doc/libtheora-exp/)
# - system libmodplug?
#
# Conditional build:
%bcond_without	directfb	# don't build directfb videosink plugin
%bcond_without	dts		# don't build DTS plugin
%bcond_without	faad		# don't build faad plugin
%bcond_without	gsm		# don't build gsm plugin
%bcond_without	mms		# don't build mms plugin
%bcond_without	musepack	# don't build musepack plugin
%bcond_without	neon		# don't build neonhttpsrc plugin
%bcond_without	sdl		# don't build sdl plugin
%bcond_without	swfdec		# don't build swfdec plugin
%bcond_without	wavpack		# don't build wavpack support
%bcond_without	xvid		# don't build XviD support
%bcond_with	divx4linux	# build with divx4linux support
#
%define		gstname		gst-plugins-bad
%define		gst_major_ver	0.10
%define		gst_req_ver	0.10.3
#
Summary:	Bad GStreamer Streaming-media framework plugins
Summary(pl):	Z�e wtyczki do �rodowiska obr�bki strumieni GStreamer
Name:		gstreamer-plugins-bad
Version:	0.10.3
Release:	3
License:	LPL
Group:		Libraries
Source0:	http://gstreamer.freedesktop.org/src/gst-plugins-bad/%{gstname}-%{version}.tar.bz2
# Source0-md5:	8545a02c408976c5e9f0c2cf3c6a362e
Patch0:		%{name}-bashish.patch
Patch1:		%{name}-libdts.patch
Patch2:		%{name}-divx4linux.patch
Patch3:		%{name}-soundtouch.patch
Patch4:		%{name}-neon.patch
URL:		http://gstreamer.freedesktop.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6
BuildRequires:	bzip2-devel
BuildRequires:	glib2-devel >= 1:2.6.0
BuildRequires:	gstreamer-devel >= %{gst_req_ver}
BuildRequires:	gstreamer-plugins-base-devel >= %{gst_req_ver}
BuildRequires:	gtk-doc >= 1.3
BuildRequires:	liboil-devel >= 0.3.2
BuildRequires:	libtool >= 1.4
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	rpmbuild(macros) >= 1.98
##
## plugins
##
%{?with_directfb:BuildRequires:	DirectFB-devel >= 1:0.9.24}
BuildRequires:	OpenGL-devel
%{?with_sdl:BuildRequires:	SDL-devel >= 0.11}
%{?with_divx4linux:BuildRequires:	divx4linux-devel >= 1:5.05.20030428}
BuildRequires:	faac-devel
%{?with_faad:BuildRequires:	faad2-devel >= 2.0-2}
%{?with_dts:BuildRequires:	libdts-devel}
%{?with_gsm:BuildRequires:	libgsm-devel}
%{?with_mms:BuildRequires:	libmms-devel >= 0.2}
%{?with_musepack:BuildRequires:	libmpcdec-devel >= 1.2}
BuildRequires:	libmusicbrainz-devel >= 2.1.0
# for modplug and libSoundTouch
BuildRequires:	libstdc++-devel
%{?with_neon:BuildRequires:	neon-devel >= 0.26}
BuildRequires:	soundtouch-devel >= 1.3.1
%{?with_swfdec:BuildRequires:	swfdec-devel >= 0.3.6}
%{?with_wavpack:BuildRequires:	wavpack-devel >= 4.2}
%{?with_xvid:BuildRequires:	xvid-devel >= 1.0.0}
Requires:	gstreamer >= %{gst_req_ver}
Requires:	gstreamer-plugins-base >= %{gst_req_ver}
Obsoletes:	gstreamer-quicktime
Obsoletes:	gstreamer-v4l2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		gstlibdir 	%{_libdir}/gstreamer-%{gst_major_ver}

%description
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related. Its plugin-based architecture means
that new data types or processing capabilities can be added simply by
installing new plugins.

%description -l pl
GStreamer to �rodowisko obr�bki danych strumieniowych, bazuj�ce na
grafie filtr�w operuj�cych na danych medialnych. Aplikacje u�ywaj�ce
tej biblioteki mog� robi� wszystko od przetwarzania d�wi�ku w czasie
rzeczywistym, do odtwarzania film�w i czegokolwiek innego zwi�zego z
mediami. Architektura bazuj�ca na wtyczkach pozwala na �atwe dodawanie
nowych typ�w danych lub mo�liwo�ci obr�bki.

##
## Plugins
##

%package -n gstreamer-aac
Summary:	GStreamer plugin for AAC audio encoding and decoding
Summary(pl):	Wtyczka do GStreamera do kodowania i dekodowania plik�w audio AAC
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gst_req_ver}

%description -n gstreamer-aac
GStreamer plugin for AAC audio encoding and decoding.

%description -n gstreamer-aac -l pl
Wtyczka do GStreamera do kodowania i dekodowania plik�w audio AAC.

%package -n gstreamer-audio-effects-bad
Summary:	Bad GStreamer audio effects plugins
Summary(pl):	Z�e wtyczki efekt�w d�wi�kowych do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}
Obsoletes:	gstreamer-audio-effects

%description -n gstreamer-audio-effects-bad
Bad GStreamer audio effects plugins.

%description -n gstreamer-audio-effects-bad -l pl
Z�e wtyczki efekt�w d�wi�kowych do GStreamera.

%package -n gstreamer-divx
Summary:	GStreamer divx plugin
Summary(pl):	Wtyczka divx do GStreamera
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gst_req_ver}

%description -n gstreamer-divx
GStreamer divx plugin.

%description -n gstreamer-divx -l pl
Wtyczka divx do GStreamera.

%package -n gstreamer-dts
Summary:	GStreamer DTS plugin
Summary(pl):	Wtyczka DTS do GStreamera
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gst_req_ver}

%description -n gstreamer-dts
Plugin for DTS Coherent Acoustics support.

%description -n gstreamer-dts -l pl
Wtyczka do GStreamera obs�uguj�ca DTS Coherent Acoustics.

%package -n gstreamer-gsm
Summary:	GStreamer plugin for GSM lossy audio format
Summary(pl):	Wtyczka do GStreamera obs�uguj�ca stratny format d�wi�ku GSM
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gst_req_ver}

%description -n gstreamer-gsm
Output plugin for GStreamer to convert to GSM lossy audio format.

%description -n gstreamer-gsm -l pl
Wtyczka wyj�cia d�wi�ku GSteamera konwertuj�ca do stratnego formatu
GSM.

%package -n gstreamer-imagesink-gl
Summary:	GStreamer plugin for outputing to OpenGL
Summary(pl):	Wtyczka wyj�cia OpenGL do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}
Provides:	gstreamer-imagesink = %{version}

%description -n gstreamer-imagesink-gl
GStreamer plugin for outputing to OpenGL.

%description -n gstreamer-imagesink-gl -l pl
Wtyczka wyj�cia OpenGL do GStreamera.

%package -n gstreamer-mms
Summary:	GStreamer mms plugin
Summary(pl):	Wtyczka mms do GStreamera
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gst_req_ver}

%description -n gstreamer-mms
GStreamer mms plugin.

%description -n gstreamer-mms -l pl
Wtyczka mms do GStreamera.

%package -n gstreamer-musepack
Summary:	GStreamer musepack plugin
Summary(pl):	Wtyczka musepack do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}

%description -n gstreamer-musepack
GStreamer musepack plugin.

%description -n gstreamer-musepack -l pl
Wtyczka musepack do GStreamera.

%package -n gstreamer-musicbrainz
Summary:	GStreamer musicbrainz plugin
Summary(pl):	Wtyczka musicbrainz do GStreamera
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gst_req_ver}

%description -n gstreamer-musicbrainz
GStreamer musicbrainz plugin - a TRM signature producer.

%description -n gstreamer-musicbrainz -l pl
Wtyczka musicbrainz do GStreamera, tworz�ca sygnatury TRM.

%package -n gstreamer-neon
Summary:	GStreamer neon HTTP source plugin
Summary(pl):	Wtyczka �r�d�a HTTP neon do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}

%description -n gstreamer-neon
GStreamer neon HTTP source plugin.

%description -n gstreamer-neon -l pl
Wtyczka �r�d�a HTTP neon do GStreamera.

%package -n gstreamer-soundtouch
Summary:	GStreamer soundtouch plugin
Summary(pl):	Wtyczka soundtouch do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}

%description -n gstreamer-soundtouch
GStreamer soundtouch source plugin - audio pitch controller.

%description -n gstreamer-soundtouch -l pl
Wtyczka soundtouch do GStreamera, steruj�ca wysoko�ci� d�wi�ku.

%package -n gstreamer-swfdec
Summary:	GStreamer Flash redering plugin
Summary(pl):	Wtyczka renderuj�ca animacje flash dla GStreamera
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gst_req_ver}
Requires:	swfdec >= 0.3.6

%description -n gstreamer-swfdec
Plugin for rendering Flash animations using swfdec library.

%description -n gstreamer-swfdec -l pl
Wtyczka renderuj�ca animacje flash w oparciu o bibliotek� swfdec.

%package -n gstreamer-videosink-sdl
Summary:	GStreamer plugin for outputing to SDL
Summary(pl):	Wtyczka wyj�cia SDL do GStreamera
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gst_req_ver}
Provides:	gstreamer-videosink = %{version}
Obsoletes:	gstreamer-SDL

%description -n gstreamer-videosink-sdl
Plugin for sending output to the Simple Direct Media architecture.
(http://www.libsdl.org/). Usefull for fullscreen playback.

%description -n gstreamer-videosink-sdl -l pl
Wtyczka przekazuj�ca wyj�cie do architektury SDL. U�yteczna do
odtwarzania na pe�nym ekranie.

%package -n gstreamer-videosink-directfb
Summary:	GStreamer DirectFB output plugin
Summary(pl):	Wtyczka wyj�cia obrazu DirectFB do GStreamera
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gst_req_ver}
Provides:	gstreamer-videosink = %{version}

%description -n gstreamer-videosink-directfb
GStreamer DirectFB output plugin.

%description -n gstreamer-videosink-directfb -l pl
Wtyczka wyj�cia obrazu DirectFB do GStreamera.

%package -n gstreamer-wavpack
Summary:	GStreamer plugin for Wavpack lossless audio format
Summary(pl):	Wtyczka do GStreamera obs�uguj�ca bezstratny format d�wi�ku Wavpack
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}

%description -n gstreamer-wavpack
Plugin for lossless Wavpack audio format.

%description -n gstreamer-wavpack -l pl
Wtyczka obs�uguj�ca bezstratny format d�wi�ku Wavpack.

%package -n gstreamer-xvid
Summary:	GStreamer xvid decoder plugin
Summary(pl):	Wtyczka do GStreamera dekoduj�ca przy u�yciu biblioteki xvid
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gst_req_ver}

%description -n gstreamer-xvid
GStreamer xvid decoder plugin.

%description -n gstreamer-xvid -l pl
Wtyczka do GStreamera dekoduj�ca przy u�yciu biblioteki xvid.

%prep
%setup -q -n %{gstname}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4 -I common/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_divx4linux:--disable-divx} \
	%{!?with_dts:--disable-dts} \
	%{!?with_faad:--disable-faad} \
	%{!?with_gsm:--disable-gsm} \
	%{!?with_mms:--disable-libmms} \
	%{!?with_musepack:--disable-musepack} \
	%{!?with_neon:--disable-neon} \
	%{!?with_sdl:--disable-sdl} \
	%{!?with_sdl:--disable-sdltest} \
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
%attr(755,root,root) %{gstlibdir}/libgstfreeze.so
%attr(755,root,root) %{gstlibdir}/libgstmodplug.so
%attr(755,root,root) %{gstlibdir}/libgstqtdemux.so
%attr(755,root,root) %{gstlibdir}/libgsttta.so
%attr(755,root,root) %{gstlibdir}/libgstvideo4linux2.so
%attr(755,root,root) %{gstlibdir}/libgstxingheader.so
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

%files -n gstreamer-audio-effects-bad
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstspeed.so

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
