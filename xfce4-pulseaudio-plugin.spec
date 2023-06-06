%define url_ver	%(echo %{version} | cut -d. -f1,2)
%define _disable_rebuild_configure 1

Summary:	A panel plugin for controlling PulseAudio mixer
Name:		xfce4-pulseaudio-plugin
Version:	0.4.7
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://goodies.xfce.org/projects/panel-plugins/xfce4-pulseaudio-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	xfce4-dev-tools >= 4.12
BuildRequires:	intltool
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(exo-2)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libpulse-mainloop-glib)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libxfce4util-1.0)
BuildRequires:	pkgconfig(libxfce4ui-2)
BuildRequires:	pkgconfig(libxfce4panel-2.0)
BuildRequires:	pkgconfig(libxfconf-0)
BuildRequires:	pkgconfig(keybinder)
Requires:	xfce4-panel >= 4.11.0
Requires:	pavucontrol
# Replaces xfce4-mixer
Obsoletes:	xfce4-mixer < 4.11.0-5


%description
Xfce4-pulseaudio-plugin is a panel plugin for controlling an audio
output volume of the PulseAudio mixer.

%prep
%setup -q
%autopatch -p1

%build
%define _disable_ld_no_undefined 1

%configure
%make_build

%install
%make_install

# we don't want these
find %{buildroot} -name "*.la" -delete

%find_lang %{name}

%files -f %{name}.lang
%doc NEWS README*
%{_libdir}/xfce4/panel/plugins/libpulseaudio-plugin.so
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_iconsdir}/hicolor/*/status/*.svg
%{_datadir}/xfce4/panel/plugins/pulseaudio.desktop
