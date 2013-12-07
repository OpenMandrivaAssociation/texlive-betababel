# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/betababel
# catalog-date 2009-03-27 13:15:14 +0100
# catalog-license lppl
# catalog-version 0.5
Name:		texlive-betababel
Version:	0.5
Release:	5
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

%description
The betababel package extends the babel polutonikogreek option
to provide a simple way to insert ancient Greek texts with
diacritical characters into your document using the commonly
used Beta Code transliteration. You can directly insert Beta
Code texts -- as they can be found at the Perseus project, for
example -- without modification.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/betababel/betababel.sty
%doc %{_texmfdistdir}/doc/latex/betababel/betatest.pdf
%doc %{_texmfdistdir}/doc/latex/betababel/betatest.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.5-2
+ Revision: 749568
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.5-1
+ Revision: 717909
- texlive-betababel
- texlive-betababel
- texlive-betababel
- texlive-betababel
- texlive-betababel

