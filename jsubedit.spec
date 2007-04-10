# Conditional build:
# _with_ra	- build in PLD Ra environment
# TODO
# - home page has only 0.1 version available
# - program only in polish!
Summary:	SubEdit - subtitles editor
Summary(pl.UTF-8):	SubEdit - edytor napisów
Name:		jsubedit
Version:	0.2
Release:	1
License:	GPL v2
Group:		Applications/Editors
Source0:	http://alfa.imi.pcz.czest.pl/~subedit/polish/download/%{name}-%{version}.tar.gz
# Source0-md5:	e4201661bc61c99d7cd172740329334d
URL:		http://subedit.prv.pl/polish/information.html
Vendor:		Artur Sikora <subedit@alfa.imi.pcz.czest.pl>
BuildRequires:	qt-devel >= 3:3.0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%if %{?_with_ra:1}%{!?_with_ra:0}
%define		_prefix		/usr/X11R6
%endif

%description
"just SubEdit" is the Linux port of SubEdit-Player program. It's meant
only for subtitles edition.

%description -l pl.UTF-8
"just SubEdit" jest linuksową wersją programu SubEdit-Player. Służy on
wyłącznie do edycji napisów.

%prep
%setup -q
%{__perl} -pi -e 's/^\s*clear\s*$/#$&/' Makefile

%build
%{__make} \
	CXXFLAGS="-I%{_includedir}/qt" \
	LDFLAGS="-L%{_libdir}" \
	LIBS="-lqt-mt"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_DIR=%{_bindir}

install %{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop
