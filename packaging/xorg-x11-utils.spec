%define pkgname utils

Summary: X.Org X11 X client utilities
Name: xorg-x11-utils
Version: 7.5
Release: 6
License: MIT
Group: User Interface/X
URL: http://www.x.org
Source: %{name}-%{version}.tar.gz

BuildRequires: pkgconfig(dmx) pkgconfig(xext) pkgconfig(xft) pkgconfig(xrandr)
#BuildRequires: pkgconfig(dmx) pkgconfig(gl) pkgconfig(xext) pkgconfig(xft)
BuildRequires: pkgconfig(xi) pkgconfig(xinerama) pkgconfig(xmu)
BuildRequires: pkgconfig(xpm) pkgconfig(xt) pkgconfig(xtst) pkgconfig(xv)
BuildRequires: pkgconfig(xxf86dga) pkgconfig(xxf86vm)
BuildRequires: pkgconfig(xcb) pkgconfig(xcb-atom)

%define DEF_SUBDIRS xdpyinfo xev xlsatoms xlsclients xlsfonts xprop xvinfo xwininfo

Provides: %{DEF_SUBDIRS} edid-decode 

%description
A collection of client utilities which can be used to query the X server
for various information.

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
%defattr(-,root,root,-)
#%doc
%{_bindir}/*
#%{_bindir}/edid-decode
#%{_bindir}/xdpyinfo
#%{_bindir}/xev
#%{_bindir}/xlsatoms
#%{_bindir}/xlsclients
#%{_bindir}/xlsfonts
#%{_bindir}/xprop
#%{_bindir}/xvinfo
#%{_bindir}/xwininfo
#%{_mandir}/man1/xdpyinfo.1*
#%{_mandir}/man1/xev.1*
#%{_mandir}/man1/xlsatoms.1*
#%{_mandir}/man1/xlsclients.1*
#%{_mandir}/man1/xlsfonts.1*
#%{_mandir}/man1/xprop.1*
#%{_mandir}/man1/xvinfo.1*
#%{_mandir}/man1/xwininfo.1*
