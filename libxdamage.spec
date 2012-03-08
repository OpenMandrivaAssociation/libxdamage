%define major 1
%define libname %mklibname xdamage %{major}
%define develname %mklibname xdamage -d

Name: libxdamage
Summary:  X Damage  Library
Version: 1.1.3
Release: 4
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXdamage-%{version}.tar.bz2

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxfixes-devel >= 3.0.1.2
BuildRequires: x11-proto-devel >= 1.2.0
BuildRequires: x11-util-macros >= 1.0.1

%description
X Damage  Library.

%package -n %{libname}
Summary: X Damage Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
X Damage  Library.

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libname} = %{version}
Provides: %{name}-devel = %{version}-%{release}
Conflicts: libxorg-x11-devel < 7.0
Obsoletes: %{_lib}xdamage1-devel
Obsoletes: %{_lib}xdamage-static-devel

%description -n %{develname}
Development files for %{name}

%prep
%setup -qn libXdamage-%{version}

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXdamage.so.%{major}*

%files -n %{develname}
%{_libdir}/libXdamage.so
%{_libdir}/pkgconfig/xdamage.pc
%{_includedir}/X11/extensions/Xdamage.h

