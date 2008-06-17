%define major 1
%define libname %mklibname xdamage %{major}
%define develname %mklibname xdamage -d
%define staticdevelname %mklibname xdamage -d -s

Name: libxdamage
Summary:  X Damage  Library
Version: 1.1.1
Release: %mkrel 3
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXdamage-%{version}.tar.bz2

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxfixes-devel >= 3.0.1.2
BuildRequires: x11-proto-devel >= 1.2.0
BuildRequires: x11-util-macros >= 1.0.1

BuildRoot: %{_tmppath}/%{name}-root

%description
X Damage  Library.

#-----------------------------------------------------------

%package -n %{libname}
Summary: X Damage Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
X Damage  Library.

#-----------------------------------------------------------

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libname} = %{version}
Requires: libxfixes-devel >= 3.0.1.2
Requires: x11-proto-devel >= 1.0.0
Provides: %{name}-devel = %{version}-%{release}

Conflicts: libxorg-x11-devel < 7.0
Obsoletes: %mklibname xdamage 1 -d

%description -n %{develname}
Development files for %{name}

%pre -n %{develname}
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/libXdamage.so
%{_libdir}/libXdamage.la
%{_libdir}/pkgconfig/xdamage.pc
%{_includedir}/X11/extensions/Xdamage.h

#-----------------------------------------------------------

%package -n %{staticdevelname}
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{develname} = %{version}
Provides: %{name}-static-devel = %{version}-%{release}

Conflicts: libxorg-x11-static-devel < 7.0
Obsoletes: %mklibname xdamage 1 -d -s

%description -n %{staticdevelname}
Static development files for %{name}.

%files -n %{staticdevelname}
%defattr(-,root,root)
%{_libdir}/libXdamage.a

#-----------------------------------------------------------

%prep
%setup -q -n libXdamage-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libXdamage.so.%{major}*
