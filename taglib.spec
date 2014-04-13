Summary:	A tag library for reading and editing audio meta data
Name:		taglib
Version:	1.9.1
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	http://taglib.github.io/releases/%{name}-%{version}.tar.gz
# Source0-md5:	0d35df96822bbd564c5504cb3c2e4d86
URL:		http://developer.kde.org/~wheeler/taglib.html
BuildRequires:	cmake
BuildRequires:	libstdc++-devel
BuildRequires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A tag library needed for juk application which is part of
kdemultimedia package.

%package devel
Summary:	libtag - header files
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for tag library.

%prep
%setup -q

%build
mkdir build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

cd build
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libtag.so.?
%attr(755,root,root) %ghost %{_libdir}/libtag_c.so.?
%attr(755,root,root) %{_libdir}/libtag.so.*.*.*
%attr(755,root,root) %{_libdir}/libtag_c.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/taglib-config
%attr(755,root,root) %{_libdir}/libtag.so
%attr(755,root,root) %{_libdir}/libtag_c.so
%{_pkgconfigdir}/taglib*.pc
%{_includedir}/taglib

