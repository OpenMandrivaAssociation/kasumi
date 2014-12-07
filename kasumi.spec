Summary:	A tool for managing Anthy's dictionary
Name:		kasumi
Version:	2.5
Release:	11
Group:		System/Internationalization
License:	GPLv2+
Url:		http://sourceforge.jp/projects/kasumi
Source0:	http://iij.dl.sourceforge.jp/kasumi/37311/%{name}-%{version}.tar.gz
Patch0:		kasumi-2.3-fix-desktop-file.patch

BuildRequires:	desktop-file-utils
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(anthy)
BuildRequires:	pkgconfig(atk)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(pango)
Requires:	anthy >= 6300

%description
A tool for managing Anthy's dictionary.

%prep
%setup -q
%apply_patches

%build
%configure2_5x
%make

%install
%makeinstall_std
%find_lang %{name}

# icons
mkdir -p %{buildroot}/%{_iconsdir}/hicolor/{16x16,32x32}/apps
cp %{buildroot}/%{_datadir}/pixmaps/%{name}.png %{buildroot}/%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert -scale 16 %{buildroot}/%{_datadir}/pixmaps/%{name}.png %{buildroot}/%{_iconsdir}/hicolor/16x16/apps/%{name}.png

# menu
desktop-file-install \
	--vendor="" \
	--dir %{buildroot}%{_datadir}/applications \
	--remove-category="Applications" \
	%{name}.desktop

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%{_bindir}/*
%{_datadir}/applications/kasumi.desktop
%{_datadir}/pixmaps/*.png
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_mandir}/man1/kasumi.1*

