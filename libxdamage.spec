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
Provides: %{name} = %{EVRD}

%description -n %{libname}
X Damage  Library.

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libname} = %{version}
Provides: %{name}-devel = %{EVRD}
Conflicts: libxorg-x11-devel < 7.0
Obsoletes: %{_lib}xdamage1-devel < 1.1.3
Obsoletes: %{_lib}xdamage-static-devel < 1.1.3

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

%pre -n %{develname}
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{libname}
%{_libdir}/libXdamage.so.%{major}*

%files -n %{develname}
%{_libdir}/libXdamage.so
%{_libdir}/pkgconfig/xdamage.pc
%{_includedir}/X11/extensions/Xdamage.h



%changelog
* Tue Dec 27 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.1.3-3
+ Revision: 745694
- rebuild
- disabled static build
- removed .la files
- cleaned up spec

* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.3-2
+ Revision: 660298
- mass rebuild

* Wed Jul 21 2010 Thierry Vignaud <tv@mandriva.org> 1.1.3-1mdv2011.0
+ Revision: 556453
- new release

* Mon Nov 09 2009 Thierry Vignaud <tv@mandriva.org> 1.1.2-1mdv2010.1
+ Revision: 463606
- new release

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.1.1-4mdv2010.0
+ Revision: 425883
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.1.1-3mdv2009.0
+ Revision: 223069
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert build requires.

* Mon Jan 14 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1.1-2mdv2008.1
+ Revision: 151701
- Update BuildRequires and rebuild.
  Also remove dependency on chrpath that should have been required to fix
  an problem in an old version.

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Jul 17 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.1-1mdv2008.0
+ Revision: 52788
- new devel library policy
- nuke rpath
- spec file clean
- new version


* Mon Feb 05 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.1-1mdv2007.0
+ Revision: 116431
- new upstream version: 1.1

* Tue Nov 21 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.0.4-1mdv2007.1
+ Revision: 85953
- new release

  + Gustavo Pichorim Boiko <boiko@mandriva.com>
    - rebuild to fix cooker uploading
    - X11R7.1
    - increment release
    - fixed more dependencies
    - Adding X.org 7.0 to the repository

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

