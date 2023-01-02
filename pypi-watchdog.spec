#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-watchdog
Version  : 2.2.1
Release  : 19
URL      : https://files.pythonhosted.org/packages/11/6f/0396d373e039b89c60e23a1a9025edc6dd203121fe0af7d1427e85d5ec98/watchdog-2.2.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/11/6f/0396d373e039b89c60e23a1a9025edc6dd203121fe0af7d1427e85d5ec98/watchdog-2.2.1.tar.gz
Summary  : Filesystem events monitoring
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-watchdog-bin = %{version}-%{release}
Requires: pypi-watchdog-license = %{version}-%{release}
Requires: pypi-watchdog-python = %{version}-%{release}
Requires: pypi-watchdog-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Watchdog
========
|Build Status|
|CirrusCI Status|
Python API and shell utilities to monitor file system events.

%package bin
Summary: bin components for the pypi-watchdog package.
Group: Binaries
Requires: pypi-watchdog-license = %{version}-%{release}

%description bin
bin components for the pypi-watchdog package.


%package license
Summary: license components for the pypi-watchdog package.
Group: Default

%description license
license components for the pypi-watchdog package.


%package python
Summary: python components for the pypi-watchdog package.
Group: Default
Requires: pypi-watchdog-python3 = %{version}-%{release}

%description python
python components for the pypi-watchdog package.


%package python3
Summary: python3 components for the pypi-watchdog package.
Group: Default
Requires: python3-core
Provides: pypi(watchdog)

%description python3
python3 components for the pypi-watchdog package.


%prep
%setup -q -n watchdog-2.2.1
cd %{_builddir}/watchdog-2.2.1
pushd ..
cp -a watchdog-2.2.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672691050
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-watchdog
cp %{_builddir}/watchdog-%{version}/COPYING %{buildroot}/usr/share/package-licenses/pypi-watchdog/aa949e9aeb3398f2f58b1f03baba6c0b2173a476 || :
cp %{_builddir}/watchdog-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-watchdog/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/watchmedo

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-watchdog/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/pypi-watchdog/aa949e9aeb3398f2f58b1f03baba6c0b2173a476

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
