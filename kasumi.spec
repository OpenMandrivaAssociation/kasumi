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
BuildRequires:	pango-devel atk-devel gtk+2-devel anthy-devel

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

%find_lang %{name}

# menu
desktop-file-install	--vendor="" \
			--dir $RPM_BUILD_ROOT%{_datadir}/applications \
			--remove-category="Applications" \
			%{name}.desktop

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_bindir}/*
%{_datadir}/applications/kasumi.desktop
%{_datadir}/pixmaps/*.png
%{_mandir}/man1/kasumi.1*
%{_menudir}/%{name}

