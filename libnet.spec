Summary:	Packet creation and handling library
Summary(pl):	Biblioteka do generacji i obróbki pakietów
Name:		libnet
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Version:	1.0
Release:	1
Source:		http://www.packetfactory.net/libnet/dist/%{name}-%{version}.tgz
Patch:		libnet-autoconf.patch
Copyright:	distributable
URL:		http://www.packetfactory.net/libnet
BuildPreReq:	libpcap-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define 	_prefix		/usr

%description
Libnet is a collection of routines to help with the construction and
sending of network packets at the link layer and the IP layer. 
Use libnet in conjunction with packet capture library (libpcap) 
and you can write some really cool stuff!.

%description -l pl 

Libnet jest bibliotek± na któr± sk³adaj± siê procedury pomagaj±ce
w tworzeniu i wysy³aniu pakietów w sieciowych warstwach: danych oraz IP.
W po³±czeniu z bibliotek± do przechwytywania pakietów (libpcap), libnet
pozwoli Ci na napisanie naprawdê fajnych rzeczy!.

%prep
%setup -q -n Libnet-%{version}
%patch -p0

%build
CFLAGS="$RPM_OPT_FLAGS"; export CFLAGS
autoconf && %configure \
	--with-pf_packet=yes

make
rm -rf doc/{.#CHANGELOG.1.13,CVS,html/CVS}
rm -rf example/{CVS,html/CVS}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/*
gzip -9nf $RPM_BUILD_DIR/Libnet-%{version}/doc/CHANGELOG* \
	$RPM_BUILD_DIR/Libnet-%{version}/doc/README* \
	$RPM_BUILD_DIR/Libnet-%{version}/doc/{COPYING,PORTS,TODO}
rm -f $RPM_BUILD_ROOT%{_libdir}/libpwrite*
ln -sf libnet.a $RPM_BUILD_ROOT%{_libdir}/libpwrite.a
mkdir -p $RPM_BUILD_ROOT%{_prefix}/src/libnet
cp example/* $RPM_BUILD_ROOT%{_prefix}/src/libnet/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man3/*
%{_includedir}/*
%{_libdir}/*
%{_prefix}/src/libnet
%doc doc/*.gz
