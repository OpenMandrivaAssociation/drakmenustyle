

Summary:  Menu Style Configuration
Name:     drakmenustyle
Version:  0.8
Release:  %mkrel 2
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
mkdir -p %buildroot/%_menudir
cat > %buildroot/%_menudir/drakmenustyle << EOF
?package(%{name}): needs="x11" icon="drakmenustyle.png" section="System/Configuration/Other" title="Menu Style" longtitle="Menu Style Configuration" command="%_bindir/%name" \
xdg="true"
EOF

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

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING ChangeLog
%_bindir/*
%_menudir/drakmenustyle
%{_datadir}/applications/mandriva-drakmenustyle.desktop
%_miconsdir/*.png
%_iconsdir/*.png
%_liconsdir/*.png


