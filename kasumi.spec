%define	name	kasumi
%define	version	2.2
%define	release	%mkrel 1
%define	Summary	A tool for managing Anthy's dictionary

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		System/Internationalization
License:	GPL
URL:		http://kasumi.sourceforge.jp/
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildrootroot
Requires:	pango atk gtk+2.0
Requires:	anthy >= 6300
BuildRequires:	pango-devel atk-devel gtk+2-devel anthy-devel ImageMagick desktop-file-utils

%description
A tool for managing Anthy's dictionary.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# icons
mkdir -p $RPM_BUILD_ROOT/%{_iconsdir}/hicolor/{16x16,32x32}/apps
cp $RPM_BUILD_ROOT/%{_datadir}/pixmaps/%{name}.png $RPM_BUILD_ROOT/%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert -scale 16 $RPM_BUILD_ROOT/%{_datadir}/pixmaps/%{name}.png $RPM_BUILD_ROOT/%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%find_lang %{name}

# menu
desktop-file-install	--vendor="" \
			--dir $RPM_BUILD_ROOT%{_datadir}/applications \
			--remove-category="Applications" \
			%{name}.desktop

%post
%update_menus
%update_icon_cache hicolor

%postun
%clean_menus
%clean_icon_cache hicolor

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_bindir}/*
%{_datadir}/applications/kasumi.desktop
%{_datadir}/pixmaps/*.png
%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%{_mandir}/man1/kasumi.1*
