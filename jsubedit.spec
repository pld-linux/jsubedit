Summary:	SubEdit - subtitles editor
Summary(pl):	SubEdit - edytor napisów
Name:		jsubedit
Version:	0.1
Release:	0.9
License:	GPL v2 ?
Group:		X11/Window Managers/Tools
Source0:	http://alfa.imi.pcz.czest.pl/~subedit/polish/download/%{name}%{version}src.tar.gz
#Source1:	%{name}.desktop
URL:		http://alfa.imi.pcz.czest.pl/~subedit/
Vendor:		Artur Sikora <subedit@alfa.imi.pcz.czest.pl>
Patch0:		%{name}-makefile.patch
BuildRequires:	qt-devel >= 3.0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6

%description
"just SubEdit" is the Linux port of SubEdit-Player program. It's meant
only for subtitles edition.

%description -l pl
"just SubEdit" jest linuxow± wersj± programu SubEdit-Player. S³u¿y on
wy³±cznie do edycji napisów.

%prep
%setup -q -n %{name}%{version}src
%patch0 -p1

%build
%{__make} CXXFLAGS="-I%{_includedir}/qt" LDFLAGS="-L%{_libdir}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_DIR=%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHYTAJTO.TXT
%attr(755,root,root) %{_bindir}/*
