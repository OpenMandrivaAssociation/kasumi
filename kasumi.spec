Summary:	A tool for managing Anthy's dictionary
Name:		kasumi
Version:	2.3
Release:	%{mkrel 3}
Group:		System/Internationalization
License:	GPLv2+
URL:		http://kasumi.sourceforge.jp/
Source0:	http://osdn.dl.sourceforge.jp/%{name}/27825/%{name}-%{version}.tar.gz
Patch0:		kasumi-2.3-fix-desktop-file.patch
# Fix build with GCC 4.3 (includes) - AdamW 2008/12 from Debian
Patch1:		04_gcc4.3fix-mandriva.patch
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
%patch1 -p1 -b .gcc43

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
