Summary:	"libpwrite" Network Routine Library
Summary(pl):	Biblioteka czynno¶ci sieciowych
Summary(pt_BR):	API para funções de rede de baixo nível
Name:		libnet
Version:	1.1.0
Release:	3
Epoch:		1
License:	BSD
Group:		Libraries
Source0:	http://www.packetfactory.net/libnet/dist/%{name}-%{version}.tar.gz
# Source0-md5:	b46e650d9d0e7ad5ef9439c7cd281922
Patch0:		%{name}-shared.patch
URL:		http://www.packetfactory.net/libnet/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpcap-devel
BuildRequires:	libtool
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

%description -l pt_BR
Este pacote fornece uma API simples para funções de rede de baixo
nível comumente usadas (principalmente injeção de pacotes). Usando
libnet, é simples construir e enviar pacotes de rede arbitrários.

%package devel
Summary:	Header files and develpment documentation for libnet
Summary(pl):	Pliki nag³ówkowe i dokumetacja do libnet
Summary(pt_BR):	Arquivos do pacote libnet para desenvolvimento
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}

%description devel
Header files and develpment documentation for libnet.

%description devel -l pl
Pliki nag³ówkowe i dokumetacja do libnet.

%description devel -l pt_BR
Arquivos de cabeçalho e bibliotecas usadas no desenvolvimento de
aplicativos que usam libnet.

%package static
Summary:	Static libnet library
Summary(pl):	Biblioteka statyczna libnet
Summary(pt_BR):	Arquivos do pacote libnet para desenvolvimento estático
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}

%description static
Static libnet library.

%description static -l pl
Biblioteka statyczna libnet.

%description static -l pt_BR
Arquivos de cabeçalho e bibliotecas usadas no desenvolvimento de
aplicativos estáticos que usam libnet.

%package examples
Summary:        libnet - example programs
Summary(pl):    libnet - programy przyk³adowe
Group:          Development/Libraries
Requires:       %{name}-devel = %{epoch}:%{version}
Requires:       %{name}-static = %{epoch}:%{version}

%description examples
libnet - example programs.

%description examples -l pl
libnet - programy przyk³adowe.

%prep
%setup -q -n Libnet-latest
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-pf_packet=yes
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	MAN_PREFIX=%{_mandir}/man3

ln -sf libnet.so	$RPM_BUILD_ROOT%{_libdir}/libpwrite.so
ln -sf libnet.a		$RPM_BUILD_ROOT%{_libdir}/libpwrite.a
install sample/*.[ch]	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README doc/{CHANGELOG,MIGRATION,SUPPORTED_PROTOCOLS,PACKET_BUILDING}
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h
%{_includedir}/libnet
%{_mandir}/man*/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
