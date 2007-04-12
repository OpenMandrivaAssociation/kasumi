%define	name	kasumi
%define	version	2.0.1
%define	release	%mkrel 2.20060803.2
%define	Summary	A tool for managing Anthy's dictionary

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		System/Internationalization
License:	GPL
URL:		http://kasumi.sourceforge.jp/
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildrootroot
Requires:	pango atk gtk+2.0
Requires:	anthy >= 6300
BuildRequires:	pango-devel atk-devel gtk+2-devel

%description
A tool for managing Anthy's dictionary.

%prep
%setup -q

%build
aclocal-1.9
autoconf-2.5x
%configure2_5x

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %{name}

# menu
mkdir -p %{buildroot}%{_menudir}
cat > %{buildroot}%{_menudir}/%{name} <<EOF
?package(%{name}): \
	command="%{_bindir}/kasumi" \
	icon="text_tools_section.png" \
	title="Kasumi" \
	longtitle="%{Summary}" \
	needs="x11" \
	section="System/Text Tools"  \
	xdg="true"
EOF

desktop-file-install	--vendor="" \
			--dir $RPM_BUILD_ROOT%{_datadir}/applications \
			--remove-category="Applications" \
			--add-category="X-MandrivaLinux-System-TextTools" \
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

