# TODO:
# new plugins:
# - ivorbis (BR: tremor-devel, CVS versions only, http://www.xiph.org/vorbis/)
#
# Conditional build:
%bcond_without	directfb	# don't build directfb videosink plugin
%bcond_without	faad		# don't build faad plugin
%bcond_without	gsm		# don't build gsm plugin
%bcond_without	mms		# don't build mms plugin
%bcond_without	musepack	# don't build musepack plugin
%bcond_without	sdl		# don't build sdl plugin
%bcond_without	wavpack		# don't build wavpack support
#
%define		gstname		gst-plugins-bad
%define		gst_major_ver	0.10
%define		gst_req_ver	0.10.0
#
Summary:	Bad GStreamer Streaming-media framework plugins
Summary(pl):	Z³e wtyczki do ¶rodowiska obróbki strumieni GStreamer
Name:		gstreamer-plugins-bad
Version:	0.10.0
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://gstreamer.freedesktop.org/src/gst-plugins-bad/%{gstname}-%{version}.tar.bz2
# Source0-md5:	3aa64cff481b0179023d71d9be5df7d5
Patch0:		%{name}-bashish.patch
URL:		http://gstreamer.freedesktop.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6
BuildRequires:	glib2-devel >= 1:2.6.0
BuildRequires:	gstreamer-devel >= %{gst_req_ver}
BuildRequires:	gstreamer-plugins-base-devel >= %{gst_req_ver}
BuildRequires:	gtk-doc >= 1.3
BuildRequires:	liboil-devel >= 0.3.0
BuildRequires:	libtool >= 1.4
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	rpmbuild(macros) >= 1.98
##
## plugins
##
%{?with_directfb:BuildRequires:	DirectFB-devel >= 0.9.24}
%{?with_sdl:BuildRequires:	SDL-devel >= 0.11}
BuildRequires:	faac-devel
%{?with_faad:BuildRequires:	faad2-devel >= 2.0-2}
%{?with_gsm:BuildRequires:	libgsm-devel}
%{?with_mms:BuildRequires:	libmms-devel >= 0.1}
%{?with_musepack:BuildRequires:	libmpcdec-devel >= 1.2}
%{?with_wavpack:BuildRequires:	wavpack-devel >= 4.2}
Requires:	gstreamer >= %{gst_req_ver}
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

%description -l pl
GStreamer to ¶rodowisko obróbki danych strumieniowych, bazuj±ce na
grafie filtrów operuj±cych na danych medialnych. Aplikacje u¿ywaj±ce
tej biblioteki mog± robiæ wszystko od przetwarzania d¼wiêku w czasie
rzeczywistym, do odtwarzania filmów i czegokolwiek innego zwi±zego z
mediami. Architektura bazuj±ca na wtyczkach pozwala na ³atwe dodawanie
nowych typów danych lub mo¿liwo¶ci obróbki.

##
## Plugins
##

%package -n gstreamer-aac
Summary:	GStreamer plugin for AAC audio encoding and decoding
Summary(pl):	Wtyczka do GStreamera do kodowania i dekodowania plików audio AAC
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gst_req_ver}

%description -n gstreamer-aac
GStreamer plugin for AAC audio encoding and decoding.

%description -n gstreamer-aac -l pl
Wtyczka do GStreamera do kodowania i dekodowania plików audio AAC.

%package -n gstreamer-audio-effects-bad
Summary:	Bad GStreamer audio effects plugins
Summary(pl):	Z³e wtyczki efektów d¼wiêkowych do GStreamera
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}
Obsoletes:	gstreamer-audio-effects

%description -n gstreamer-audio-effects-bad
Bad GStreamer audio effects plugins.

%description -n gstreamer-audio-effects-bad -l pl
Z³e wtyczki efektów d¼wiêkowych do GStreamera.

%package -n gstreamer-gsm
Summary:	GStreamer plugin for GSM lossy audio format
Summary(pl):	Wtyczka do GStreamera obs³uguj±ca stratny format d¼wiêku GSM
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gst_req_ver}

%description -n gstreamer-gsm
Output plugin for GStreamer to convert to GSM lossy audio format.

%description -n gstreamer-gsm -l pl
Wtyczka wyj¶cia d¼wiêku GSteamera konwertuj±ca do stratnego formatu
GSM.

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

%package -n gstreamer-videosink-sdl
Summary:	GStreamer plugin for outputing to SDL
Summary(pl):	Wtyczka wyj¶cia SDL do GStreamera
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gst_req_ver}
Provides:	gstreamer-videosink = %{version}
Obsoletes:	gstreamer-SDL

%description -n gstreamer-videosink-sdl
Plugin for sending output to the Simple Direct Media architecture.
(http://www.libsdl.org/). Usefull for fullscreen playback.

%description -n gstreamer-videosink-sdl -l pl
Wtyczka przekazuj±ca wyj¶cie do architektury SDL. U¿yteczna do
odtwarzania na pe³nym ekranie.

%package -n gstreamer-videosink-directfb
Summary:	GStreamer DirectFB output plugin
Summary(pl):	Wtyczka wyj¶cia obrazu DirectFB do GStreamera
Group:		Libraries
Requires:	gstreamer-plugins-base >= %{gst_req_ver}
Provides:	gstreamer-videosink = %{version}

%description -n gstreamer-videosink-directfb
GStreamer DirectFB output plugin.

%description -n gstreamer-videosink-directfb -l pl
Wtyczka wyj¶cia obrazu DirectFB do GStreamera.

%package -n gstreamer-wavpack
Summary:	GStreamer plugin for Wavpack lossless audio format
Summary(pl):	Wtyczka do GStreamera obs³uguj±ca bezstratny format d¼wiêku Wavpack
Group:		Libraries
Requires:	gstreamer >= %{gst_req_ver}

%description -n gstreamer-wavpack
Plugin for lossless Wavpack audio format.

%description -n gstreamer-wavpack -l pl
Wtyczka obs³uguj±ca bezstratny format d¼wiêku Wavpack.

%prep
%setup -q -n %{gstname}-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4 -I common/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_faad:--disable-faad} \
	%{!?with_gsm:--disable-gsm} \
	%{!?with_mms:--disable-libmms} \
	%{!?with_musepack:--disable-musepack} \
	%{!?with_sdl:--disable-sdl} \
	%{!?with_sdl:--disable-sdltest} \
	%{!?with_wavpack:--disable-wavpack} \
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README RELEASE
%attr(755,root,root) %{gstlibdir}/libgstqtdemux.so
%attr(755,root,root) %{gstlibdir}/libgsttta.so
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

%if %{with gsm}
%files -n gstreamer-gsm
%defattr(644,root,root,755)
%attr(755,root,root) %{gstlibdir}/libgstgsm.so
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
