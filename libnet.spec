Summary:	"libpwrite" Network Routine Library
Summary(pl):	Biblioteka czynno¶ci sieciowych
Summary(pt_BR):	API para funções de rede de baixo nível
Name:		libnet
Version:	1.0.2a
Release:	5
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

%description -l pt_BR
Este pacote fornece uma API simples para funções de rede de baixo
nível comumente usadas (principalmente injeção de pacotes). Usando
libnet, é simples construir e enviar pacotes de rede arbitrários.

%package devel
Summary:	Header files and develpment documentation for libnet
Summary(pl):	Pliki nag³ówkowe i dokumetacja do libnet
Summary(pt_BR):	Arquivos do pacote libnet para desenvolvimento
Group:		Development/Libraries
Requires:	%{name} = %{version}

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
Requires:	%{name}-devel = %{version}

%description static
Static libnet library.

%description static -l pl
Biblioteka statyczna libnet.

%description static -l pt_BR
Arquivos de cabeçalho e bibliotecas usadas no desenvolvimento de
aplicativos estáticos que usam libnet.

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

ln -sf libnet.so.1.0 $RPM_BUILD_ROOT%{_libdir}/libnet.so
ln -sf libnet.so $RPM_BUILD_ROOT%{_libdir}/libpwrite.so
ln -sf libnet.so $RPM_BUILD_ROOT%{_libdir}/libpwrite.so
ln -sf libnet.a $RPM_BUILD_ROOT%{_libdir}/libpwrite.a

gzip -9nf README doc/CHANGELOG*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libpwrite
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h
%{_includedir}/libnet
%{_mandir}/man*/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
