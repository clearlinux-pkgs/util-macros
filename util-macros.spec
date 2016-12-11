#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : util-macros
Version  : 1.19.0
Release  : 11
URL      : http://xorg.freedesktop.org/releases/individual/util/util-macros-1.19.0.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/util/util-macros-1.19.0.tar.gz
Summary  : A set of autoconf project macros for X.Org modules
Group    : Development/Tools
License  : MIT
Requires: util-macros-data
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32

%description
This is a set of autoconf macros used by the configure.ac scripts in
other Xorg modular packages, and is needed to generate new versions
of their configure scripts with autoconf.

%package data
Summary: data components for the util-macros package.
Group: Data

%description data
data components for the util-macros package.


%package dev
Summary: dev components for the util-macros package.
Group: Development
Requires: util-macros-data
Provides: util-macros-devel

%description dev
dev components for the util-macros package.


%package dev32
Summary: dev32 components for the util-macros package.
Group: Default
Requires: util-macros-data

%description dev32
dev32 components for the util-macros package.


%prep
%setup -q -n util-macros-1.19.0
pushd ..
cp -a util-macros-1.19.0 build32
popd

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
%configure --disable-static  --libdir=/usr/lib32
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
pushd ../build32
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do mv $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/util-macros/INSTALL

%files dev
%defattr(-,root,root,-)
/usr/lib64/pkgconfig/xorg-macros.pc
/usr/share/aclocal/*.m4

%files dev32
%defattr(-,root,root,-)
/usr/lib32/pkgconfig/32xorg-macros.pc
