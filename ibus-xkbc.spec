Summary:	The XKBC engine for IBus input platform
Summary(pl.UTF-8):	Silnik XKBC dla platformy wprowadzania IBus
Name:		ibus-xkbc
Version:	1.3.3.20100922
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://cloud.github.com/downloads/sun-im/ibus-xkbc/%{name}-%{version}.tar.gz
# Source0-md5:	96ad4c25356e07223a862b5067c9422c
Patch0:		%{name}-scripts.patch
URL:		http://github.com/sun-im/ibus-xkbc/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.10
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	rarian-compat
Requires:	ibus >= 1.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/ibus

%description
The XKBC engine for IBus platform. It provides keyboard layout
emulation input method based on XKeyboard Config data.

%description -l pl.UTF-8
Silnik XKBC dla platformy IBus. Udostępmia metodę wprowadzania
znaków polegającą na emulacji układu klawiatury w oparciu o dane
konfiguracyjne XKeyboard Config.

%prep
%setup -q
%patch0 -p1

%build
%{__glib_gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_bindir}/ibus-keyboard
%attr(755,root,root) %{_libexecdir}/ibus-engine-xkbc
%attr(755,root,root) %{_libexecdir}/ibus-setup-xkbc
%{_datadir}/ibus-xkbc
%{_datadir}/ibus/component/xkbc.xml
