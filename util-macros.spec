#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xCFDF148828C642A7 (alanc@freedesktop.org)
#
Name     : util-macros
Version  : 1.19.2
Release  : 19
URL      : https://xorg.freedesktop.org/releases/individual/util/util-macros-1.19.2.tar.gz
Source0  : https://xorg.freedesktop.org/releases/individual/util/util-macros-1.19.2.tar.gz
Source1  : https://xorg.freedesktop.org/releases/individual/util/util-macros-1.19.2.tar.gz.sig
Summary  : A set of autoconf project macros for X.Org modules
Group    : Development/Tools
License  : MIT
Requires: util-macros-data = %{version}-%{release}
Requires: util-macros-license = %{version}-%{release}
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
Requires: util-macros-data = %{version}-%{release}
Provides: util-macros-devel = %{version}-%{release}
Requires: util-macros = %{version}-%{release}

%description dev
dev components for the util-macros package.


%package dev32
Summary: dev32 components for the util-macros package.
Group: Default
Requires: util-macros-data = %{version}-%{release}
Requires: util-macros-dev = %{version}-%{release}

%description dev32
dev32 components for the util-macros package.


%package license
Summary: license components for the util-macros package.
Group: Default

%description license
license components for the util-macros package.


%prep
%setup -q -n util-macros-1.19.2
cd %{_builddir}/util-macros-1.19.2
pushd ..
cp -a util-macros-1.19.2 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604441953
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../build32;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1604441953
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/util-macros
cp %{_builddir}/util-macros-1.19.2/COPYING %{buildroot}/usr/share/package-licenses/util-macros/f35b1294fe252bc8ec243713fe9e214bbe5c6069
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
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
/usr/lib32/pkgconfig/xorg-macros.pc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/util-macros/f35b1294fe252bc8ec243713fe9e214bbe5c6069
