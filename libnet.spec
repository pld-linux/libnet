Summary:	C library for portable packet creation and injection
Summary(pl.UTF-8):   Biblioteka C do przenośnego tworzenia i wprowadzania pakietów
Summary(pt_BR.UTF-8):   API para funções de rede de baixo nível
Name:		libnet
Version:	1.1.2.1
Release:	3
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

%description -l pl.UTF-8
Biblioteka dostarcza API dla popularnych niskopoziomowych funkcji
sieciowych (głównie wprowadzania pakietów). Przy użyciu libnet można
łatwo stworzyć dowolne pakiety sieciowe. Biblioteka dostarcza
przenośny szkielet do niskopoziomowego zapisu i obsługi pakietów
sieciowych (w połączeniu z libpcap można napisać coś naprawdę
fajnego). Libnet obejmuje tworzenie pakietów w warstwie IP i
połączenia, a także funkcjonalność dodatkową i uzupełniającą.

%description -l pt_BR.UTF-8
Este pacote fornece uma API simples para funções de rede de baixo
nível comumente usadas (principalmente injeção de pacotes). Usando
libnet, é simples construir e enviar pacotes de rede arbitrários.

%package devel
Summary:	Header files and develpment documentation for libnet
Summary(pl.UTF-8):   Pliki nagłówkowe i dokumetacja do libnet
Summary(pt_BR.UTF-8):   Arquivos do pacote libnet para desenvolvimento
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files and develpment documentation for libnet.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do libnet.

%description devel -l pt_BR.UTF-8
Arquivos de cabeçalho e bibliotecas usadas no desenvolvimento de
aplicativos que usam libnet.

%package static
Summary:	Static libnet library
Summary(pl.UTF-8):   Biblioteka statyczna libnet
Summary(pt_BR.UTF-8):   Arquivos do pacote libnet para desenvolvimento estático
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static libnet library.

%description static -l pl.UTF-8
Biblioteka statyczna libnet.

%description static -l pt_BR.UTF-8
Arquivos de cabeçalho e bibliotecas usadas no desenvolvimento de
aplicativos estáticos que usam libnet.

%package examples
Summary:	libnet - example programs
Summary(pl.UTF-8):   libnet - programy przykładowe
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description examples
libnet - example programs.

%description examples -l pl.UTF-8
libnet - programy przykładowe.

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
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{_mandir}/man3,%{_bindir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf libnet.so	$RPM_BUILD_ROOT%{_libdir}/libpwrite.so
ln -sf libnet.a		$RPM_BUILD_ROOT%{_libdir}/libpwrite.a
install sample/*.[ch]	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install doc/man/man3/libnet-functions.h.3 $RPM_BUILD_ROOT%{_mandir}/man3
install libnet-config	$RPM_BUILD_ROOT%{_bindir}

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
%attr(755,root,root) %{_bindir}/libnet-config
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
