# libxdamage is used by mesa, mesa is used by wine and steam
%ifarch %{x86_64}
%bcond_without compat32
%else
%bcond_with compat32
%endif

%define major	1
%define libname %mklibname xdamage %{major}
%define devname %mklibname xdamage -d
%define lib32name libxdamage%{major}
%define dev32name libxdamage-devel

%global optflags %{optflags} -O3

Summary: 	X Damage  Library
Name:		libxdamage
Version:	1.1.6
Release:	1
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXdamage-%{version}.tar.xz

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)
%if %{with compat32}
BuildRequires:	libc6
BuildRequires:	devel(libX11)
BuildRequires:	devel(libXfixes)
BuildRequires:	devel(libxcb)
BuildRequires:	devel(libXau)
BuildRequires:	devel(libXdmcp)
%endif

%description
X Damage  Library.

%package -n %{libname}
Summary:	X Damage Library
Group:		Development/X11

%description -n %{libname}
X Damage  Library.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
Development files for %{name}

%if %{with compat32}
%package -n %{lib32name}
Summary:	X Damage Library (32-bit)
Group:		Development/X11

%description -n %{lib32name}
X Damage Library.

%package -n %{dev32name}
Summary:	Development files for %{name} (32-bit)
Group:		Development/X11
Requires:	%{devname} = %{version}-%{release}
Requires:	%{lib32name} = %{version}-%{release}

%description -n %{dev32name}
Development files for %{name}
%endif

%prep
%autosetup -n libXdamage-%{version}
export CONFIGURE_TOP="$(pwd)"
autoreconf -fi
%if %{with compat32}
mkdir build32
cd build32
%configure32
cd ..
%endif
mkdir build
cd build
%configure

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build

%files -n %{libname}
%{_libdir}/libXdamage.so.%{major}*

%files -n %{devname}
%{_libdir}/libXdamage.so
%{_libdir}/pkgconfig/xdamage.pc
%{_includedir}/X11/extensions/Xdamage.h

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libXdamage.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/libXdamage.so
%{_prefix}/lib/pkgconfig/xdamage.pc
%endif
