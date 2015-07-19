%define major	1
%define libname %mklibname xdamage %{major}
%define devname %mklibname xdamage -d

Summary: 	X Damage  Library
Name:		libxdamage
Version:	1.1.4
Release:	13
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXdamage-%{version}.tar.bz2

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)

%description
X Damage  Library.

%package -n %{libname}
Summary:	X Damage Library
Group:		Development/X11
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
X Damage  Library.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development files for %{name}

%prep
%setup -qn libXdamage-%{version}

%build
autoreconf -fi
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%pre -n %{devname}
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{libname}
%{_libdir}/libXdamage.so.%{major}*

%files -n %{devname}
%{_libdir}/libXdamage.so
%{_libdir}/pkgconfig/xdamage.pc
%{_includedir}/X11/extensions/Xdamage.h

