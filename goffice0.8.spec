%define oname	goffice
%define api	0.8
%define major	8
%define libname %mklibname %{oname} %{api} %{major}
%define devname %mklibname -d %{oname} %{api}

Summary:	Set of document centric objects and utilities for glib/gtk
Name:		%{oname}%{api}
Version:	0.8.17
Release:	4
License:	GPLv2
Group:		System/Libraries
Url:		http://www.gnome.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/goffice/%{oname}-%{version}.tar.xz
Patch0:		goffice-0.8.17-pcre8.30.patch

BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	pcre
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig(glib-2.0) >= 2.8.0
BuildRequires:	pkgconfig(gobject-2.0) >= 2.16.0
BuildRequires:	pkgconfig(gmodule-2.0) >= 2.16.0
BuildRequires:	pkgconfig(gio-2.0) >= 2.16.0
BuildRequires:	pkgconfig(libgsf-1) >= 1.14.9
BuildRequires:	pkgconfig(libxml-2.0) >= 2.4.12
BuildRequires:	pkgconfig(pango) >= 1.8.1
BuildRequires:	pkgconfig(pangocairo) >= 1.8.1
BuildRequires:	pkgconfig(cairo) >= 1.2.0
BuildRequires:	pkgconfig(gtk+-2.0) >= 2.12.0
BuildRequires:	pkgconfig(cairo-ps) >= 1.2.0
BuildRequires:	pkgconfig(cairo-pdf) >= 1.2.0
BuildRequires:	pkgconfig(cairo-svg) >= 1.2.0
BuildRequires:	pkgconfig(gconf-2.0)
Conflicts:	goffice < 0.9
Conflicts:	%{_lib}goffice0.8_8 < 0.8.17-2

%description
There are common operations for document centric applications that are
conceptually simple, but complex to implement fully.
    - plugins
    - load/save documents
    - undo/redo

%package -n %{libname}
Summary:	Set of document centric objects and utilities for glib/gtk
Group:		System/Libraries

%description -n %{libname}
Shared library implementing document centric objects and utilities for glib/gtk

%package -n %{devname}
Summary:	Set of document centric objects and utilities for glib/gtk
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development files of the Goffice library.

%prep
%setup -qn %{oname}-%{version}
%apply_patches

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%find_lang %{oname}-%{version}

%files -f %{oname}-%{version}.lang
%doc README NEWS AUTHORS BUGS MAINTAINERS
%{_datadir}/%{oname}/%{version}
%{_datadir}/pixmaps/%{oname}/%{version}
%{_libdir}/%{oname}/%{version}

%files -n %{libname}
%{_libdir}/libgoffice-%{api}.so.%{major}*

%files -n %{devname}
%{_includedir}/libgoffice-%{api}
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gtk-doc/html/goffice-%{api}

