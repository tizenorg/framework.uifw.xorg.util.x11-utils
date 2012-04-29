Summary: X11 utilities
Name: xorg-x11-utils
Version: 7.5
Release: 6
License: MIT/X11
Group: User Interface/X
URL: http://www.x.org
Source: %{name}-%{version}.tar.gz

BuildRequires: pkgconfig(xorg-macros)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xaw7)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xft)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xmuu)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(xt)
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(xxf86dga)
BuildRequires: pkgconfig(xxf86vm)
BuildRequires: pkgconfig(xv)
BuildRequires: pkgconfig(xmu)
BuildRequires: pkgconfig(inputproto)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(fontenc)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-atom)
BuildRequires: pkgconfig(xcb-shape)

%define DEF_SUBDIRS appres editres listres luit viewres xdpyinfo xev xfd xfontsel xkill xlsatoms xlsclients xlsfonts xmessage xprop xvinfo xwininfo

Provides: %{DEF_SUBDIRS}

%description
A collection of common X Window System applications.

%prep
%setup -q

%build
# Build all apps
{
    for app in %{DEF_SUBDIRS}; do
        pushd $app
        %configure \
            --disable-xprint \
            RSH=rsh \
            MANCONF="/etc/manpath.config"
        popd
    done
}

%install
rm -rf $RPM_BUILD_ROOT
# Install all apps
{
   for app in %{DEF_SUBDIRS} ; do
      pushd $app
      make install DESTDIR=$RPM_BUILD_ROOT
      popd
   done
}

%remove_docs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/*
/etc/X11/app-defaults/*
