%define pkgname utils

Summary: X.Org X11 X client utilities
Name: xorg-x11-%{pkgname}
Version:	7.5
Release: 3
License: MIT
Group: User Interface/X
URL: http://www.x.org

Source0:  %{name}-%{version}.tar.gz

BuildRequires: pkgconfig(xorg-macros) pkgconfig(glproto)
BuildRequires: pkgconfig(dmx) pkgconfig(gl) pkgconfig(xext) pkgconfig(xft)
BuildRequires: pkgconfig(xi) pkgconfig(xinerama) pkgconfig(xmu)
BuildRequires: pkgconfig(xpm) pkgconfig(xt) pkgconfig(xtst) pkgconfig(xv)
BuildRequires: pkgconfig(xxf86dga) pkgconfig(xxf86misc) pkgconfig(xxf86vm)
BuildRequires: pkgconfig(xcb) pkgconfig(xcb-atom) pkgconfig(xaw7) pkgconfig(fontenc)

Provides: xdpyinfo xev xlsatoms xlsclients xlsfonts xprop xvinfo xwininfo

%description
A collection of client utilities which can be used to query the X server
for various information.

%prep
%setup -q 

%build
rm -rf debian
# Build all apps
{
   for app in * ; do
      pushd $app
      if [ -e ./configure ] ; then
	%configure
        make
      fi
      popd
   done
}

%install
# Install all apps
{
   for app in * ; do
      pushd $app
      if [ -e Makefile ]; then
      	make install DESTDIR=$RPM_BUILD_ROOT
      fi
      popd
   done
}

%docs_package

%files
%{_bindir}/xdpyinfo
%{_bindir}/xev
%{_bindir}/xlsatoms
%{_bindir}/xlsclients
%{_bindir}/xlsfonts
%{_bindir}/xprop
%{_bindir}/xvinfo
%{_bindir}/xwininfo
/usr/bin/xmessage
/etc/X11/app-defaults/Editres
/etc/X11/app-defaults/Editres-color
/etc/X11/app-defaults/Viewres
/etc/X11/app-defaults/Viewres-color
/etc/X11/app-defaults/XFontSel
/etc/X11/app-defaults/Xfd
/etc/X11/app-defaults/Xmessage
/etc/X11/app-defaults/Xmessage-color
/usr/bin/appres
/usr/bin/editres
/usr/bin/listres
/usr/bin/luit
/usr/bin/viewres
/usr/bin/xdriinfo
/usr/bin/xfd
/usr/bin/xfontsel
/usr/bin/xkill
