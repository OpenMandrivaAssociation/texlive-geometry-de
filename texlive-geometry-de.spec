# revision 21882
# category Package
# catalog-ctan /macros/latex/contrib/geometry-de
# catalog-date 2011-03-29 21:39:15 +0200
# catalog-license lppl1.3
# catalog-version 1.1
Name:		texlive-geometry-de
Version:	1.1
Release:	1
Summary:	German translation of the geometry package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/geometry-de
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/geometry-de.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/geometry-de.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
German translation of the geometry package, by Hans-Martin
Haase of the University of Jena.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/geometry-de/README
%doc %{_texmfdistdir}/doc/latex/geometry-de/README-DE
%doc %{_texmfdistdir}/doc/latex/geometry-de/geometry-de.dtx
%doc %{_texmfdistdir}/doc/latex/geometry-de/geometry-de.pdf
%doc %{_texmfdistdir}/doc/latex/geometry-de/geometry.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
