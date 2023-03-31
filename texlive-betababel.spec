Name:		texlive-betababel
Version:	15878
Release:	2
Summary:	Insert ancient greek text coded in Beta Code
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/betababel
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/betababel.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/betababel.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
