%global tl_name betababel
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5
Release:	%{tl_revision}.1
Summary:	Insert ancient greek text coded in Beta Code
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/betababel
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/betababel.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/betababel.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The betababel package extends the babel polutonikogreek option to
provide a simple way to insert ancient Greek texts with diacritical
characters into your document using the commonly used Beta Code
transliteration. You can directly insert Beta Code texts -- as they can
be found at the Perseus project, for example -- without modification.

