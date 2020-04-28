#
# Conditional build:
%bcond_without	apidocs	# Doxygen documentation in HTML format

Summary:	C library for portable packet creation and injection
Summary(pl.UTF-8):	Biblioteka C do przenośnego tworzenia i wprowadzania pakietów
Summary(pt_BR.UTF-8):	API para funções de rede de baixo nível
Name:		libnet
Version:	1.2
Release:	1
Epoch:		1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/libnet/libnet/releases
Source0:	https://github.com/libnet/libnet/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a36c669e0cdfda6a2aa3adfb1f6fe60a
Patch0:		%{name}-libdir.patch
Patch1:		%{name}-proc.patch
URL:		https://github.com/libnet/libnet
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.14
%{?with_apidocs:BuildRequires:	doxygen}
BuildRequires:	libtool >= 2:2.4.2
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
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumetacja do libnet
Summary(pt_BR.UTF-8):	Arquivos do pacote libnet para desenvolvimento
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
Summary(pl.UTF-8):	Biblioteka statyczna libnet
Summary(pt_BR.UTF-8):	Arquivos do pacote libnet para desenvolvimento estático
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static libnet library.

%description static -l pl.UTF-8
Biblioteka statyczna libnet.

%description static -l pt_BR.UTF-8
Arquivos de cabeçalho e bibliotecas usadas no desenvolvimento de
aplicativos estáticos que usam libnet.

%package apidocs
Summary:	API documentation for libnet
Summary(pl.UTF-8):	Dokumentacja API biblioteki libnet
Group:		Documentation
%if "%{_rpmversion}" >= "4.6"
BuildArch:	noarch
%endif

%description apidocs
API documentation for libnet.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libnet.

%package examples
Summary:	libnet - example programs
Summary(pl.UTF-8):	libnet - programy przykładowe
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
%if "%{_rpmversion}" >= "4.6"
BuildArch:	noarch
%endif

%description examples
libnet - example programs.

%description examples -l pl.UTF-8
libnet - programy przykładowe.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_apidocs:--disable-doxygen-html} \
	--with-link-layer=linux

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/%{_lib},%{_mandir}/man1,%{_examplesdir}/%{name}-%{version}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p sample/*.[ch] $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__mv} $RPM_BUILD_ROOT%{_libdir}/libnet.so.* $RPM_BUILD_ROOT/%{_lib}
ln -sf /%{_lib}/$(cd $RPM_BUILD_ROOT/%{_lib} ; echo libnet.so.*.*.*) \
        $RPM_BUILD_ROOT%{_libdir}/libnet.so

# fix man section
%{__mv} $RPM_BUILD_ROOT{%{_mandir}/man3/libnet-config.3,%{_mandir}/man1/libnet-config.1}

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libnet.la

%if %{with apidocs}
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libnet
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog.md LICENSE README.md doc/{MIGRATION,RAWSOCKET}.md
%attr(755,root,root) /%{_lib}/libnet.so.*.*.*
%attr(755,root,root) %ghost /%{_lib}/libnet.so.9

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libnet-config
%attr(755,root,root) %{_libdir}/libnet.so
%{_includedir}/libnet.h
%{_includedir}/libnet
%{_pkgconfigdir}/libnet.pc
%{_mandir}/man1/libnet-config.1*
%{_mandir}/man3/libnet.3*
%{_mandir}/man3/libnet-functions.3*
%{_mandir}/man3/libnet-macros.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libnet.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc doc/html/*.{css,html,js,png}
%endif

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
