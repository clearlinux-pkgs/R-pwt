#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-pwt
Version  : 7.1.1
Release  : 20
URL      : https://cran.r-project.org/src/contrib/pwt_7.1-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/pwt_7.1-1.tar.gz
Summary  : Penn World Table (Versions 5.6, 6.x, 7.x)
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : buildreq-R

%description
national income accounts converted to international prices for
	189 countries for some or all of the years 1950-2010.

%prep
%setup -q -c -n pwt
cd %{_builddir}/pwt

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589537701

%install
export SOURCE_DATE_EPOCH=1589537701
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pwt
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pwt
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pwt
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc pwt || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/pwt/CITATION
/usr/lib64/R/library/pwt/DESCRIPTION
/usr/lib64/R/library/pwt/INDEX
/usr/lib64/R/library/pwt/Meta/Rd.rds
/usr/lib64/R/library/pwt/Meta/data.rds
/usr/lib64/R/library/pwt/Meta/features.rds
/usr/lib64/R/library/pwt/Meta/hsearch.rds
/usr/lib64/R/library/pwt/Meta/links.rds
/usr/lib64/R/library/pwt/Meta/nsInfo.rds
/usr/lib64/R/library/pwt/Meta/package.rds
/usr/lib64/R/library/pwt/NAMESPACE
/usr/lib64/R/library/pwt/NEWS
/usr/lib64/R/library/pwt/R/pwt
/usr/lib64/R/library/pwt/R/pwt.rdb
/usr/lib64/R/library/pwt/R/pwt.rdx
/usr/lib64/R/library/pwt/data/Rdata.rdb
/usr/lib64/R/library/pwt/data/Rdata.rds
/usr/lib64/R/library/pwt/data/Rdata.rdx
/usr/lib64/R/library/pwt/data/datalist
/usr/lib64/R/library/pwt/help/AnIndex
/usr/lib64/R/library/pwt/help/aliases.rds
/usr/lib64/R/library/pwt/help/paths.rds
/usr/lib64/R/library/pwt/help/pwt.rdb
/usr/lib64/R/library/pwt/help/pwt.rdx
/usr/lib64/R/library/pwt/html/00Index.html
/usr/lib64/R/library/pwt/html/R.css
