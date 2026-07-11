%global tl_name blacklettert1
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	T1-encoded versions of Haralambous old German fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/gothic/blacklettert1
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/blacklettert1.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/blacklettert1.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/blacklettert1.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package contains virtual fonts that offer T1-alike encoded variants
of Yannis Haralambous's old German fonts Gothic, Schwabacher and Fraktur
(which are also available in Adobe type 1 format). The package includes
LaTeX macros to embed the fonts into the LaTeX font selection scheme.

