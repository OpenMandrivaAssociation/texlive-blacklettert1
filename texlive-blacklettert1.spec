# revision 15878
# category Package
# catalog-ctan /fonts/gothic/blacklettert1
# catalog-date 2008-04-19 22:58:44 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-blacklettert1
Version:	20080419
Release:	4
Summary:	T1-encoded versions of Haralambous old German fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/gothic/blacklettert1
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/blacklettert1.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/blacklettert1.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/blacklettert1.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides virtual fonts for T1-like variants of
Yannis Haralambous's old German fonts Gothic, Schwabacher and
Fraktur (which are also available in Adobe type 1 format). The
package includes LaTeX macros to embed the fonts into the LaTeX
font selection scheme.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/tfm/public/blacklettert1/tfrak.tfm
%{_texmfdistdir}/fonts/tfm/public/blacklettert1/tfrakls.tfm
%{_texmfdistdir}/fonts/tfm/public/blacklettert1/tgoth.tfm
%{_texmfdistdir}/fonts/tfm/public/blacklettert1/tswab.tfm
%{_texmfdistdir}/fonts/vf/public/blacklettert1/tfrak.vf
%{_texmfdistdir}/fonts/vf/public/blacklettert1/tfrakls.vf
%{_texmfdistdir}/fonts/vf/public/blacklettert1/tgoth.vf
%{_texmfdistdir}/fonts/vf/public/blacklettert1/tswab.vf
%{_texmfdistdir}/tex/latex/blacklettert1/t1yfrak.fd
%doc %{_texmfdistdir}/doc/fonts/blacklettert1/COPYING
%doc %{_texmfdistdir}/doc/fonts/blacklettert1/INSTALL
%doc %{_texmfdistdir}/doc/fonts/blacklettert1/README
%doc %{_texmfdistdir}/doc/fonts/blacklettert1/blacklettert1.pdf
#- source
%doc %{_texmfdistdir}/source/fonts/blacklettert1/Makefile
%doc %{_texmfdistdir}/source/fonts/blacklettert1/blacklettert1.dtx
%doc %{_texmfdistdir}/source/fonts/blacklettert1/blacklettert1.ins
%doc %{_texmfdistdir}/source/fonts/blacklettert1/cmbsy10.pl
%doc %{_texmfdistdir}/source/fonts/blacklettert1/cmbx10.pl
%doc %{_texmfdistdir}/source/fonts/blacklettert1/cmmi10.pl
%doc %{_texmfdistdir}/source/fonts/blacklettert1/cmmib10.pl
%doc %{_texmfdistdir}/source/fonts/blacklettert1/cmr10.pl
%doc %{_texmfdistdir}/source/fonts/blacklettert1/cmr7.pl
%doc %{_texmfdistdir}/source/fonts/blacklettert1/cmsy10.pl
%doc %{_texmfdistdir}/source/fonts/blacklettert1/cmu10.pl
%doc %{_texmfdistdir}/source/fonts/blacklettert1/ecbx1000.pl
%doc %{_texmfdistdir}/source/fonts/blacklettert1/ecrm0700.pl
%doc %{_texmfdistdir}/source/fonts/blacklettert1/ecrm1000.pl
%doc %{_texmfdistdir}/source/fonts/blacklettert1/yfrak.pl
%doc %{_texmfdistdir}/source/fonts/blacklettert1/ygoth.pl
%doc %{_texmfdistdir}/source/fonts/blacklettert1/yswab.pl

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20080419-2
+ Revision: 749766
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20080419-1
+ Revision: 717951
- texlive-blacklettert1
- texlive-blacklettert1
- texlive-blacklettert1
- texlive-blacklettert1
- texlive-blacklettert1

