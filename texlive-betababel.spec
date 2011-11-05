# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/betababel
# catalog-date 2009-03-27 13:15:14 +0100
# catalog-license lppl
# catalog-version 0.5
Name:		texlive-betababel
Version:	0.5
Release:	1
Summary:	Insert ancient greek text coded in Beta Code
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/betababel
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/betababel.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/betababel.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The betababel package extends the babel polutonikogreek option
to provide a simple way to insert ancient Greek texts with
diacritical characters into your document using the commonly
used Beta Code transliteration. You can directly insert Beta
Code texts -- as they can be found at the Perseus project, for
example -- without modification.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/betababel/betababel.sty
%doc %{_texmfdistdir}/doc/latex/betababel/betatest.pdf
%doc %{_texmfdistdir}/doc/latex/betababel/betatest.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
