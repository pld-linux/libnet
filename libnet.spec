Summary:	"libpwrite" Network Routine Library
Summary(pl):	Biblioteka czynno¶ci sieciowych
Name:		libnet
Version:	1.0.2a
Release:	3
Epoch:		1
License:	BSD
Group:		Libraries
Source0:	http://www.packetfactory.net/libnet/dist/%{name}-%{version}.tar.gz
Patch0:		%{name}-shared.patch
URL:		http://www.packetfactory.net/libnet/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Network Library provides a simple API for commonly used low-level
network functions (mainly packet injection). Using libnet, it is easy
to build and write arbitrary network packets. It provides a portable
framework for low-level network packet writing and handling (use
libnet in conjunction with libpcap and you can write some really cool
stuff). Libnet includes packet creation at the IP layer and at the
link layer as well as a host of supplementary and complementary
functionality.

%description -l pl
Biblioteka dostarcza API dla popularnych nisko-poziomowych funkcji
sieciowych (g³ównie wstrzykuj±cych pakiety).

%package devel
Summary:	Header files and develpment documentation for libnet
Summary(pl):	Pliki nag³ówkowe i dokumetacja do libnet
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files and develpment documentation for libnet.

%description -l pl devel
Pliki nag³ówkowe i dokumetacja do libnet.

%package static
Summary:	Static libnet library
Summary(pl):	Biblioteka statyczna libnet
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libnet library.

%description -l pl static
Biblioteka statyczna libnet.

%prep
%setup -q -n Libnet-%{version}
%patch0 -p1

%build
aclocal
autoconf
%configure \
	--with-pf_packet=yes
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	MAN_PREFIX=%{_mandir}/man3

(cd $RPM_BUILD_ROOT%{_libdir} ; ln -sf libnet.so.*.* libnet.so )
ln -sf libnet.so $RPM_BUILD_ROOT%{_libdir}/libpwrite

gzip -9nf README doc/CHANGELOG*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/libpwrite

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h
%{_includedir}/libnet
%{_mandir}/man*/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
