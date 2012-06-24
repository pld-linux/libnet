Summary:	C library for portable packet creation and injection
Summary(pl):	Biblioteka C do przeno�nego tworzenia i wprowadzania pakiet�w
Summary(pt_BR):	API para fun��es de rede de baixo n�vel
Name:		libnet
Version:	1.1.2.1
Release:	2
Epoch:		1
License:	BSD
Group:		Libraries
Source0:	http://www.packetfactory.net/libnet/dist/%{name}-%{version}.tar.gz
# Source0-md5:	be845c41170d72c7db524f3411b50256
Patch0:		%{name}-shared.patch
Patch1:		%{name}-am.patch
URL:		http://www.packetfactory.net/libnet/
BuildRequires:	autoconf
BuildRequires:	automake
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
Biblioteka dostarcza API dla popularnych niskopoziomowych funkcji
sieciowych (g��wnie wprowadzania pakiet�w). Przy u�yciu libnet mo�na
�atwo stworzy� dowolne pakiety sieciowe. Biblioteka dostarcza
przeno�ny szkielet do niskopoziomowego zapisu i obs�ugi pakiet�w
sieciowych (w po��czeniu z libpcap mo�na napisa� co� naprawd�
fajnego). Libnet obejmuje tworzenie pakiet�w w warstwie IP i
po��czenia, a tak�e funkcjonalno�� dodatkow� i uzupe�niaj�c�.

%description -l pt_BR
Este pacote fornece uma API simples para fun��es de rede de baixo
n�vel comumente usadas (principalmente inje��o de pacotes). Usando
libnet, � simples construir e enviar pacotes de rede arbitr�rios.

%package devel
Summary:	Header files and develpment documentation for libnet
Summary(pl):	Pliki nag��wkowe i dokumetacja do libnet
Summary(pt_BR):	Arquivos do pacote libnet para desenvolvimento
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files and develpment documentation for libnet.

%description devel -l pl
Pliki nag��wkowe i dokumentacja do libnet.

%description devel -l pt_BR
Arquivos de cabe�alho e bibliotecas usadas no desenvolvimento de
aplicativos que usam libnet.

%package static
Summary:	Static libnet library
Summary(pl):	Biblioteka statyczna libnet
Summary(pt_BR):	Arquivos do pacote libnet para desenvolvimento est�tico
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static libnet library.

%description static -l pl
Biblioteka statyczna libnet.

%description static -l pt_BR
Arquivos de cabe�alho e bibliotecas usadas no desenvolvimento de
aplicativos est�ticos que usam libnet.

%package examples
Summary:	libnet - example programs
Summary(pl):	libnet - programy przyk�adowe
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description examples
libnet - example programs.

%description examples -l pl
libnet - programy przyk�adowe.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-pf_packet=yes
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{_mandir}/man3}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf libnet.so	$RPM_BUILD_ROOT%{_libdir}/libpwrite.so
ln -sf libnet.a		$RPM_BUILD_ROOT%{_libdir}/libpwrite.a
install sample/*.[ch]	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install doc/man/man3/libnet-functions.h.3 $RPM_BUILD_ROOT/%{_mandir}/man3

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README doc/{CHANGELOG,MIGRATION,PACKET_BUILDING}
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
