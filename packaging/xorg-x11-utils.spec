%define pkgname utils

Summary: X.Org X11 X client utilities
Name: xorg-x11-utils
Version: 7.5.1
Release: 6
License: MIT
Group: User Interface/X
URL: http://www.x.org
Source: %{name}-%{version}.tar.gz

BuildRequires: pkgconfig(dmx) pkgconfig(xext) pkgconfig(xft) pkgconfig(xrandr)
#BuildRequires: pkgconfig(dmx) pkgconfig(gl) pkgconfig(xext) pkgconfig(xft)
BuildRequires: pkgconfig(xi) pkgconfig(xinerama) pkgconfig(xmu)
BuildRequires: pkgconfig(xt) pkgconfig(xtst) pkgconfig(xv)
BuildRequires: pkgconfig(xxf86dga) pkgconfig(xxf86vm)
BuildRequires: pkgconfig(xcb) pkgconfig(xcb-atom)

%define DEF_SUBDIRS xdpyinfo xev xprop xvinfo xwininfo

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
        %reconfigure \
            --disable-xprint \
            RSH=rsh \
            MANCONF="/etc/manpath.config"
        popd
    done
}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/share/license
cp -af COPYING %{buildroot}/usr/share/license/%{name}
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
%manifest xorg-x11-utils.manifest
%defattr(-,root,root,-)
/usr/share/license/%{name}
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
