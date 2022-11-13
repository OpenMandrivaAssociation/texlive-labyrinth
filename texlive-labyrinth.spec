Name:		texlive-labyrinth
Version:	33454
Release:	1
Summary:	Draw labyrinths and solution paths
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/labyrinth
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/labyrinth.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/labyrinth.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The labyrinth package provides code and an environment for
typesetting simple labyrinths with LaTeX, and generating an
automatic or manual solution path.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/labyrinth/labyrinth.sty
%doc %{_texmfdistdir}/doc/latex/labyrinth/README
%doc %{_texmfdistdir}/doc/latex/labyrinth/classic-en.ist
%doc %{_texmfdistdir}/doc/latex/labyrinth/labyrinth.pdf
%doc %{_texmfdistdir}/doc/latex/labyrinth/labyrinth.tex
%doc %{_texmfdistdir}/doc/latex/labyrinth/lstlocal.cfg

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
