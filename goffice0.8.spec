%define origname goffice

%define api 0.8
%define major 8
%define libname %mklibname %{origname} %{api}_%{major}
%define develname %mklibname -d %{origname} %{api}

Summary:	Set of document centric objects and utilities for glib/gtk
Name:		%{origname}%{api}
Version:	0.8.17
Release:	1
License:	GPLv2
Group:		System/Libraries
Url:		http://www.gnome.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/goffice/%{origname}-%{version}.tar.xz
Patch0:		goffice-0.8.17-no-pcre.patch
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
BuildRequires:	gtk-doc
BuildRequires:	intltool
Conflicts:	goffice < 0.9

%description
There are common operations for document centric applications that are
conceptually simple, but complex to implement fully.
    - plugins
    - load/save documents
    - undo/redo

%package -n %{libname}
Summary:	Set of document centric objects and utilities for glib/gtk
Group:		System/Libraries
Requires:	%{name} >= %{version}

%description -n %{libname}
Shared library implementing document centric objects and utilities for glib/gtk

%package -n %{develname}
Summary:	Set of document centric objects and utilities for glib/gtk
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n %{develname}
Development files of the Goffice library.

%prep
%setup -qn %{origname}-%{version}
%patch0 -p1

%build
autoreconf -fi
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%find_lang %{origname}-%{version}

%files -f %{origname}-%{version}.lang
%doc README NEWS AUTHORS BUGS MAINTAINERS
%{_datadir}/%{origname}/%{version}
%{_datadir}/pixmaps/%{origname}/%{version}

%files -n %{libname}
%{_libdir}/libgoffice-%{api}.so.%{major}*
%{_libdir}/%{origname}/%{version}

%files -n %{develname}
%{_includedir}/libgoffice-%{api}
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gtk-doc/html/goffice-%{api}


