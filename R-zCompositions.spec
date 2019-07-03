#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-zCompositions
Version  : 1.3.2.1
Release  : 24
URL      : https://cran.r-project.org/src/contrib/zCompositions_1.3.2-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/zCompositions_1.3.2-1.tar.gz
Summary  : Treatment of Zeros, Left-Censored and Missing Values in
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-NADA
Requires: R-truncnorm
BuildRequires : R-NADA
BuildRequires : R-truncnorm
BuildRequires : buildreq-R

%description
compositional data sets.

%prep
%setup -q -c -n zCompositions

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1562177522

%install
export SOURCE_DATE_EPOCH=1562177522
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library zCompositions
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library zCompositions
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library zCompositions
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc zCompositions || :


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
