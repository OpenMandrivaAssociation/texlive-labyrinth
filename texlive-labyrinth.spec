%global tl_name labyrinth
%global tl_revision 33454

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Draw labyrinths and solution paths
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/labyrinth
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/labyrinth.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/labyrinth.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The labyrinth package provides code and an environment for typesetting
simple labyrinths with LaTeX, and generating an automatic or manual
solution path.

