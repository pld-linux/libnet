Summary:	Packet creation and handling library
Summary(pl):	Biblioteka do generacji i obróbki pakietów
Name:		libnet
Version:	1.0.1a
Release:	1
Copyright:	distributable
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Source0:	http://www.packetfactory.net/libnet/dist/%{name}-%{version}.tgz
Patch0:		libnet-autoconf.patch
URL:		http://www.packetfactory.net/libnet
BuildRequires:	libpcap-devel
Requires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libnet is a collection of routines to help with the construction and
sending of network packets at the link layer and the IP layer. Use
libnet in conjunction with packet capture library (libpcap) and you
can write some really cool stuff!.

%description -l pl 
Libnet jest bibliotek± na któr± sk³adaj± siê procedury pomagaj±ce w
tworzeniu i wysy³aniu pakietów w sieciowych warstwach: danych oraz IP.
W po³±czeniu z bibliotek± do przechwytywania pakietów (libpcap),
libnet pozwoli Ci na napisanie naprawdê fajnych rzeczy!.

%package demo
Summary:	Libnet library - source code of demo programs
Summary(pl):	Biblioteka libnet - ¼ród³a programów demonstracyjnych
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description demo
Libnet library - source code of demo programs

%description demo -l pl
Biblioteka libnet - wersje ¼ród³owe programów demonstracyjnych


%prep
%setup -q -n Libnet-%{version}
%patch -p0

rm -rf doc/{.#CHANGELOG.1.13,CVS,html/CVS}
rm -rf example/{CVS,html/CVS}
rm -rf test/CVS test/*/CVS

%build
autoconf
%configure \
	--with-pf_packet=yes

%{__make} CFLAGS="$RPM_OPT_FLAGS -funroll-loops -fomit-frame-pointer -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/src/examples/libnet/libnet-examples

%{__make} install DESTDIR=$RPM_BUILD_ROOT

ln -sf libnet.a $RPM_BUILD_ROOT%{_libdir}/libpwrite.a
cp -r example/* $RPM_BUILD_ROOT%{_prefix}/src/examples/libnet/libnet-examples
cp -r test/* $RPM_BUILD_ROOT%{_prefix}/src/examples/libnet/

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
	doc/{CHANGELOG*,README*,COPYING,TODO*}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.gz
%attr(755,root,root) %{_bindir}/*

%{_includedir}/*
%{_libdir}/*.a
%{_mandir}/man3/*

%files demo
%defattr(644,root,root,755)
%{_prefix}/src/examples/libnet
