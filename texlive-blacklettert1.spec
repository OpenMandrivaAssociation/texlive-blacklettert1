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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package contains virtual fonts that offer T1-alike encoded variants
of Yannis Haralambous's old German fonts Gothic, Schwabacher and Fraktur
(which are also available in Adobe type 1 format). The package includes
LaTeX macros to embed the fonts into the LaTeX font selection scheme.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/fonts/vf
%dir %{_datadir}/texmf-dist/source/fonts
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/fonts/blacklettert1
%dir %{_datadir}/texmf-dist/fonts/tfm/public
%dir %{_datadir}/texmf-dist/fonts/vf/public
%dir %{_datadir}/texmf-dist/source/fonts/blacklettert1
%dir %{_datadir}/texmf-dist/tex/latex/blacklettert1
%dir %{_datadir}/texmf-dist/fonts/tfm/public/blacklettert1
%dir %{_datadir}/texmf-dist/fonts/vf/public/blacklettert1
%doc %{_datadir}/texmf-dist/doc/fonts/blacklettert1/COPYING
%doc %{_datadir}/texmf-dist/doc/fonts/blacklettert1/INSTALL
%doc %{_datadir}/texmf-dist/doc/fonts/blacklettert1/README
%doc %{_datadir}/texmf-dist/doc/fonts/blacklettert1/blacklettert1.pdf
%{_datadir}/texmf-dist/fonts/tfm/public/blacklettert1/tfrak.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/blacklettert1/tfrakls.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/blacklettert1/tgoth.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/blacklettert1/tswab.tfm
%{_datadir}/texmf-dist/fonts/vf/public/blacklettert1/tfrak.vf
%{_datadir}/texmf-dist/fonts/vf/public/blacklettert1/tfrakls.vf
%{_datadir}/texmf-dist/fonts/vf/public/blacklettert1/tgoth.vf
%{_datadir}/texmf-dist/fonts/vf/public/blacklettert1/tswab.vf
%doc %{_datadir}/texmf-dist/source/fonts/blacklettert1/Makefile
%doc %{_datadir}/texmf-dist/source/fonts/blacklettert1/blacklettert1.dtx
%doc %{_datadir}/texmf-dist/source/fonts/blacklettert1/blacklettert1.ins
%doc %{_datadir}/texmf-dist/source/fonts/blacklettert1/cmbsy10.pl
%doc %{_datadir}/texmf-dist/source/fonts/blacklettert1/cmbx10.pl
%doc %{_datadir}/texmf-dist/source/fonts/blacklettert1/cmmi10.pl
%doc %{_datadir}/texmf-dist/source/fonts/blacklettert1/cmmib10.pl
%doc %{_datadir}/texmf-dist/source/fonts/blacklettert1/cmr10.pl
%doc %{_datadir}/texmf-dist/source/fonts/blacklettert1/cmr7.pl
%doc %{_datadir}/texmf-dist/source/fonts/blacklettert1/cmsy10.pl
%doc %{_datadir}/texmf-dist/source/fonts/blacklettert1/cmu10.pl
%doc %{_datadir}/texmf-dist/source/fonts/blacklettert1/ecbx1000.pl
%doc %{_datadir}/texmf-dist/source/fonts/blacklettert1/ecrm0700.pl
%doc %{_datadir}/texmf-dist/source/fonts/blacklettert1/ecrm1000.pl
%doc %{_datadir}/texmf-dist/source/fonts/blacklettert1/yfrak.pl
%doc %{_datadir}/texmf-dist/source/fonts/blacklettert1/ygoth.pl
%doc %{_datadir}/texmf-dist/source/fonts/blacklettert1/yswab.pl
%{_datadir}/texmf-dist/tex/latex/blacklettert1/t1yfrak.fd
