#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : R-zCompositions
Version  : 1.5.0.4
Release  : 66
URL      : https://cran.r-project.org/src/contrib/zCompositions_1.5.0-4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/zCompositions_1.5.0-4.tar.gz
Summary  : Treatment of Zeros, Left-Censored and Missing Values in
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-NADA
Requires: R-truncnorm
BuildRequires : R-NADA
BuildRequires : R-truncnorm
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
zCompositions
=============
Imputation of Zeros, Nondetects and Missing Data in Compositional Data Sets

%prep
%setup -q -n zCompositions
pushd ..
cp -a zCompositions buildavx2
popd
pushd ..
cp -a zCompositions buildavx512
popd
pushd ..
cp -a zCompositions buildapx
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1740105507

%install
export SOURCE_DATE_EPOCH=1740105507
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -mapxf -mavx10.1-512 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -mapxf -mavx10.1-512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-va/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/zCompositions/CITATION
/usr/lib64/R/library/zCompositions/DESCRIPTION
/usr/lib64/R/library/zCompositions/INDEX
/usr/lib64/R/library/zCompositions/Meta/Rd.rds
/usr/lib64/R/library/zCompositions/Meta/data.rds
/usr/lib64/R/library/zCompositions/Meta/features.rds
/usr/lib64/R/library/zCompositions/Meta/hsearch.rds
/usr/lib64/R/library/zCompositions/Meta/links.rds
/usr/lib64/R/library/zCompositions/Meta/nsInfo.rds
/usr/lib64/R/library/zCompositions/Meta/package.rds
/usr/lib64/R/library/zCompositions/NAMESPACE
/usr/lib64/R/library/zCompositions/NEWS
/usr/lib64/R/library/zCompositions/R/zCompositions
/usr/lib64/R/library/zCompositions/R/zCompositions.rdb
/usr/lib64/R/library/zCompositions/R/zCompositions.rdx
/usr/lib64/R/library/zCompositions/data/LPdata.rda
/usr/lib64/R/library/zCompositions/data/LPdataZM.rda
/usr/lib64/R/library/zCompositions/data/Pigs.rda
/usr/lib64/R/library/zCompositions/data/Water.rda
/usr/lib64/R/library/zCompositions/data/mdl.rda
/usr/lib64/R/library/zCompositions/help/AnIndex
/usr/lib64/R/library/zCompositions/help/aliases.rds
/usr/lib64/R/library/zCompositions/help/paths.rds
/usr/lib64/R/library/zCompositions/help/zCompositions.rdb
/usr/lib64/R/library/zCompositions/help/zCompositions.rdx
/usr/lib64/R/library/zCompositions/html/00Index.html
/usr/lib64/R/library/zCompositions/html/R.css
