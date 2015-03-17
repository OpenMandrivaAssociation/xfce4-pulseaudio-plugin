%define url_ver	%(echo %{version} | cut -d. -f1,2)

# exclude plugin .so from provides
%global __provides_exclude_from %{_libdir}/xfce4/panel/plugins/.*\\.so

Summary:	A panel plugin for controlling PulseAudio mixer
Name:		xfce4-pulseaudio-plugin
Version:	0.2.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://goodies.xfce.org/projects/panel-plugins/xfce4-pulseaudio-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	xfce4-dev-tools >= 4.12
BuildRequires:	intltool
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(libpulse-mainloop-glib)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libxfce4util-1.0)
BuildRequires:	pkgconfig(libxfce4ui-2) >= 4.11.0
BuildRequires:	pkgconfig(libxfce4panel-2.0) >= 4.11.0
Requires:	xfce4-panel >= 4.11.0
Requires:	pavucontrol
# Replaces xfce4-mixer
%rename		xfce4-mixer < 4.11.0-3

%description
Xfce4-pulseaudio-plugin is a panel plugin for controlling an audio
output volume of the PulseAudio mixer.

%prep
%setup -q
%apply_patches

%build
%configure
%make

%install
%makeinstall_std

# we don't want these
find %{buildroot} -name "*.la" -delete

%files
%doc NEWS README
%{_libdir}/xfce4/panel/plugins/libpulseaudio-plugin.so
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_datadir}/xfce4/panel/plugins/pulseaudio.desktop
