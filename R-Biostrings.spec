%bcond_with bootstrap
%global packname  Biostrings
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          2.22.0
Release:          2
Summary:          String objects representing biological sequences, and matching algorithms
Group:            Sciences/Mathematics
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-methods R-IRanges R-graphics R-methods R-stats R-utils
Requires:         R-RUnit
%if %{with bootstrap}
Requires:         R-BSgenome R-BSgenome.Celegans.UCSC.ce2
Requires:         R-BSgenome.Dmelanogaster.UCSC.dm3 R-drosophila2probe
Requires:         R-hgu95av2probe R-hgu133aprobe R-GenomicFeatures
Requires:         R-hgu95av2cdf R-affy R-affydata
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods
BuildRequires:    R-IRanges R-graphics R-methods R-stats R-utils R-IRanges
BuildRequires:    R-RUnit 
%if %{without bootstrap}
BuildRequires:    R-BSgenome R-BSgenome.Celegans.UCSC.ce2
BuildRequires:    R-BSgenome.Dmelanogaster.UCSC.dm3 R-drosophila2probe
BuildRequires:    R-hgu95av2probe R-hgu133aprobe R-GenomicFeatures
BuildRequires:    R-hgu95av2cdf R-affy R-affydata
%endif

%description
Memory efficient string containers, string matching algorithms, and other
utilities, for fast manipulation of large biological sequences or sets of

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/UnitTests
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/libs
