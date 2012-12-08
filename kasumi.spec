Summary:	A tool for managing Anthy's dictionary
Name:		kasumi
Version:	2.5
Release:	%mkrel 4
Group:		System/Internationalization
License:	GPLv2+
URL:		http://sourceforge.jp/projects/kasumi
Source0:	http://iij.dl.sourceforge.jp/kasumi/37311/%name-%version.tar.gz
Patch0:		kasumi-2.3-fix-desktop-file.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildrootroot
Requires:	anthy >= 6300
BuildRequires:	pango-devel
BuildRequires:	atk-devel
BuildRequires:	gtk+2-devel
BuildRequires:	anthy-devel
BuildRequires:	imagemagick
BuildRequires:	desktop-file-utils

%description
A tool for managing Anthy's dictionary.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# icons
mkdir -p %{buildroot}/%{_iconsdir}/hicolor/{16x16,32x32}/apps
cp %{buildroot}/%{_datadir}/pixmaps/%{name}.png %{buildroot}/%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert -scale 16 %{buildroot}/%{_datadir}/pixmaps/%{name}.png %{buildroot}/%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%find_lang %{name}

# menu
desktop-file-install	--vendor="" \
			--dir %{buildroot}%{_datadir}/applications \
			--remove-category="Applications" \
			%{name}.desktop

%if %mdkversion < 200900
%post
%update_menus
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_icon_cache hicolor
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_bindir}/*
%{_datadir}/applications/kasumi.desktop
%{_datadir}/pixmaps/*.png
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_mandir}/man1/kasumi.1*


%changelog
* Tue May 10 2011 Funda Wang <fwang@mandriva.org> 2.5-2mdv2011.0
+ Revision: 673246
- rebuild

* Tue Aug 04 2009 Frederik Himpe <fhimpe@mandriva.org> 2.5-1mdv2011.0
+ Revision: 409448
- Update to new version 2.5

* Thu Jan 29 2009 Funda Wang <fwang@mandriva.org> 2.4-1mdv2009.1
+ Revision: 335226
- New version 2.4

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Wed Dec 10 2008 Adam Williamson <awilliamson@mandriva.org> 2.3-3mdv2009.1
+ Revision: 312418
- add gcc4.3fix patch: from Debian (re-diffed), fixes build with GCC 4.3

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Nov 09 2007 Funda Wang <fwang@mandriva.org> 2.3-2mdv2008.1
+ Revision: 107076
- rebuild for new lzma

* Fri Nov 02 2007 Funda Wang <fwang@mandriva.org> 2.3-1mdv2008.1
+ Revision: 105356
- New version 2.3

* Fri Jul 13 2007 Adam Williamson <awilliamson@mandriva.org> 2.2-1mdv2008.0
+ Revision: 51765
- buildrequires desktop-file-utils
- generate and package fd.o icons
- BuildRequires anthy-devel
- drop old menu file and X-Mandriva menu category
- new release 2.2


* Thu Aug 24 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 2.0.1-2.20060803.2mdv2007.0
- fix summary macro usage for menu item
- fix section in menu item
- drop COPYING file as package is GPL
- cosmetics

* Thu Aug 03 2006 Thierry Vignaud <tvignaud@mandriva.com> 2.0.1-2.20060803.1mdv2007.0
- fix build
- XDG menu
- UTUMI Hirosi <utuhiro78@yahoo.co.jp>:
  o latest snapshot (includes fixes for gcc-4.1.1)
  o remove patch0 (kasumi-fix-for-anthy-7716.diff) (merged upstream)

* Mon Jul 03 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 2.0.1-1mdv2007.0
- SECURITY FIX RELEASE

* Thu Dec 15 2005 Thierry Vignaud <tvignaud@mandriva.com> 1.0-1mdk
- new release

* Thu Oct 06 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.10-1mdk
- new release

* Fri Jul 29 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.9-1mdk
- new release

* Sat Apr 09 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 0.8-1mdk
- new release

* Mon Jan 10 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 0.7-2.cvs20050110.1mdk
- latest snapshot

* Sun Jan 02 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 0.7-1mdk
- first spec for mdk
- do not package empty files (tv)

