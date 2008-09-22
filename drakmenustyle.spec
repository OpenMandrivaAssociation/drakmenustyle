

Summary:  Menu Style Configuration
Name:     drakmenustyle
Version:  0.13
Release:  %mkrel 1
Source0:  %name-%version.tar.bz2
Source1:  drakmenustyle16.png
Source2:  drakmenustyle32.png
Source3:  drakmenustyle48.png
License:  GPL
Group:    System/Configuration/Other
Url:      http://www.mandrivalinux.com/en/cvs.php3
BuildRequires: perl-MDK-Common-devel
Requires: drakxtools => 10.4.53-1mdv2007.0
Requires: perl-Gtk2 >= 1.023-1mdk
BuildRoot: %_tmppath/%name-%version-buildroot
Provides: menudrake
Obsoletes: menudrake
BuildArch: noarch

%description
Drakmenustyle enables to configure the menu style under Mandriva Linux.

%prep
%setup -q

%build
perl -pi -e 's/^use strict/#use strict/g' drakmenustyle

%install
rm -fr $RPM_BUILD_ROOT
%makeinstall_std

#install lang
%find_lang %name

#install menu

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-drakmenustyle.desktop << EOF
[Desktop Entry]
Name=Menu Style Configuration
Comment=Menu Style Configuration
Exec=%{_bindir}/%name
Icon=drakmenustyle
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;X-MandrivaLinux-CrossDesktop;Settings;
NoDisplay=true
EOF

#install menu icon
mkdir -p %buildroot/{%_miconsdir,%_liconsdir}
install -m644 %SOURCE1 %buildroot/%_miconsdir/drakmenustyle.png
install -m644 %SOURCE2 %buildroot/%_iconsdir/drakmenustyle.png
install -m644 %SOURCE3 %buildroot/%_liconsdir/drakmenustyle.png

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING ChangeLog
%_bindir/*
%{_datadir}/applications/mandriva-drakmenustyle.desktop
%_miconsdir/*.png
%_iconsdir/*.png
%_liconsdir/*.png


